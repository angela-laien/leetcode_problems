Given a set with distinct elements, find all of its distinct subsets.

Example 1:

Input: [1, 3]
Output: [], [1], [3], [1,3]
Example 2:

Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]

def find_subsets(nums):
  subsets = []
  subsets.append([])
  for current in nums:
    for i in range(len(subsets)):
      newset = list(subsets[i])
      newset.append(current)
      subsets.append(newset)
  return subsets