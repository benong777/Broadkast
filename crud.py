"""CRUD operations."""

from datetime import datetime
from model import db, User, Location, Comment, Rating, Bookmark, History, connect_to_db
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


# def create_location(name, description, addr, lat, lng, created_at, active):
def create_location(name, addr, lat, lng, created_at, active):
    """Create and return a new location."""

    location = Location(
                        name=name,
                        # description=description,
                        addr=addr,
                        lng=lng,
                        lat=lat,
                        created_at=created_at,
                        active=active
                        )
    return location


def create_comment(user, location, comment, created_at, active):
    """Create a new comment."""

    comment = Comment(
                        user=user,
                        location=location,
                        comment=comment,
                        created_at=created_at,
                        active=active
                     )
    return comment


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


def add_bookmark(user_id, location_id):
    """Add a bookmark location to a user."""

    bookmark = Bookmark(
                        user_id=user_id,
                        location_id=location_id
                        )

    return bookmark


def add_history(user_id, location_id):
    """Add search location result to history."""

    history = History(
                        user_id=user_id,
                        location_id=location_id,
                     )
    return history



#---------------------------------
# Users
#---------------------------------
def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


#---------------------------------
# Locations
#---------------------------------
def get_locations():
    """Return all locations."""

    return Location.query.all()


def get_location_by_id(location_id):
    """Return a location by primary key."""

    return Location.query.get(location_id)


def get_location_by_name(name):
    """Return a location by name."""

    return Location.query.filter(Location.name == name).first()


def get_location_by_addr(addr):
    """Return a location by addr."""

    return Location.query.filter(Location.addr == addr).first()


def get_location_by_name_and_addr(name, addr):
    """Return a location by name and addr."""

    return Location.query.filter(Location.name == name, Location.addr == addr).first()



#---------------------------------
# Bookmarks
#---------------------------------
def get_bookmark_by_user(user_id):
    """Return bookmark locations of a user"""

    return Bookmark.query.filter(Bookmark.user_id == user_id).all()


def get_bookmark_by_user_and_location(user_id, location_id):
    """Return bookmark based on user and location id."""

    return Bookmark.query.filter(Bookmark.user_id == user_id, Bookmark.location_id == location_id).first()


#---------------------------------
# History
#---------------------------------
def get_history_by_user(user_id):
    """Return user's search history."""

    # ??? 
    # return History.query.filter(History.user_id == user_id).all()
    return History.query.filter(History.user_id == user_id).all()


def get_history_by_location(location_id):
    """Return location in search history based on location id."""

    return History.query.filter(History.location_id == location_id).all()


def get_history_by_user_and_location(user_id, location_id):
    """Return history item based on user and location id."""

    return History.query.filter(History.user_id == user_id, History.location_id == location_id).first()

#---------------------------------
# Comments
#---------------------------------
def get_comments_by_location(location_id):
    """Return comments for a location"""

    return Comment.query.filter(Comment.location_id == location_id).order_by(Comment.created_at.desc()).all()



if __name__ == "__main__":
    from server import app
    connect_to_db(app)
