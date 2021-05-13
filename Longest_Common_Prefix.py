# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new = sorted(strs)
        prefix = ""
        for x, y in zip(new[0], new[-1]):
            if x == y:
                prefix += x
            else:
                break
        return prefix