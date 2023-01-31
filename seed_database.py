"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb ratings")
os.system("createdb ratings")

model.connect_to_db(server.app)
model.db.create_all()

# Load data from JSON file
with open("data/locations.json") as f:
    location_data = json.loads(f.read())

# Create locations, store them in list
locations_in_db = []
for location in location_data:
    # name, description, addr = (
    name, addr, lat, lng, website, phone = (
        location["name"],
        # location["description"],
        location["addr"],
        location["lat"],
        location["lng"],
        location["website"],
        location["phone"],
    )
    # release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")

    db_location = crud.create_location(name, addr, lat, lng, website, phone, datetime.now(), True)
    locations_in_db.append(db_location)

model.db.session.add_all(locations_in_db)
model.db.session.commit()


# # Create users; each user will make n comments
with open("data/users.json") as f:
    user_data = json.loads(f.read())

# Create locations, store them in list
users_in_db = []
for user in user_data:
    fname, lname, email, password, phone_num = (
        user["fname"],
        user["lname"],
        user["email"],
        user["password"],
        user["phone_num"],
    )
    # release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")

    db_user = crud.create_user(fname, lname, email, password, phone_num, datetime.now(), True)
    users_in_db.append(db_user)

model.db.session.add_all(users_in_db)
model.db.session.commit()


# Create history for testing
with open("data/history.json") as f:
    history_data = json.loads(f.read())

# Create locations in history table
history_in_db = []
for item in history_data:
    user_id, location_id = (
        item["user_id"],
        item["location_id"],
    )
    # release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")

    db_history = crud.add_history(user_id, location_id)
    history_in_db.append(db_history)

model.db.session.add_all(history_in_db)
model.db.session.commit()


# Create bookmark for testing
with open("data/bookmark.json") as f:
    bookmark_data = json.loads(f.read())

# Create bookmarks, store them in list
bookmark_in_db = []
for bookmark in bookmark_data:
    user_id, location_id = (
        bookmark["user_id"],
        bookmark["location_id"],
    )

    db_bookmark = crud.add_bookmark(user_id, location_id)
    bookmark_in_db.append(db_bookmark)

model.db.session.add_all(bookmark_in_db)
model.db.session.commit()


# # Create comments for testing
# with open("data/comments.json") as f:
#     comment_data = json.loads(f.read())

# # Create comments, store them in list
# comments_in_db = []
# for comment in comment_data:
#     user_id, location_id, comment = (
#         comment["user_id"],
#         comment["location_id"],
#         comment["comment"],
#     )

#     db_comment = crud.create_comment(user_id, location_id, comment, datetime.now(), True)
#     comments_in_db.append(db_comment)

# model.db.session.add_all(comments_in_db)
# model.db.session.commit()


# # Create users; each user will make n comments
# for n in range(3):
#     email = f"user{n+1}@test.com"
#     password = "test"

#     user = crud.create_user(f"fname_{n}", f"lname_{n}", email, password, f"408-000-{n}{n}{n}{n}", datetime.now(), True)
#     model.db.session.add(user)

#     for i in range(3):
#         random_location = choice(locations_in_db)

#         comment = crud.create_comment(user, random_location, f"\t comment_{i+1}", datetime.now(), True)
#         model.db.session.add(comment)

#         # item = crud.add_history(user, random_location)
#         # model.db.session.add(item)
# 
# model.db.session.commit()