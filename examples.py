# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:52:03 2019

@author: mbs
"""

#Using the class

import dpamd as dpamd

request_class = dpamd.Ssot_Request()
secid_list = ["US1491231015","BE0974293251"]
secid_list_bonds = ["FR0011052661","DE000A2TSTD0"]

example_portdata   = request_class.port_query(secid_list)
example_portdata_rating = request_class.port_query_rating(secid_list_bonds)
example_portfields  = request_class.port_fields()
example_listFunds  = request_class.list_funds()
example_newfunddbreport  = request_class.newfunddb_report(54437)


























## RAW

import requests
import pandas as pd

secid_list_bonds = ["FR0011052661","DE000A2TSTD0"]
api_url = 'http://172.20.17.46/api/'
raw = requests.post(api_url+'port_query_rating', json={'isin':secid_list})
pd.DataFrame().from_dict(raw.json())
