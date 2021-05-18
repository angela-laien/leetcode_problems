# Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]

def make_squares(arr):
  squares = [0 for i in range(len(arr))]
  first = 0
  last = len(arr)-1
  highestSquareIdx = len(arr)-1
  while first <= last:
    left = arr[first]*arr[first]
    right = arr[last]*arr[last]
    if left > right:
      squares[highestSquareIdx] = left
      first += 1
    else:
      squares[highestSquareIdx] = right
      last -= 1
    highestSquareIdx -= 1
  return squares