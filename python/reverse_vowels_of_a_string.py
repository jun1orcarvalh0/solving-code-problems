"""leetcode link: https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""

##first solution
class Solution:
    def reverseVowels(self, s: str) -> str:
        str_to_list = [*s]
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels_in_string = []
        for index, word in enumerate(str_to_list):
            if word in vowels:
                vowels_in_string.insert(0, word)
        
        vowels_in_string_index = 0

        for index, word in enumerate(str_to_list):
            if word in vowels:
                str_to_list[index] = vowels_in_string[vowels_in_string_index]
                vowels_in_string_index += 1

        return ''.join(str_to_list)



##better solution
class Solution:
    def reverseVowels(self, s: str) -> str:
        word_to_list = list(s)
        start = 0
        end = len(word_to_list) - 1
        vowels = "aeiouAEIOU"

        while start < end:
            while start < end and word_to_list[start] not in vowels:
                start += 1
            while start < end and word_to_list[end] not in vowels:
                end -= 1
            
            word_to_list[start], word_to_list[end] = word_to_list[end], word_to_list[start]

            start += 1
            end -= 1
        
        return "".join(word_to_list)
