# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:46:55 2019

@author: tony
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

A = pd.read_csv('data/data_1d.csv', header=None).as_matrix()

x = A[:,0]

y = A[:,1]

plt.scatter(x,y)

x_line = np.linspace(0, 100, 100)

y_line = 2*x_line +1

plt.plot(x_line, y_line)

plt.show()