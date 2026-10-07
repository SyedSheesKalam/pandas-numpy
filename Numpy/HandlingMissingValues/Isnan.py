import numpy as np
arr = np.array([1, 2, np.nan, 4, np.nan, 6])
print(np.isnan(arr))  # Output: [False False  True False  True False]
# Handling missing values by replacing NaN with a specific value (e.g., 0)
# we can't compare np.nan == np.nan directly
updated_arr = np.nan_to_num(arr, nan=3)
# The default replacement value is 0, but any value can be specified.
print(updated_arr)

# np.isinf() is used to check for infinite values in an array
arr2 = np.array([1, 2, np.inf, 4, -np.inf, 6])
print(np.isinf(arr2))  # Output: [False False  True False  True False]
updated_arr2 = np.nan_to_num(arr2, posinf=999, neginf=-999)
print(updated_arr2)  # Output: [   1.    2. 999.    4. -999.    6.] 