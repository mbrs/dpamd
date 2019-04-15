# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 14:47:42 2019

@author: mbs
"""


import pandas as pd
import requests

class Ssot_Request():
    
    def __init__(self):
        self.api_url = 'http://172.20.17.46/api/'

    def port_query(self,secid_list):
        raw = requests.post(self.api_url+'port_query', json={'isin':secid_list})
        return  pd.DataFrame().from_dict(raw.json())
    
    def port_query_rating(self,secid_list):
        raw = requests.post(self.api_url+'port_query_rating', json={'isin':secid_list})
        return  pd.DataFrame().from_dict(raw.json())

    def port_fields(self):
       raw = requests.post(self.api_url+'port_fields')
       return  pd.DataFrame().from_dict(raw.json())       

    def list_funds(self):
       raw = requests.get(self.api_url+'list_funds')
       return  pd.DataFrame().from_dict(raw.json())   

    def newfunddb_report(self,code):
       raw = requests.get(self.api_url+'newfunddb_report/'+str(code))
       return  pd.DataFrame().from_dict(raw.json())   


