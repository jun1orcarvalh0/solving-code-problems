"""leetcode link: https://leetcode.com/problems/is-subsequence/

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""

##first solution
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        result_string = ''
        index_1 = 0
        index_2 = 0
        while index_1 < len(t) and index_2 < len(s):
            if s[index_2] == t[index_1]:
                result_string += t[index_1]
                index_2 += 1
            
            index_1 += 1

        if result_string == s:
            return True