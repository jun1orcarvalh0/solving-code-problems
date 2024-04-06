"""leetcode link: https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""
# first solution
class Solution:
    def moveZeroes(self, nums: list) -> None:
        compair_idx = 0
        
        for i in range(len(nums)):
            if nums[compair_idx] == 0 and nums[i] != 0:
                nums[compair_idx], nums[i] = nums[i], nums[compair_idx]
                
            if nums[compair_idx] != 0:
                compair_idx += 1

# better solution
class Solution:
    def moveZeroes(self, nums: list) -> None:
        compair_idx = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[compair_idx], nums[i] = nums[i], nums[compair_idx]
                compair_idx += 1