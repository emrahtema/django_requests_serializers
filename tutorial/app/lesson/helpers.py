import requests

BASE_URL = "https://randomuser.me/api/?results=200"


def client_response_validation(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if response.ok:
            response = response.json()
            results = response.get("results")
        return results
    return wrapper

@client_response_validation
def make_requests():
    return requests.get(BASE_URL)