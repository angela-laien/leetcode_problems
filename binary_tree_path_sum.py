Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def has_path(root, sum):
  if root is None:
    return False
  
  if root.val == sum and root.left is None and root.right is None:
    return True

  return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)