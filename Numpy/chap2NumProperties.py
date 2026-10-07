# # checking the properties of a numpy array
import numpy as np
# # SHAPE
# array_2d = np.array([[1, 2, 3,], [4, 5, 6]])
# print(array_2d.shape) 
# # Size
# print(array_2d.size)
# # Number of dimensions
# print(array_2d.ndim)

# # data type
# print(array_2d.dtype)

# changing the data type of an array
# arr = np.array([1.1, 2.2, 3.3, 4.8, 5.9])
# print(arr.dtype)
# print(arr)
# int_arr = arr.astype(int)
# print('\n', int_arr.dtype)    
# print(int_arr)

# Mathematical operations on numpy arrays
arr = np.array([10,20,30])
print(arr+2)
print(arr-2)
print(arr*2)
print(arr/2)
print(arr%2)
print(arr**2)
print(arr//2)