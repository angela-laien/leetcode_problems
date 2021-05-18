# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Input: s = "()[]{}"
# Output: true

# Input: s = "(]"
# Output: false

# Input: s = "([)]"
# Output: false

# Input: s = "{[]}"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        open_par = set(["(", "{", "["])
        for i in s:
            if i in open_par:
               stack.append(i)
            elif stack and i == brackets[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []