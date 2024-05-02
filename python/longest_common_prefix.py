"""leetcode link: https://leetcode.com/problems/longest-common-prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

#first solution
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_str = None
        
        for curr_str in strs:
            if min_str is None:
                min_str = curr_str
            if len(curr_str) < len(min_str):
                min_str = curr_str
        
        longest_commom_prefix = ""
        
        for i in range(len(min_str)):
            for s in strs:
                if s[i] != min_str[i]:
                  return longest_commom_prefix

            longest_commom_prefix += s[i]
        
        return longest_commom_prefix
    
#other solution
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest_commom_prefix = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return longest_commom_prefix
            longest_commom_prefix += s[i]
        
        return longest_commom_prefix

#other solution
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pref = strs[0]
        pref_len = len(pref)

        for s in strs[1:]:
            while pref != s[:pref_len]:
                pref_len -= 1
                pref = pref[:pref_len]

                if pref_len == 0:
                    return ""
        
        return pref
    