from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

client_secret = os.getenv('client_secret')
client_id = os.getenv('client_id')
grant_type = os.getenv('grant_type')

class _id():
    def __init__(self, url):
        self.url = url
        self.client_secret = client_secret
        self.client_id = client_id
        self.data = {"grant_type": grant_type, "client_id": client_id, "client_secret": client_secret}
        self.token = self.get_token()

    def get_token(self):
            self.token_response = requests.post(url + 'oauth/token', data=self.data) #Get token
            if self.token_response.status_code == 200: #Token validated
                token = token_response.json().get('access_token')
            else: #Token Echec
                token = None
                print("Token error:", token_response.text)
            return token