from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

client_secret = os.getenv('client_secret')
client_id = os.getenv('client_id')
grant_type = os.getenv('grant_type')

token = None

def get_token(url):
        data = {"grant_type": grant_type, "client_id": client_id, "client_secret": client_secret}
        token_response = requests.post(url + 'oauth/token', data=data) #Get token
        if token_response.status_code == 200: #Token validated
            token = token_response.json().get('access_token')
        else: #Token Echec
            token = None
            print("Token error:", token_response.text)
        return token