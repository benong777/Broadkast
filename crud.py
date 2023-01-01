"""CRUD operations."""

from datetime import datetime
from model import db, User, Location, Comment, Rating, Favorite, connect_to_db
# from model import db, User, Location, Comment, Rating, connect_to_db


def create_user(fname, lname, email, password, phone_num, created_at, active):
    """Create and return a new user."""

    user = User(
                fname=fname,
                lname=lname,
                email=email,
                password=password,
                phone_num=phone_num,
                created_at=created_at,
                active=active
                )
    return user


def create_location(name, description, addr, long, lat, created_at, active):
    """Create and return a new location."""

    location = Location(
                        name=name,
                        description=description,
                        addr=addr,
                        long=long,
                        lat=lat,
                        created_at=created_at,
                        active=active
                        )
    return location


def create_comment(user, location, comment, created_at, active):
    """Create a new comment."""

    new_comment = Comment(
                        user=user,
                        location=location,
                        comment=comment,
                        created_at=created_at,
                        active=active
                     )
    return new_comment


def update_comment(comment_id, new_comment):
    """ Update a comment given comment_id and the updated score. """

    comment = Comment.query.get(comment_id)
    comment.comment = new_comment


def create_rating(user, location, rating_score, created_at, active):
    """Create and return a new rating."""

    rating = Rating(
                    user=user,
                    location=location,
                    rating=rating_score,
                    created_at=created_at,
                    active=active
                    )
    return rating


def update_rating(rating_id, new_score):
    """ Update a rating given rating_id and the updated score. """

    rating = Rating.query.get(rating_id)
    rating.score = new_score


def create_favorite(user, location):
    """Add a favorite location to a user."""

    favorite = Favorite(
                        user=user,
                        location=location
                        )

    return favorite


def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_locations():
    """Return all locations."""

    return Location.query.all()


def get_location_by_id(location_id):
    """Return a location by primary key."""

    return Location.query.get(location_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def get_favs_by_user(user_id):
    """Return favorite locations of a user"""

    return Favorite.query.filter(User.user_id == user_id).all()


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
