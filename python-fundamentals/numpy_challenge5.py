import numpy as np

nums = np.array([5, 10, 15, 20, 25])

print(nums[1:4])

print(nums[2:5])

#Leaving the first part blank means that the array will start from the first element
print(nums[:3])

#Leaving the second part blank means that the array will go to the last element
print(nums[2:])

#The line below prints everything except the first and last element of an array
print(nums[1:-1])
