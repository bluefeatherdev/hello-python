# W3Schools, NumPy Array Filter
import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
