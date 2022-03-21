# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 14:11:54 2022

@author: Rich
"""

import pytrends
from pytrends.request import TrendReq

pytrends = TrendReq(hl="en-US", tz=360)
pytrends.build_payload(kw_list=["Bitcoin"])

df = pytrends.interest_over_time()
df["Bitcoin"].plot(figsize=(20, 7), color="black", linewidth=5)
