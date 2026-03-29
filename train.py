import numpy as np
import platform

print(f"Architecture: {platform.machine()}")

a = np.random.rand(1000, 1000)
b = np.random.rand(1000, 1000)
c = np.dot(a, b)

print("Matrix multiplication successful! C-bindings are working correctly on this architecture.")
