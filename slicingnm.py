#slicing using numpy

import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

# subscript array [start:end:step]

print(array[0:2,2:]) # first 2 rows, last 2 columns
print(array[:,::2])  # all rows, every second column
print(array[1::2,1::2]) # every second row starting from index 1, every second column starting from index 1
print(array[-2:, -3:]) # last 2 rows, last 3 columns    
#last 2 rows, first 2 columns 
print(array[-2:, :2])
print(array[2:,2:])
