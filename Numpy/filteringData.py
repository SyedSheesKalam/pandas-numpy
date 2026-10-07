import numpy as np
# filtering data in numpy arrays (boolean masking)
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[arr > 30])  # Output: [40 50 60] select elements greater than or equal to 30

#  x----x

# Array Shaping
# Reshaping arrays = changing the shape of an array without changing its data
arr = np.array([[1, 2, 3,4, 5, 6]])
reshaped_arr = arr.reshape(2, 3)  # Reshape to 2 rows and 3 columns
print(reshaped_arr)  # Output: [[1 2 3] [4 5 6]]
# reshape does not change the original array, it returns a new array with the specified shape

""" Flattening arrays = converting a multi-dimensional array into a 1D array
 .ravel() -> view
 .flatten() -> copy
 """
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d.ravel())  # Output: [1 2 3 4 5 6] returns a view of the original array
print(arr_2d.flatten())  # Output: [1 2 3 4 5 6] returns a copy of the original array
