"""leetcode link: https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""

##first solution O(n2)
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        list_of_products = []
        for index in range(nums):
            start = 0
            result = None
            while start < len(nums):
                if result == None and start != index:
                    result = nums[start]
                elif start != index:
                    result = result * nums[start]
                
                start += 1
                    
            list_of_products.append(result)
        return list_of_products
    
##better solution O(n)
class Solution:
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    result_array = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        result_array[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        result_array[i] *= postfix
        postfix *= nums[i]
    
    return result_array