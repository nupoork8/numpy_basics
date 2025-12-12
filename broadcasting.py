# Brodcasting allows numpy Numpy to perform operations on arrays
# with diffrent shapes by virtually expanding dimensions
# so they match the larger array's shape

# the dimensions have the same size
# or
# one of the dimensions has a size of 1


import numpy as np

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1],[2],[3],[4]])

print(array1.shape)  # Output: (1, 4)
print(array2.shape)  # Output: (4, 1)

print(array1 * array2)
