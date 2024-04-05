"""leetcode link: https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""
# first solution
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_average = None
        end = k - 1
        number_of_iterations = 0

        for i in range(len(nums)):
            total = 0
            start = i
            if number_of_iterations < (len(nums) - k) + 1:
                while start <= end:
                    total += nums[start]
                    start += 1
                average = total / k
                if (max_average is None or average > max_average):
                    max_average = average
                end += 1
                number_of_iterations += 1
        return max_average

# better solution
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr_sum = max_sum = sum(nums[:k])
        
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]
            
            if curr_sum > max_sum:
                max_sum = curr_sum

        return max_sum / k