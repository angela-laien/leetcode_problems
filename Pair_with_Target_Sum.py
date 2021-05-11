# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

def pair_with_targetsum(arr, target_sum):
  # TODO: Write your code here
  window_start = 0
  window_end = len(arr)-1
  while (window_start < window_end):
    if arr[window_start] + arr[window_end] == target_sum:
      return [window_start, window_end]
    elif arr[window_start] + arr[window_end] > target_sum:
      window_end -= 1
    else:
      window_start += 1
  return [-1, -1]