# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:52:03 2019

@author: mbs
"""

#example

import dpamd as dpamd

request_class = dpamd.Request()
secid_list = ["US1491231015","BE0974293251"]

r = request_class.port_query(secid_list)
r2 = request_class.port_fields()
