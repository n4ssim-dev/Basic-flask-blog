import requests

def get_age(name,country_id):
    response = requests.get(f'https://api.agify.io?name={name}&country_id={country_id}')
    if response.status_code == requests.codes.ok:
        response_dict = response.json()
        response_age = response_dict["age"]
        return response_age
    else:
        print(f'There seems to be an error: {response.status_code} ; {response.text}')

def get_gender(name):
    response = requests.get(f'https://api.genderize.io?name={name}')
    if response.status_code == requests.codes.ok:
        response_name = response.json()["gender"]
        return response_name
    else:
        print(f'There seems to be an error: {response.status_code} ; {response.text}')