"""leetcode link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
"""
# first solution (99 / 106 testcases passed)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_number_of_vowels = 0
        start = 0
        end = k - 1

        def number_of_vowels(str):
            num_of_vowels = 0
            for letter in str:
                if letter in ['a', 'e', 'i', 'o', 'u']:
                    num_of_vowels += 1
            return num_of_vowels

        while end < len(s):
            num_of_vowels = number_of_vowels(s[start:end+1])
            max_number_of_vowels = max(max_number_of_vowels, num_of_vowels)
            end += 1
            start +=1
        
        return max_number_of_vowels
    
# other solution (better)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_number_of_vowels = 0
        current_vowel_count = 0

        for i in range(k):
            if s[i] in vowels:
                current_vowel_count += 1
        
        max_number_of_vowels = current_vowel_count

        for i in range(k, len(s)):
            if s[i] in vowels:
                current_vowel_count += 1
            if s[i - k] in vowels:
                current_vowel_count -= 1
            max_number_of_vowels = max(max_number_of_vowels, current_vowel_count)
        
        return max_number_of_vowels