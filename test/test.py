import pytest
import requests

# Define the base URL for the API
BASE_URL = 'http://localhost:8000'

@pytest.fixture
def sample_person():
    return {
        'name': 'Okai Musa'
}

def test_create_person(sample_person):

    response = requests.post(f'{BASE_URL}/api', json=sample_person)
    assert response.status_code == 200

def test_get_person():
    response = requests.get(f'{BASE_URL}/api/user_id?name=Okai%20Musa')
    assert response.status_code == 200

def test_update_person(sample_person):
    updated_data = {'name': 'Okai Ibrahim'}
    response = requests.put(f'{BASE_URL}/api/user_id?name=Okai%20Musa', json=updated_data)
    assert response.status_code == 200

def test_delete_person():
    response = requests.delete(f'{BASE_URL}/api/user_id?name=Okai%20Ibrahim')
    assert response.status_code == 200