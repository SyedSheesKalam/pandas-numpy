import numpy as np
arr = np.array([100,200,300])
discount = 10
final_prices = arr - (arr * discount/100)
print(final_prices)  # Output: [ 90. 180. 270.]