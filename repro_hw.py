#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 16:32:20 2019

@author: mulderg
"""

import pandas as pd
from statsmodels.tsa.api import ExponentialSmoothing

ts_df = pd.read_csv("ts.csv")
ts = pd.Series(ts_df.val, index=ts_df.date)
cfg = {'damped': False, 'seasonal': 'add', 'seasonal_periods': 48}
model = ExponentialSmoothing(endog=ts, **cfg).fit()
