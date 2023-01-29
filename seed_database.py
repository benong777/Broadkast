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