# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 03:42:32 2019

@author: tony
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

L = [1,2,3]
A= np.array([1,2,3])


for e in L:
    print(e)
for e in A:
    print(e)
    
L.append(4)

L

L= L + [5]

L

L2 = []

for e in L:
    L2.append(e + e)
    
L2

A + A

2*A

2*L

L2 = []

for e in L:
    L2.append(e*e)

L2

A**2

np.sqrt(A)

np.log(A)

np.exp(A)

#vector multiplication

a = np.array([1,2])

b= np.array([2,1])

dot=0

for e, f in zip(a, b):
    dot += e*f
    
dot

np.dot(a, b)

a.dot(b)

b.dot(a)

#element wise multiplication
a*b

np.sum(a*b)

(a*b).sum()

#vector length
amag = np.sqrt( (a*a).sum() )

amag

amag = np.linalg.norm(a)

amag

cosangle  = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))

cosangle

angle = np.arccos(cosangle)

angle