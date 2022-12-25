"""Server for location status app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
from datetime import datetime
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")


@app.route("/login")
def login():
    """View login page."""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
        return redirect("/login")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.fname}!")

    return redirect("/")


@app.route("/create_account")
def create_account():
    """View new account page."""

    return render_template("create_account.html")


@app.route("/locations")
def all_locations():
    """View all locations"""

    locations = crud.get_locations()
    return render_template("all_locations.html", locations=locations)


@app.route("/locations/<location_id>")
def show_location(location_id):
    """Show details on a particular location."""

    location = crud.get_location_by_id(location_id)

    return render_template("location_details.html", location=location)


@app.route("/locations/<location_id>/comments", methods=["POST"])
def create_comment(location_id):
    """Create a new comment for the location."""

    logged_in_email = session.get("user_email")
    comment_input = request.form.get("comment")

    if logged_in_email is None:
        flash("You must log in to submit a comment.")
    elif not comment_input:
        flash("Error: you didn't select a score for your rating.")
    else:
        user = crud.get_user_by_email(logged_in_email)
        location = crud.get_location_by_id(location_id)

        comment = crud.create_comment(user, location, comment_input, datetime.now(), True)
        db.session.add(comment)
        db.session.commit()

        flash(f"Your comment has been submitted: \n{comment.comment}.")

    return redirect(f"/locations/{location_id}")


@app.route("/locations/<location_id>/ratings", methods=["POST"])
def create_rating(location_id):
    """Create a new rating for the location."""

    logged_in_email = session.get("user_email")
    rating_score = request.form.get("rating")

    if logged_in_email is None:
        flash("You must log in to rate a location.")
    elif not rating_score:
        flash("Error: you didn't select a score for your rating.")
    else:
        user = crud.get_user_by_email(logged_in_email)
        location = crud.get_location_by_id(location_id)

        print(f"***** {logged_in_email}: {user} *****")

        if not user:    # Do we need this additional check? user_email in sessions cookie, but user not in database
                        # User was deleted in the database
            print(f"***** User not in database *****")
            print(f"***** {logged_in_email}: {user} *****")
            return redirect("/login")

        print("***** User FOUND *****")
        rating = crud.create_rating(user, location, int(rating_score), datetime.now(), True)
        db.session.add(rating)
        db.session.commit()

        flash(f"You (user: {user}) rated this location {rating_score} out of 5.")

    return redirect(f"/locations/{location_id}")


@app.route("/users")
def all_users():
    """View all users."""

    users = crud.get_users()

    return render_template("all_users.html", users=users)


@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user('fname', 'lname', email, password, '408-000-8888', datetime.now(), True)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")


@app.route("/users/<user_id>")
def show_user(user_id):
    """Show details on a particular user."""

    user = crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user)


# @app.route("/update_rating", methods=["POST"])
# def update_rating():
#     rating_id = request.json["rating_id"]
#     updated_score = request.json["updated_score"]
#     crud.update_rating(rating_id, updated_score)
#     db.session.commit()

#     return "Success"

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
