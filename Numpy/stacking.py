import numpy as np
"""
vstack() -> stack arrays vertically (row wise)
hstack() -> stack arrays horizontally (column wise)
"""
arr1 = np.array([12,23,34])
arr2 = np.array([45,56,67])
print(np.vstack((arr1,arr2)))  # Output: [[12 23 34]
                                        # [45 56 67]]

print((np.hstack((arr1,arr2))))  # Output: [12 23 34 45 56 67]
