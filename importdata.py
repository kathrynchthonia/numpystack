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

M = X.as_matrix()


type(M)


X[0]

X.head()

type(X[0])


X.iloc[0]

#depreciated
X.ix[1]

type(X.iloc[0])

X[[0,2]]

X[ X[0] < 5]

X[0] < 5

type(X[0] < 5)











































