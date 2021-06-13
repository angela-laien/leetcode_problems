Problem Statement #

Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.

from collections import deque
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
  if not root:
    return 0
  min_depth = 0
  queue = deque()
  queue.append(root)
  while queue:
    min_depth += 1
    for i in range(len(queue)):
      currentNode = queue.popleft()
      if not currentNode.left and not currentNode.right:
        return min_depth
      if currentNode.left is not None:
        queue.append(currentNode.left)
      if currentNode.right is not None:
        queue.append(currentNode.right)