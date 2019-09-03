# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 03:44:24 2019

@author: tony
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
x = np.linspace(0, 10, 100)

y = np.cos(x)

plt.plot(x, y)

plt.show()

plt.plot(x, y)

plt.xlabel('Time')

plt.ylabel('Cos(time)')

plt.title('cos of time')

plt.show()

x = np.linspace(0, 10, 100)

y= np.sin(x)

plt.plot(x,y)

plt.show()