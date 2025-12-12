import numpy as np

#python code
# my_list = [1,2,3,4]
# my_list = my_list * 2
# print(my_list)

#numpy code
# array = array * 2
# print(array)
# print(type(array))

#multi dimensional array
# import numpy as np

# A proper 3D array: shape (5, 2, 3) - 5 blocks, 2 rows each, 3 columns each
array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '_']]])
# print(array.ndim)      # 3 (three dimensions)
# print(array.shape)     # (5, 2, 3) - 5 blocks, 2 rows, 3 columns

# Chain indexing examples:
# print(array[1][1][1])  # 'N' - first block, first row, first column
# print(array[4][0][0])  # 'Y' - fifth block, first row, first column
# print(array[2][1][2])  # 'R' - third block, second row, third column

word = array[0,0,0] + array[2,0,0] + array[2,0,0]
print(word)
