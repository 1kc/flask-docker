import pytest
import connexion
import config
from flask import request, jsonify

flask_app = config.connex_app
flask_app.add_api('swagger.yml')

@pytest.fixture
def client():
    with flask_app.app.test_client() as client:
        yield client

def test_get_all(client):
    response = client.get('/api/sample')
    assert response.status_code == 200


def test_get_one(client):
    """Test that a single sample could be retrieved"""

    # add a sample to be checked
    create_response = client.post('/api/sample', json={
            "harmful": True,
            "l_value": 1.0,
           "photo": "grain.jpg"
    })

    # get the new sample's id
    new_id = create_response.get_json()['grain_id']

    get_response = client.get('/api/sample/{}'.format(new_id))
    retrieved_id = get_response.get_json()['grain_id']

    assert new_id == retrieved_id

def test_create_harmful(client):
    """Test that harmful samples could be added"""
    response = client.post('/api/sample', json={
            "harmful": True,
            "l_value": 1.0,
            "photo": "grain.jpg"
    })
    json = response.get_json()

    # should get back the added sample in the response
    assert json['harmful'] == True

def test_create_non_harmful(client):
    """Test that non-harmful samples could be added"""
    response = client.post('/api/sample', json={
            "harmful": False,
            "l_value": 1.0,
            "photo": "grain.jpg"
    })
    json = response.get_json()
    assert json['harmful'] == False

def test_create_l_value(client):
    """Test deciaml l values could be added"""
    response = client.post('/api/sample', json={
            "harmful": True,
            "l_value": 123.456,
            "photo": "grain.jpg"
    })
    json = response.get_json()
    assert json['l_value'] == 123.456

def test_create_photo(client):
    """Test that a photo link could added"""
    response = client.post('/api/sample', json={
            "harmful": True,
            "l_value": 1.0,
            "photo": "grain.jpg"
    })
    json = response.get_json()
    assert json['photo'] == 'grain.jpg'

def test_delete_response(client):
    """Test that the delete api could be called"""

    # add a sample to be deleted
    create_response = client.post('/api/sample', json={
            "harmful": True,
            "l_value": 1.0,
           "photo": "grain.jpg"
    })

    # get the added sample's id
    json = create_response.get_json()
    delete_id = json['grain_id']

    # delete the sample
    delete_response = client.delete('/api/sample/{}'.format(delete_id))

    expected_body = b'Sample %d deleted' % delete_id

    assert expected_body in delete_response.data

def test_delete_sample(client):
    """Test that a sample could be deleted"""

    # add a sample to be deleted
    create_response = client.post('/api/sample', json={
            "harmful": True,
            "l_value": 1.0,
           "photo": "grain.jpg"
    })

    # get the added sample's id
    json = create_response.get_json()
    delete_id = json['grain_id']

    # delete the sample
    delete_response = client.delete('/api/sample/{}'.format(delete_id))

    # check the deleted sample is not there anymore
    get_response = client.get('/api/sample/{}'.format(delete_id))

    assert get_response.status_code == 404