# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:01:43 2022

@author: Administrator
"""

### Euler-Maruyama SDE simulation: PyEM
### https://github.com/adamskiij99/PyEM
### Skip to bottom for common/interesting SDEs that you may wish to experiment with.

two = False     # Set to True if your SDE Y depends on another SDE X
both = True     # Set to True if you want both Y and X to be displayed

multiple_dependent_processes = True

import numpy as np
np.random.seed(999)
import matplotlib.pyplot as plt

N = 300         # No. time steps (terminal time is 1)
n = 10          # No. sample paths
rho = -0.6      # Correlation between BMs
dt = np.ones(N) / N
sqrtdt = np.sqrt(dt[0])
dW1 = np.random.normal(0, sqrtdt, [n, N])
dW2 = np.random.normal(0, sqrtdt, [n, N])
W1 = np.zeros([n, N])   # BM (increments) for X
W2 = np.zeros([n, N])   # BM (increments) for Y
for i in range(n):
    W1[i] = dW1[i].cumsum()
    W2[i] = dW2[i].cumsum()

def F(x, xi, t):    # Drift function mu for X
    return -0 * (xi**3 - xi) + 15 * (np.mean(x) - xi)

def G(x, xi, t):    # Volatility function sigma for X
    return 0.1

X = np.zeros([n, N])
X_0 = np.zeros(n)  # Initial distribution of X
X.T[-1] = X_0

if multiple_dependent_processes:    # Keep two=False for this. Easily modifiable if required.
    for t in range(N):      # Euler-Maruyama estimation of X
        for i in range(n):
            X[i, t] = X[i, t - 1] + F(X[:, t - 1], X[i, t - 1], t / N) * dt[0] + G(X[:, t - 1], X[i, t - 1], t / N) * dW1[i, t]

else:
    for t in range(N):      # Euler-Maruyama estimation of X
        for i in range(n):
            X[i, t] = X[i, t - 1] + F(X[i, t - 1], t / N) * dt[0] + G(X[i, t - 1], t / N) * dW1[i, t]
    
    if two:
        def H(y, x, t):     # Drift function mu for Y
            return 0.3 * y
        
        def I(y, x, t):     # Volatility function sigma for Y
            return np.sqrt(x) * y
        
        Y = np.zeros([n, N])
        Y_0 = np.ones(n)    # Initial distribution of Y
        Y.T[-1] = X_0
        
        for t in range(N):      # Euler-Maruyama estimation of Y
            for i in range(n):
                Y[i, t] = Y[i, t - 1] + H(Y[i, t - 1], X[i, t - 1], t / N) * dt[0] + I(Y[i, t - 1], X[i, t - 1], t / N) * dW2[i, t]

######## Plotting ########
plt.style.use("bmh")
if two and both:
    fig, axs = plt.subplots(2, figsize = (12, 10), dpi = 200, sharex = True)
    axs[1].plot(X.T)
    axs[1].set_title("X")
    axs[0].plot(Y.T)
    axs[0].set_title("Y")
elif two and not both:
    fig = plt.figure(figsize = (12, 8), dpi = 200)
    plt.plot(Y.T)
    plt.title("Y")
else:
    fig = plt.figure(figsize = (6, 4), dpi = 200)
    plt.ylim([-0.16, 0.16])
    plt.plot(X.T)
    #plt.title("a = 15")
ticks = np.round(np.linspace(0, N, 6), 2)
labels = np.round(np.linspace(0, 1, 6), 2)
plt.xticks(ticks, labels)
plt.show()
##########################

"""

* Heston Model *
two = True
F(x, t)    = 0.09 * (0.3 - x)
G(x, t)    = 0.05 * np.sqrt(x)
H(y, x, t) = 0.3 * y
I(y, x, t) = np.sqrt(x) * y

* Ornstein-Uhlenbeck (OU) *
* aka. Vasicek model for interest rates *
two = False
F(x, t) = 0.1 * (0.5 - x)
G(x, t) = 0.5

* Not quite Ornstein-Uhlenbeck *
* where mean is replaced by current group mean *
two = False

F(x, t) = 0.1 * (0.5 - x)
G(x, t) = 0.5

"""