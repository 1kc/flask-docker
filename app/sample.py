"""
This is the people module and supports all the REST actions for the
people data
"""

from flask import make_response, abort
from config import db
from models import Sample, SampleSchema


def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        json string of list of people
    """
    # Create the list of people from our data
    sample = Sample.query.order_by(Sample.grain_id).all()

    # Serialize the data for the response
    sample_schema = SampleSchema(many=True)
    data = sample_schema.dump(sample).data
    return data

def create(sample):
    """
    This function creates a new person in the people structure
    based on the passed in person data

    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """

    # Create a person instance using the schema and the passed in person
    schema = SampleSchema()
    new_sample = schema.load(sample, session=db.session).data

    # Add the person to the database
    db.session.add(new_sample)
    db.session.commit()

    # Serialize and return the newly created person in the response
    data = schema.dump(new_sample).data

    return data, 201