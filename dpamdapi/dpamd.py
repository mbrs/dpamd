# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 14:47:42 2019

@author: mbs
"""

import pandas as pd
import requests

class Request():
    
    def __init__(self):
        self.api_url = 'http://172.20.17.46/api/'

    def port_query(self,secid_list):
        raw = requests.post(self.api_url+'port_query', json={'isin':secid_list})
        return  pd.DataFrame().from_dict(raw.json())

        
