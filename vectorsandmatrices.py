# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:13:10 2019

@author: tony
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

M = np.array([ [1,2], [3,4] ])

L = [ [1,2], [3,4] ]

L[0]

L[0][0]


M[0][0]

M[0,0]

M2 = np.matrix([ [1,2], [3,4] ])

M2

#Convert Matrix to np.array
A = np.array(M2)

A

Z= np.zeros(10)

Z

Z= np.zeros((10, 10))
Z

O= np.ones((10, 10))
O

R = np.random.random((10,10))

R

G = np.random.randn(10,10)

G

G.mean()
G.var()

A = np.array([[1, 2], [3,4]])

Ainv = np.linalg.inv(A)

Ainv

Ainv.dot(A)

A.dot(Ainv)

np.linalg.det(A)

np.diag(A)

np.diag([1,2])

A = np.array([1, 2])

B = np.array( [3,4])

np.outer(A, B)

np.inner(A,B)

A.dot(B)

np.diag(A).sum()

np.trace(A)

X = np.random.randn(100,3)

cov = np.cov(X.T)

cov.shape
cov

np.linalg.eigh(cov)

np.linalg.eig(cov)








