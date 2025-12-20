import sys
import os
import time
import requests
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "id"))
from identification import LufthansaAPI


class LufthansaFly:
    def __init__(self):
        self.api = LufthansaAPI()
        if self.api.token is None:
            self.token = self.api.get_token()
        else:
            self.token = self.api.token
        self.headers = {'Authorization': f'Bearer {self.token}'}

    def get_fly(self):
        url = f"{self.api.url}/"



if __name__ == "__main__":
    LufthansaFly().get_fly()