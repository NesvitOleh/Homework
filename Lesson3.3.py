nums = [1, 2, 3, 4, 5, 6]
middle = len(nums) // 2
result = [nums [:middle], nums[middle:]]
print(result)

nums = [1, 2, 3]
middle = len(nums) -1
result = [nums [: middle], nums[middle:]]
print(result)

nums = [1, 2, 3, 4, 5]
middle = len(nums) - 2
result = [nums [:middle], nums [middle:]]
print(result)

nums = [1]
middle = len(nums) + 1
result = [nums [:middle], nums [middle:]]
print(result)

nums = []
middle = len(nums)
result = [nums [:middle], nums [middle:]]
print(result)
