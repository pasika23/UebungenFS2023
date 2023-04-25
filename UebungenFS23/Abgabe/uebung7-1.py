import matplotlib.pyplot as plt
from math import sin, pi
import numpy as np
import random

x = np.random.random(1000)
x = x*200-100
y = np.random.random(1000)
y = y*200-100

colors = [random.random() for i in range(1000)]

plt.scatter(x,y, c=colors)
plt.grid('true')
plt.show()