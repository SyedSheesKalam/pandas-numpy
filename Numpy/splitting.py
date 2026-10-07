import numpy as np
"""
np.split() is use for equal splitting of an array into multiple sub-arrays along the specified axis

np.hsplit() is use for splitting an array into multiple sub-arrays horizontally (column wise)

np.vsplit() is use for splitting an array into multiple sub-arrays vertically (row wise)

np.array_split() is use for splitting an array into multiple sub-arrays of unequal size along the specified axis
"""
arr = np.array([[1,2,3,4,5,6,7,8,9,10,11,12]])
arr2 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(np.split(arr, 2,axis = 1))  # Output: [array([[1, 2, 3, 4, 5, 6]]), array([[ 7,  8,  9, 10, 11, 12]])]
print(np.hsplit(arr, 2))  # Output: [array([[1, 2, 3, 4, 5, 6]]), array([[ 7,  8,  9, 10, 11, 12]])]

print(np.hsplit(arr2, 2))  # Output: [array([[1, 2, 3, 4, 5, 6]]), array([[ 7,  8,  9, 10, 11, 12]])]