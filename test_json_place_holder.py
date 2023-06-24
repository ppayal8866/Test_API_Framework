
import json
import requests

ENDPOINT = "https://jsonplaceholder.typicode.com"

MAX_POSTS = 101
MAX_COMMENTS = 501
MAX_ALBUMS = 101
MAX_PHOTOS = 5001
MAX_TODOS = 201
MAX_USERS = 11

#-----------------------getting all Resources-----------------------
def test_get_posts():
    for number in range(1, 2):
        response = requests.get(ENDPOINT + '/posts/{}'.format(number))
        assert response.status_code == 200
        data = response.json()
        assert data['userId'] == 1
        assert data['id'] == number


def test_get_comments():
    count = 0
    for number in range(1, 2):
        response = requests.get(ENDPOINT + '/posts/{}/comments'.format(number))
        assert response.status_code == 200
        data = response.json()
        for d in data:
            assert(list(d.keys()) == ['postId', 'id', 'name', 'email', 'body'])
            count += 1
            assert d['postId'] == number
            assert d['id'] == count
def test_all_albums():

        for number in range(1,2):
            response = requests.get(ENDPOINT + '/albums/{}'.format(number))
            assert response.status_code == 200
            data = response.json()
            
            assert data['userId'] == 1
            assert data['id'] == number
            assert data['title'] != ''

def test_all_photos():
    for number in range(1,2):
        response = requests.get(ENDPOINT + '/photos/{}'.format(number))
        assert response.status_code == 200
        data = response.json()
        assert data['albumId'] == 1
        assert data['id'] == number
        assert data['title'] != " " 
        assert data['url'] != " " 
        assert data['thumbnailUrl'] != " "         
           
def test_all_todos():
 
    for number in range(1,2):
        response = requests.get(ENDPOINT + '/todos/{}'.format(number))
        assert response.status_code == 200
        d = response.json()
       
        assert d['userId'] == 1
        assert d['id'] == number
        assert d['title'] != " " 
        assert isinstance(d['completed'],bool) 


def test_users():
    for number in range(1,2):
            response = requests.get(ENDPOINT + '/users/{}'.format(number))
            assert response.status_code == 200
            data = response.json()
            
            assert data['id'] == number
            assert data['name'] != ''
            assert data['username'] != ''
            assert data['email'] != ''
            assert list(data['address'].keys()) == ['street', 'suite', 'city', 'zipcode','geo']
            assert data['phone'] != ''
            assert data['website'] != ''
            assert list(data['company'].keys()) == ['name', 'catchPhrase', 'bs']
   
        

def test_create_posts():
    payload = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
    }
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }

    response = requests.post(ENDPOINT + '/posts', data=json.dumps(payload), headers=headers)
    json_data = response.json()
    assert (json_data)

def test_put_posts():
    payload = {
    'id': 1,
    'title': 'foo',
    'body': 'bar',
    'userId': 1
    }
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }

    response = requests.put(ENDPOINT + '/posts/1', data=json.dumps(payload), headers=headers)
    json_data = response.json()
    assert (json_data)

def test_patch_posts():
    payload = {
    'title': 'foo'
    }
    headers = {'Content-type': 'application/json; charset=UTF-8'}  

    response = requests.patch(ENDPOINT + '/posts/1', data=json.dumps(payload), headers=headers)
    json_data = response.json()
    assert (json_data)    

def test_delete_posts():

    response = requests.delete(ENDPOINT + '/posts/1')
    json_data = response.json()
    assert response.status_code == 200, f"Request failed with status code {response.status_code}"


def test_filtering_resources():
    #  This will return all the posts that belong to the first user
    response = requests.get(ENDPOINT + "/posts?userId=1")
    assert  response.status_code == 200, f"Request failed with status code {response.status_code}"
    json_data = response.json()
    print(json_data)

'''     For validation:

Before validation, please ensure each test case contains a code block

Validate the expected status code is the actual status code

Validate that expected data is somewhere in the response body

In the event of errors and test failures, ensure that the tests have failed. '''


