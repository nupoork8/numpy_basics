# Aggregate functions = summarize data and typically return a single value

import numpy as np

array = np.array([[1, 2, 3,4,5], 
                [6,7,8,9,10]])
print(np.sum(array)) # Sum
print(np.mean(array)) # Average
print(np.max(array)) # Maximum
print(np.min(array))    # Minimum 
print(np.std(array))  # Standard Deviation
print(np.var(array))  # Variance    
print(np.median(array))  # Median # Median
print(np.percentile(array, 50))  # Percentile (50th percentile is the same as median)  # Percentile (50th percentile is the same as median)
print(np.argmin(array))  # Index of Minimum value