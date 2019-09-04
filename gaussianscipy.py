# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:16:06 2019

@author: tony
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm

norm.pdf(0)

norm.pdf(0, loc=5, scale=10)

r = np.random.randn(10)

norm.pdf(r)

norm.logpdf(r)

norm.cdf(r)

norm.logcdf(r)

r = np.random.randn(10000)

plt.hist(r, bins=100, color='indigo')

r= 10*np.random.randn(10000) + 5

plt.show()

r= np.random.randn(10000, 2)

plt.scatter(r[:,0], r[:,1], color='pink')

plt.show()

r[:,1] = 5*r[:,1] +2

plt.scatter(r[:,0], r[:,1], color='magenta')

plt.show()

plt.axis('equal')

plt.show()

#covariance matrix
cov = np.array([[1,.8], [.8,3]])

from scipy.stats import multivariate_normal as mvn

mu = np.array([0,2])

r = mvn.rvs(mean=mu, cov=cov, size=1000)

plt.scatter(r[:,0], r[:,1], color='indigo')

plt.axis('equal')

plt.show()

r = np.random.multivariate_normal(mean=mu, cov=cov, size=1000)

plt.scatter(r[:,0], r[:,1], color='purple')

plt.axis('equal')

plt.show()

#Other scipy functions
x= np.linspace(0, 100, 10000)

y= np.sin(x) + np.sin(3*x) +np.sin(5*x)

plt.plot(y)

plt.show()

Y = np.fft.fft(y)

plt.plot(np.abs(Y))

plt.show()

2*np.pi*16/100

2*np.pi*48/100

2*np.pi*80/100








