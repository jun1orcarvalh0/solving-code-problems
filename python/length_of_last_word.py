"""leetcode link: https://leetcode.com/problems/length-of-last-word/

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""
# first solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])

# other solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length_of_last_word = 0
        
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                if length_of_last_word > 0:
                    return length_of_last_word
                else:
                    continue
            length_of_last_word += 1
        return length_of_last_word