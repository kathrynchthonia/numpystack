# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:18:48 2019

@author: tony
"""

import numpy as np
import matplotlib.pyplot as plt


X = []

for line in open('data_2d.csv'):
    row = line.split(',')
    sample = list(map(float, row))
    X.append(sample)
X = np.array(X)
print(X)

#pandas method
import pandas as pd
X = pd.read_csv('data_2d.csv', header=None)

type(X)

X.info()

X.head()

X.head(4)