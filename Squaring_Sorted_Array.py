# Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]

def make_squares(arr):
  first_i = 0
  last_i = len(arr)-1
  last_squares_i = len(arr)-1
  squares = [0 for i in range(len(arr))]
  while first_i < last_i:
    start = arr[first_i] * arr[first_i]
    end = arr[last_i] * arr[last_i]
    if start > end:
      squares[last_squares_i] = start
      first_i += 1
    else:
      squares[last_squares_i] = end
      last_i -= 1
    last_squares_i -= 1
  
  return squares