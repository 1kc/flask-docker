import os
from config import db
from models import Sample

# Data to initialize database with
'''
PEOPLE = [
    {"fname": "Doug", "lname": "Farrell"},
    {"fname": "Kent", "lname": "Brockman"},
    {"fname": "Bunny", "lname": "Easter"},
]
'''

SAMPLE = [
    {"l_value": 2.0, "harmful": True, "photo": "photo1.jpg"},
    {"l_value": 1.5, "harmful": False, "photo": "photo2.jpg"},
    {"l_value": 10.5, "harmful": True, "photo": "photo3.jpg"},
]

# Create the database
db.create_all()

# iterate over the PEOPLE structure and populate the database
'''
for person in PEOPLE:
    p = Person(lname=person.get("lname"), fname=person.get("fname"))
    db.session.add(p)
'''

for sample in SAMPLE:
    s = Sample(l_value=sample.get("l_value"), harmful=sample.get("harmful"), photo=sample.get("photo"))
    db.session.add(s)

db.session.commit()
