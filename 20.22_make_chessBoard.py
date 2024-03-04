# Now here we will draw a Chess Board with Python.

'''import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

dx, dy = 0.015, 0.05
x = np.arange(-4.0, 4.0, dx)
y = np.arange(-4.0, 4.0, dy)
X, Y = np.meshgrid(x, y)
extent = np.min(x), np.max(x), np.min(y), np.max(y)
cb1 = np.add.outer(range(8), range(8)) % 2
plt.imshow(cb1, cmap="binary_r", interpolation="nearest", extent=extent) # type: ignore

def chess(x, y):
    return(1- x/2 +x **5 + y **6) * np.exp(-(x**2 + y**2))
cb2 = chess(X, Y)
plt.imshow(cb2, alpha=0.7, interpolation="bilinear", extent=extent) # type: ignore
plt.title("Chess Board to show the Concept")
plt.show()'''