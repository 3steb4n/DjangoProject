import requests

def generate_request(url, auth):
    response = requests.post(url, auth)

    if response.status_code == 200:
        return response.json()