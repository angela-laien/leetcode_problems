# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            goal = target - v
            if goal in seen:
                return [seen[goal], i]
            seen[v] = i
        return []