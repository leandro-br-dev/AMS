# app/orchestration/service_caller.py
import requests
from app.models import Service

class ServiceCaller:
    @staticmethod
    def call_service(service, data):
        headers = {'Content-Type': 'application/json'}
        response = requests.post(service.endpoint_url, json=data, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            return None
