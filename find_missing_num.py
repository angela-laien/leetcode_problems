# We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

# Input: [4, 0, 3, 1]
# Output: 2

# Input: [8, 3, 5, 2, 4, 6, 0, 1]
# Output: 7

def find_missing_number(nums):
  i = 0
  while i < len(nums):
    j = nums[i]
    if j < len(nums) and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    else: 
      i += 1
    
  for i in range(len(nums)):
    if nums[i] != i:
      return i
    else:
      i += 1
  return -1