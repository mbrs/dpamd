# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 14:47:42 2019

@author: mbs
"""

from sqlalchemy import create_engine
import pandas as pd
import tia.bbg.datamgr as dm
from tia.bbg import LocalTerminal
import requests


def quotes(s1):
    return "'{}'".format(s1)

mgr = dm.BbgDataManager()
ms = dm.MemoryStorage()

'''
helpers
'''
def quotes(s1):
    return "'{}'".format(s1)



r = requests.post('http://172.20.17.46/api/port_query', json={'isin': ["US1491231015","BE0974293251"]})
ans = pd.DataFrame().from_dict(r.json())

r = requests.get('http://172.20.17.46/landingpage/')