import requests
from flask import jsonify

class user_auth_adapter:
    def __init__(self):
        self.baseUrl = "https://68ac-181-177-183-178.ngrok-free.app/"

    def get_userID(self, endpoint):
        url = self.baseUrl + endpoint

        try:
            response = requests.get(url)
            print(response)
            if response.status_code == 200:
                data = response.json()
                userID = data.get("userID")
                print(response)
                return userID
            else:
                print("Failed getting userID:", response.status_code)
                return None
        except requests.exceptions.RequestException as e:
            print("Error occurred while communicating with the microservice:", str(e))
            return None

    def get_id_registering(self):
        endpoint = '/register'
        return self.get_userID(endpoint)

    def get_id_logging_in(self):
        endpoint = '/login'
        return self.get_userID(endpoint)
        