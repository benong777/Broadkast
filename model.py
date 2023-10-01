"""Models for location status app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    phone_num = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    active = db.Column(db.Boolean)

    comments = db.relationship("Comment", back_populates="user")
    ratings = db.relationship("Rating", back_populates="user")
    bookmarks = db.relationship("Bookmark", back_populates="user")
    history = db.relationship("History", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"


class Location(db.Model):
    """A location."""

    __tablename__ = "locations"

    location_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    # description = db.Column(db.Text)
    addr = db.Column(db.String)
    lat  = db.Column(db.Float)
    lng = db.Column(db.Float)
    website = db.Column(db.String)
    phone = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    active = db.Column(db.Boolean)

    comments = db.relationship("Comment", back_populates="location")
    ratings = db.relationship("Rating", back_populates="location")
    bookmarks = db.relationship("Bookmark", back_populates="location")
    history = db.relationship("History", back_populates="location")

    def __repr__(self):
        return f"<Location location_id={self.location_id} name={self.name} addr={self.addr}>"


class Comment(db.Model):
    """A comment."""

    __tablename__ = "comments"

    comment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    location_id = db.Column(db.Integer, db.ForeignKey("locations.location_id"))
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    active = db.Column(db.Boolean)

    user = db.relationship("User", back_populates="comments")
    location = db.relationship("Location", back_populates="comments")

    # def __repr__(self):
    #     return f"<Comment user={self.user} location={self.location} comment={self.comment}>"

    def __repr__(self):
        return f'{{"comment_id": {self.comment_id}, "user_name": "{self.user_id}", "location_id": {self.location_id}, "comment": "{self.comment}"}}'
        # return {"comment_id": {self.comment_id}, "user_name": "{self.user_id}", "location_id": {self.location_id}, "comment": "{self.comment}"}


class Rating(db.Model):
    """A rating."""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    location_id = db.Column(db.Integer, db.ForeignKey("locations.location_id"))
    rating = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    active = db.Column(db.Boolean)

    user = db.relationship("User", back_populates="ratings")
    location = db.relationship("Location", back_populates="ratings")

    def __repr__(self):
        return f"<Rating rating_id={self.rating_id} rating={self.rating}>"


class Bookmark(db.Model):
    """User's bookmark location"""

    __tablename__ = "bookmarks"

    bookmark_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    location_id = db.Column(db.Integer, db.ForeignKey("locations.location_id"))

    user = db.relationship("User", back_populates="bookmarks")
    location = db.relationship("Location", back_populates="bookmarks")

    def __repr__(self):
        return f"<Bookmark user={self.user} location={self.location}"


class History(db.Model):
    """User's search history."""

    __tablename__ = "history"

    history_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    location_id = db.Column(db.Integer, db.ForeignKey("locations.location_id"))

    user = db.relationship("User", back_populates="history")
    location = db.relationship("Location", back_populates="history")

    def __repr__(self):
        return f"<History location={self.location} user={self.user}"


def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
