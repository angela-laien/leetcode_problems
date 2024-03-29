Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:

Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]
Example 2:

Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3] 

def find_subsets(nums):
  startIndex = 0
  endIndex = 0
  nums.sort()
  subsets = []
  subsets.append([])
  for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i-1]:
      startIndex = endIndex + 1
    endIndex = len(subsets)-1
    for j in range(startIndex, endIndex+1):
      newset = list(subsets[j])
      newset.append(nums[i])
      subsets.append(newset)
  return subsets
