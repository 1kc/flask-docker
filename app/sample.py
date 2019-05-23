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

def read_one(sample_id):
    """
    This function responds to a request for /api/people/{person_id}
    with one matching person from people

    :param person_id:   Id of person to find
    :return:            person matching id
    """
    # Get the person requested
    sample = Sample.query.filter(Sample.grain_id == sample_id).one_or_none()

    # Did we find a person?
    if sample is not None:

        # Serialize the data for the response
        sample_schema = SampleSchema()
        data = sample_schema.dump(sample).data
        return data

    # Otherwise, nope, didn't find that person
    else:
        abort(
            404,
            "Person not found for Id: {sample_id}".format(sample_id=sample_id),
        )

def delete(sample_id):
    """
    This function deletes a sample from the sample structure

    :param sample_id:   Id of the sample to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the person requested
    sample = Sample.query.filter(Sample.grain_id == sample_id).one_or_none()

    # Did we find a person?
    if sample is not None:
        db.session.delete(sample)
        db.session.commit()
        return make_response(
            "Sample {sample_id} deleted".format(sample_id=sample_id), 200
        )

    # Otherwise, nope, didn't find that sample
    else:
        abort(
            404,
            "Sample not found for Id: {sample_id}".format(sample_id=sample_id),
        )
