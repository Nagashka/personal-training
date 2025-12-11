from dotenv import load_dotenv
import os
import requests
import json

# Load from .env file
load_dotenv()

class LufthansaAPI:
    def __init__(self):
        self.LH_CLIENT_ID = os.getenv("LH_CLIENT_ID")
        self.LH_CLIENT_SECRET = os.getenv("LH_CLIENT_SECRET")
        self.url = "https://api.lufthansa.com/v1"
        self.token = None
        self.token = self.get_token()

    # Token retrieval method
    def get_token(self):
        url = f"{self.url}/oauth/token"
        response = requests.post(url, data={
            'client_id': self.LH_CLIENT_ID,
            'client_secret': self.LH_CLIENT_SECRET,
            'grant_type': 'client_credentials'
        })
        if response.status_code == 200:
            self.token = response.json()['access_token']
            print("[INFO] Successfully authenticated with Lufthansa API.")
            return self.token
        else:
            print(f"[ERROR] : {response.status_code} - {response.text}")
            return None



if __name__ == "__main__":
    lufthansa_api = LufthansaAPI()
    token = lufthansa_api.get_token()
    print(f"Token d'accès : {lufthansa_api.token}")



#401 token invalid