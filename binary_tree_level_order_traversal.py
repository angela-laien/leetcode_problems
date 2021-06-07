# Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.

# [[1],
# [2,3],
# [4,5,6,7]] 

# [[12],
# [7,1],
# [9,10,5]]  

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  result = []
  if root is None:
    return result
  queue = deque()
  queue.append(root)
  while queue:
    levelSize = len(queue)
    currentLevel = []
    for i in range(levelSize):
      currentNode = queue.popleft()
      currentLevel.append(currentNode.val)
      if currentNode.left is not None:
        queue.append(currentNode.left)
      if currentNode.right is not None:
        queue.append(currentNode.right)
    result.append(currentLevel)
  return result
