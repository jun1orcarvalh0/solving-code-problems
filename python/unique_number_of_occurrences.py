import collections
"""leetcode link: https://leetcode.com/problems/unique-number-of-occurrences/

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""
# first solution
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        number_occurrences = {}
        for number in arr:
            if number in number_occurrences:
                number_occurrences[number] += 1
            else:
                number_occurrences[number] = 1
        
        if len(set(number_occurrences.values())) == len(number_occurrences.values()):
               return True
               
        return False

# other solution (my first solution is better, in my opinion)
class Solution():
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        c = collections.Counter(arr)
        return len(c) == len(set(c.values()))