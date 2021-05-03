# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  window_start = 0
  window_sum = 0
  max_sum = 0

  for window_end in range(len(arr)):
    window_sum += arr[window_end]
    if window_end >= k-1:
      max_sum = max(max_sum, window_sum)
      window_sum -= arr[window_start]
      window_start += 1
  return max_sum
