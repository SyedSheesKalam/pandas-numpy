import numpy as np
"""
np.insert(array, index, value, axis=none) -> insert value at the specified index along the specified axis)
"""
arr = np.array([10, 20, 30, 40, 50])
# new_arr = np.insert(arr,2,100, axis=0)  # insert 100 at index 2 along axis 0
# print(new_arr)  # Output: [10 20 100 30 40 50]

# append() -> append value to the end of the array
new_arr2 = np.append(arr,60)  # append 60 to the end of the array
# print(new_arr2)  # Output: [10 20 30 40 50 60]

# concatenate() -> concatenate two or more arrays along the specified axis
arr2 =np.array([70, 80, 90,100,110])
new_arr3 = np.concatenate((arr,arr2), axis= 0)  # concatenate arr and arr2 along axis 0
print(new_arr3)  # Output: [10 20 30 40 50 70 80 90 100 110]

# Removing elements from an array
# np.delete(array, index, axis=none) -> delete value at the specified index along the specified axis
new_arr4 = np.delete(arr,2, axis= None)  # delete value at index 2 along axis none
print(new_arr4)  # Output: [10 20 40 50]
# another example but for 2D array
arr_2D = np.array([[1,2,3], [4,5,6]])
new_arr5 = np.delete(arr_2D,1, axis=0)  # delete row at index 1 along axis 0
print(new_arr5)  # Output: [[1 2 3]]