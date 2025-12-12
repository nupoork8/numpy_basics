#scalar arithmetic operations

import numpy as np
# array = np.array([1,2,3])
# print(array + 1) 
# print(array - 2) 
# print(array * 3)
# print(array / 4)  
# print(array ** 5)

#vectorized math functions

# radii = np.array([1,2,3])
# print(np.sqrt(array))
# print(np.floor(array))
# print(np.ceil(array))
# print(np.round(array))

# print(np.pi * radii **2) # area of circles with given radii

#element wise addition, subtraction, multiplication, division

# array1 = np.array([1,2,3])
# array2 = np.array([4,5,6])

# print(array1 + array2)
# print(array1 - array2)
# print(array1 * array2)  
# print(array1 / array2)
# print(array1 ** array2)

#comparison operations
scores = np.array([85,90,78,55,92,88,100])
# print(scores > 90)
# print(scores == 100)
# print(scores < 90)
# print(scores >= 88)
# print(scores != 78)     
# print((scores >= 85) & (scores <= 90))  # between 85 and 90 inclusive
# print((scores < 80) | (scores == 100))   # less than 80 or equal to 100     
scores[scores < 60] = 0
print(scores)

#logical operations