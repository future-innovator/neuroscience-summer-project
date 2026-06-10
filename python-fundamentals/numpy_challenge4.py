import numpy as np

nums = np.array([5, 10, 15, 20, 25])

print(f"The first element of nums is: {nums.item(0)}")

print(f"The third element of nums is: {nums[2]}")

print(f"The last element of nums is: {nums[-1]}")

#Python allows the index -1 because it knows the length of an array and can use it to retrieve the last element of an array. This solves the problem of having to determine the exact length of an array to reference the last element
