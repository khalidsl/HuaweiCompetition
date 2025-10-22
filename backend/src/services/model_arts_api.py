from flask import request, jsonify
import requests
import os

class ModelArtsAPI:
    def __init__(self):
        self.base_url = os.getenv('MODEL_ARTS_BASE_URL')

    def get_model_prediction(self, model_name, data):
        url = f"{self.base_url}/models/{model_name}/predict"
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to get prediction", "status_code": response.status_code}

    def upload_model(self, model_name, model_file):
        url = f"{self.base_url}/models/{model_name}/upload"
        files = {'file': model_file}
        response = requests.post(url, files=files)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to upload model", "status_code": response.status_code}

    def delete_model(self, model_name):
        url = f"{self.base_url}/models/{model_name}"
        response = requests.delete(url)
        if response.status_code == 204:
            return {"message": "Model deleted successfully"}
        else:
            return {"error": "Failed to delete model", "status_code": response.status_code}