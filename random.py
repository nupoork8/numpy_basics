import numpy as np

# numpy generate random numbers

# rng = np.random.default_rng(seed=1)
# print(rng.integers(low = 1,high =7,size=(3,2)))

# np.random.seed(seed=1)
# print(np.random.uniform(low=-1,high=1,size=(3,2)))

#shuffle array
rng = np.random.default_rng()
# array = np.array([1,2,3,4,5])
# print(array)

fruits = np.array(['apple','banana','cherry','date','elderberry'])
fruit = rng.choice(fruits,size=3)
print(fruits)