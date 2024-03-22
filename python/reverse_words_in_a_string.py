"""leetcode link: https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
"""

##first solution
class Solution:
    def reverseWords(self, s: str) -> str:
        words_in_array = s.split(' ')
        new_string = ''
        for index in range(len(words_in_array) - 1, -1, -1):
            if words_in_array[index]:
                new_string += words_in_array[index] + ' '
        return new_string.strip()


##improved first solution
class Solution:
    def reverseWords(self, s: str) -> str:
        words_in_array = s.split()
        new_string = ''
        for index in range(len(words_in_array) - 1, -1, -1):
            new_string += words_in_array[index] + ' '
        return new_string.strip()


##other solution
class Solution:
    def reverseWords(self, s: str) -> str:
        array_s = s.split(' ')
        start = 0
        end = len(array_s) - 1
        while start < end:
            array_s[start], array_s[end] = array_s[end], array_s[start]

            start += 1
            end -= 1

        filtered_words = [word for word in array_s if word]

        return " ".join(filtered_words)
    

##better solution (using built-in reverse)
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        print(words)
        
        words.reverse()

        return ' '.join(words)