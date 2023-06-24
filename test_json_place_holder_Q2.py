import json

import requests

from test_json_place_holder import ENDPOINT

BASE_URL = "https://jsonplaceholder.typicode.com"

MAX_POSTS = 101
MAX_COMMENTS = 501
MAX_ALBUMS = 101
MAX_PHOTOS = 5001
MAX_TODOS = 201
MAX_USERS = 11

def generate_endpoint(resource_type, resource_id):
    return f"{BASE_URL}/{resource_type}/{resource_id}"


def generate_headers():
    # If you have specific headers to include, generate them here
    headers = {
        'Content-Type': 'application/json',
        # Add any other headers you need
    }
    return headers


def generate_request_body():
    # If you need to send a request body, generate it here Otherwise, return None
    
    request_body = {
        'key': 'value',
        # Add the necessary data for the request body
    }
    return request_body


def send_http_request(method, endpoint, request_body=None, headers=None):
    if headers is None:
        headers = generate_headers()
    if request_body is None:
        response = requests.request(method, endpoint, headers=headers)
    else:
        response = requests.request(method, endpoint, headers=headers, json=request_body)
    return response


def parse_response(response):
    status_code = response.status_code
    data = response.json()
    return status_code, data



# Rest of your code...

def test_get_posts():
    for number in range(1, 2):
        endpoint = generate_endpoint("posts", number)
        response = send_http_request('GET', endpoint)
        status_code, data = parse_response(response)
        
        assert status_code == 200
        assert data['userId'] == 1
        assert data['id'] == number

def test_get_comments():
    for number in range(1, 2):
        endpoint = generate_endpoint("comments", number)
        response = send_http_request('GET', endpoint)
        status_code, data = parse_response(response)
        
        assert status_code == 200
        assert list(data.keys()) == ['postId', 'id', 'name', 'email', 'body']
        assert data['postId'] == number
        assert data['id'] == number

def test_all_albums():
    for number in range(1, 2):
        endpoint = generate_endpoint("albums", number)
        response = send_http_request('GET', endpoint)
        status_code, data = parse_response(response)
        
        assert status_code == 200
        assert data['userId'] == 1
        assert data['id'] == number
        assert data['title'] != ''
        
def test_all_photos():
    for number in range(1,2):
        endpoint = generate_endpoint('photos',number)
        response = send_http_request('GET', endpoint)
        status_code, data = parse_response(response)
        
        assert status_code == 200
        assert data['albumId'] == 1
        assert data['id'] == number
        assert data['title'] != " " 
        assert data['url'] != " " 
        assert data['thumbnailUrl'] != " "         
           
def test_all_todos():
 
    for number in range(1,2):
        endpoint = generate_endpoint('todos',number)
        response = send_http_request('GET', endpoint)
        status_code, data = parse_response(response)
        
        assert status_code == 200

        assert data['userId'] == 1
        assert data['id'] == number
        assert data['title'] != " " 
        assert isinstance(data['completed'],bool) 


def test_users():
    for number in range(1,2):
        endpoint = generate_endpoint('users',number)
        response = send_http_request('GET', endpoint)
        status_code, data = parse_response(response)
        
        assert status_code == 200
        assert data['id'] == number
        assert data['name'] != ''
        assert data['username'] != ''
        assert data['email'] != ''
        assert list(data['address'].keys()) == ['street', 'suite', 'city', 'zipcode','geo']
        assert data['phone'] != ''
        assert data['website'] != ''
        assert list(data['company'].keys()) == ['name', 'catchPhrase', 'bs']           
            

#  Failed test cases

def test_failed_endpoint():
    endpoint = generate_endpoint("nonexistent", 1)
    response = send_http_request('GET', endpoint)
    status_code, _ = parse_response(response)

    expected_status_code = 404  # Assuming the endpoint returns a 404 status code for non-existent resources
    assert status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {status_code}"
