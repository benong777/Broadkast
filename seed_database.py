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

# Create locations, store them in list so we can use them
# to create fake ratings
locations_in_db = []
for location in location_data:
    name, description, addr = (
        location["name"],
        location["description"],
        location["addr"],
    )
    # release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")

    db_location = crud.create_location(name, description, addr, 32.4, 16.8, datetime.now(), True)
    locations_in_db.append(db_location)

model.db.session.add_all(locations_in_db)
model.db.session.commit()

# Create 10 users; each user will make 10 comments
for n in range(10):
    email = f"user{n+1}@test.com"
    password = "test"

    user = crud.create_user(f"fname_{n}", f"lname_{n}", email, password, f"408-000-{n}{n}{n}{n}", datetime.now(), True)
    model.db.session.add(user)

    for _ in range(5):
        random_location = choice(locations_in_db)

        comment = crud.create_comment(user, random_location, f"comment_{n+1}", datetime.now(), True)
        model.db.session.add(comment)

model.db.session.commit()