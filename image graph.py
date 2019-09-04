# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:10:40 2019

@author: tony
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('./data/train.csv')

df.shape

M = df.values

im = M[0, 1:]

im.shape

im = im.reshape(28,28)

im.shape

plt.imshow(im)

M[0,0]


plt.imshow(im, cmap='pink')

plt.show()

plt.imshow(255-im, cmap='pink')

plt.show()