import numpy as np

nums = np.array([5, 10, 15, 20, 25])

print(nums)

# this is a numpy array
print(f"Of type {type(nums)}")

# numpy arrays are faster and more memory efficient than python lists
nums_list = [5, 10, 15, 20, 25]
print(f"NumPy array * 2: {nums * 2}")
print(f"Python list * 2: {nums_list * 2}")
# numpy arrays also allow vectorized operations
