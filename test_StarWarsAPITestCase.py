
import json

import requests

ENDPOINT = "https://swapi.dev/api/"


#-----to check whether base url is working-------
# response = requests.get(ENDPOINT)
# print('----response: ',response)

# data = response.json
# print('----data: ',data)

# status_code = response.status_code
# print('----status_code: ',status_code)

def test_all_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


def test_people_endpoint():
    response = requests.get(ENDPOINT + 'people')
    assert response.status_code == 200


def test_people_with_height_greater_than_200():
    response = requests.get(ENDPOINT + 'people', params={'height': '> 200'})
    data = response.json()
    count = len(data['results'])
    expected_count = 10
    assert count == expected_count


def test_total_people_count():
    response = requests.get(ENDPOINT + 'people')
    data = response.json()
    count = data['count']
    expected_count = 82
    assert count == expected_count
 
    
    
def test_specific_people():
    response = requests.get(ENDPOINT + 'people')
    data = json.loads(response.text)
    # print('----response data:',data)
    
    # Extract the list of individuals
    individuals = data.get('results', [])
    
    # List of expected names
    expected_people = [ 'Darth Vader', 'Chewbacca', 'Roos Tarpals', 'Rugor Nass',
                        'Yarael Poof', 'Lama Su', 'Tuan Wu', 'Grievous', 'Tarfful', 'Tion Medon']
    
    for person in individuals:
        name = person.get('name')
        assert name in expected_people, f"Expected name '{name}' not found in the API response"
        expected_people.remove(name)
            
    # Verify if all expected names were found
    assert len(expected_people) == 0, f"Some expected individuals were missing from the API response: {expected_people}"
 
    


    

 
 
