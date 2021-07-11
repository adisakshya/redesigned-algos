"""
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.
Return the array ans.

Source - https://leetcode.com/problems/concatenation-of-array/
"""

"""
Time Complexity - O(n)
    - 'n' is length of concatenated list
Space Complexity - O(1)
"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
