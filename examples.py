# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:52:03 2019

@author: mbs
"""

#example

import dpamd as dpamd

request_class = dpamd.Request()
secid_list = ["US1491231015","BE0974293251"]

example_portdata   = request_class.port_query(secid_list)
example_portfields  = request_class.port_fields()
example_listFunds  = request_class.list_funds()
example_newfunddbreport  = request_class.newfunddb_report(54441)