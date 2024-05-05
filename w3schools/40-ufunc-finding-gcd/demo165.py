# W3Schools, NumPy Ufunc Finding LCM
import numpy as np

arr = np.array([20, 8, 32, 36, 16])

x = np.gcd.reduce(arr)

print(x)
