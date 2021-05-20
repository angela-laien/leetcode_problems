# Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

# If the total number of nodes in the LinkedList is even, return the second middle node.

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
# Output: 3

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
# Output: 4

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
# Output: 4

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def find_middle_of_linked_list(head):
  # TODO: Write your code here
  fast = head
  slow = head
  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
  return slow