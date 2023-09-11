import requests
import json

# Base URL of Django app
BASE_URL = 'http://127.0.0.1:8000/api/'

# Test Create operation
def test_create_person():
    print('Testing Create Operation')
    payload = {'name': 'Ngozi Onyemaechi'}
    r = requests.get(BASE_URL, params=payload)
    data = r.json()
    print("Create Operation Response:", data)
    return data['id']

# Test Read Operation
def test_read_person(person_id):
    print("Testing Read Operation")
    r = requests.get(f"{BASE_URL}{person_id}/")
    data = r.json()
    print("Read Operation Response:", data)

# Test Update operation
def test_update_person(person_id):
    print("Testing Update Operation")
    payload = {'name': 'Ngozi Blessing Onyemaechi'}
    r = requests.get(f"{BASE_URL}{person_id}/update/", params=payload)
    data = r.json()
    print("Update Operation Response:", data)

# Test Delete operation
def test_delete_person(person_id):
    print("Testing Delete Operation")
    r = requests.get(f"{BASE_URL}{person_id}/delete/")
    data = r.json()
    print("Delete Operation Response:", data)

if __name__ == '__main__':
    # Create person and get id
    created_person_id = test_create_person()

    # Read person information using id
    test_read_person(created_person_id)

    # Update person's name using their id
    test_update_person(created_person_id)

    #delete person using id
    test_delete_person(created_person_id)