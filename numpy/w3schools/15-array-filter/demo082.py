# W3Schools, NumPy Array Filter
import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = []

for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
