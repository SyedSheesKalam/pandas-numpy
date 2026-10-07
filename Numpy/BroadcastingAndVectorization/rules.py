import numpy as np
# Expanding single elements
arr = np.array([[1,2,3],[4,5,6]])
print(arr +10 )  

# Multi dimensional array broadcasting
arr2 = np.array([[1,2,3],[4,5,6]])
arr3 = np.array([[1,2,3]])
print(arr2 + arr3)  # Output: [[2 4 6]
#                              [5 7 9]]

# Incompatible shapes
arr4 = np.array([[1,2,3],[4,5,6]])
arr5 = np.array([[1,2],[3,4]])
print(arr4 + arr5)  # Output: ValueError: operands could not be