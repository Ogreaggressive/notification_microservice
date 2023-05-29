import requests
from flask import jsonify

class user_admin_adapter:
    def __init__(self):
        self.baseUrl = "https://65db-181-177-183-178.ngrok-free.app/"

    def get_email(self, userID):
        endpoint = '/users/'+str(userID)
        url = self.baseUrl + endpoint

        try:
            response = requests.get(url)
            print(response)
            if response.status_code == 200:
                data = response.json()
                email = data.get("email")
                print(response)
                return email
            else:
                print("Failed getting email:", response.status_code)
                return None
        except requests.exceptions.RequestException as e:
            print("Error occurred while communicating with the microservice:", str(e))
            return None