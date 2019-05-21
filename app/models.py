from datetime import datetime
from config import db, ma


"""
class Person(db.Model):
    __tablename__ = "person"
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32))
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person
        sqla_session = db.session

"""

class Sample(db.Model):
    __tablename__ = "sample"
    grain_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    l_value = db.Column(db.Numeric())
    harmful = db.Column(db.Boolean())
    photo = db.Column(db.String(32))


class SampleSchema(ma.ModelSchema):
    class Meta:
        model = Sample
        sqla_session = db.session
