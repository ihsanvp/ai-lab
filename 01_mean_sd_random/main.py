import numpy as np
import random
from math import sqrt

data = []

for i in range(10):
    data.append(random.randint(0, 100))

mean = np.mean(data)
sd = sqrt(np.var(data))

print("data =", data)
print("mean =", mean)
print("standard deviation =", sd)
