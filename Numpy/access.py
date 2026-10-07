import numpy as np
# Indexing and Slicing
# Indexing
arr = np.array([10, 20, 30, 40, 50])
print(arr[-1])  # Output: 30

# Slicing
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[1:5])  # Output: [20 30 40]   
print(arr[:2])  # Output: [10 20]
print(arr[::3])  # Output: [10 40] take 3 steps ahead
print(arr[::-1])  # Output: [60 50 40 30 20 10] reverse the array


# fancy indexing = selecting  multiple elements at once from an array

arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[[1, 3, 5]])  # Output: [20 40 60] select elements at index 1,3,5