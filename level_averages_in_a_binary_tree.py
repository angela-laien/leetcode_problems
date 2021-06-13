Given a binary tree, populate an array to represent the averages of all of its levels.

from collections import deque
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
  result = []
  if root is None:
    return result
  queue = deque()
  queue.append(root)
  while queue:
    levelSize = len(queue)
    currentLevel = []
    levelSum = 0
    currentAverage = 0
    for i in range(levelSize):
      currentNode = queue.popleft()
      currentLevel.append(currentNode.val)
      levelSum = sum(currentLevel)
      currentAverage = levelSum/levelSize
      if currentNode.left is not None:
        queue.append(currentNode.left)
      if currentNode.right is not None:
        queue.append(currentNode.right)
    result.append(currentAverage)
  return result