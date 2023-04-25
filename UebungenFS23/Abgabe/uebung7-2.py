import matplotlib.pyplot as plt
from math import sin, pi
import numpy as np
import random

x = np.linspace(-5,5,1000)
y = np.linspace(-5,5,1000)

def f(a,b):
    return np.exp(-a**2)*np.sin(b)

X, Y = np.meshgrid(x, y)
Z = f(X,Y)

plt.pcolormesh(X, Y, Z)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('equal')
plt.show()
