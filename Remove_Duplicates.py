# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

def remove_duplicates(arr):
    window_start = 1
    count = 1
    while window_start <= len(arr)-1:
        if arr[window_start-1] != arr[window_start]:
            count += 1
        window_start += 1
    return count