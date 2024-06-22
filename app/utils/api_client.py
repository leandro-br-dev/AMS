import requests

def call_external_service(endpoint, payload):
    response = requests.post(endpoint, json=payload)
    return response.json()
