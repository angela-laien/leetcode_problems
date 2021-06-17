Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the node that appears right after the given node in the level order traversal.

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
  if root is None:
    return None

  queue = deque()
  queue.append(root)
  while queue:
    currentNode = queue.popleft()
    if currentNode.left:
      queue.append(currentNode.left)
    if currentNode.right:
      queue.append(currentNode.right)

    if currentNode.val == key:
      break
  return None
