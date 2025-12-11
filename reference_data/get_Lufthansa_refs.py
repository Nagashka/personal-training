import os
import time
import panda as pd
from identification import LufthansaAPI

wanted_items = 10400 # nb airports to fetch (default 10400 for all)
pd.set_option('display.max_rows', wanted_items)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', None)

class LufthansaRefs:
    def __init__(self):
        self.api = LufthansaAPI()
        self.headers = {'Authorization': f'Bearer {self.token}'}
        if api.token is None:
            self.token = self.api.get_token()
        else
            self.token = self.api.token

    def get_airports(self):
        url = f"{self.api.url}/references/airports"
        airports_df = pd.DataFrame()
        
