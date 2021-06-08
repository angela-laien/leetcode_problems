# Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level comes first. You should populate the values of all nodes in each level from left to right in separate sub-arrays.

#  [[4,5,6,7],
#  [2,3],
#  [1]]  

#  [[9,10,5],
#  [7,1],
#  [12]] 

from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = deque()
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
    result.appendleft(currentLevel)
  return result