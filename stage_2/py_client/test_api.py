import requests
import json

base_url = "http://localhost:8000/api/"


def print_response(response):
    """function to print response data"""
    print(f"Status Code: {response.status_code}")
    if response.text:
        print("Response Data:")
        print(json.dumps(response.json(), indent=2))
    print()


def create_person(data):
    endpoint = base_url
    response = requests.post(endpoint, json=data)
    print("Add Person:")
    print_response(response)
    return response.json() if response.status_code == 201 else None


def retrieve_person(person_id):
    endpoint = f"{base_url}{person_id}/"
    response = requests.get(endpoint)
    print("Retrieve Person:")
    print_response(response)


def update_person(person_id, data):
    endpoint = f"{base_url}{person_id}/"
    response = requests.put(endpoint, json=data)
    print("Update Person:")
    print_response(response)


def delete_person(person_id):
    endpoint = f"{base_url}{person_id}/"
    response = requests.delete(endpoint)
    print("Delete Person:")
    print_response(response)


if __name__ == "__main__":
    # Test the CRUD operations
    person_data = {
        "name": "John Doe",
    }

    test_person = create_person(person_data)

    if test_person:
        retrieve_person(test_person["id"])

        updated_person_data = {
            "name": "John Updated",
        }

        update_person(
            test_person["id"],
            updated_person_data
        )
        retrieve_person(test_person["id"])
        delete_person(test_person["id"])
