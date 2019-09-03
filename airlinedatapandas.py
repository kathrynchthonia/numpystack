# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 03:06:24 2019

@author: tony
"""

# Airline Data
import pandas as pd

df = pd.read_csv('international-airline-passengers.csv', engine='python', skipfooter=3)


df.columns

df.columns = ['month', 'passengers']

df.columns

df['passengers']

#no spaces
df.passengers

df['ones'] = 1

df.head()

from datetime import datetime

datetime.strptime('1949-05', '%Y-%m')

df['dt'] = df.apply(lambda row: datetime.strptime(row['month'], '%Y-%m'), axis=1)

df.info()
