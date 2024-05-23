"""leetcode link: https://leetcode.com/problems/roman-to-integer/description/
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

# first solution
class Solution:
    def romanToInt(self, s: str) -> int:
        int_value = 0
        
        
        def i_to_int_value(index):
            if index != len(s) - 1 and (s[index + 1] == 'V' or s[index + 1] == 'X'):
                return -1
            else:
                return +1
        
        def x_to_int_value(index):
            if index != len(s) - 1 and (s[index + 1] == 'L' or s[index + 1] == 'C'):
                return -10
            else:
                return +10
        
        def c_to_int_value(index):
            if index != len(s) - 1 and (s[index + 1] == 'D' or s[index + 1] == 'M'):
                return -100
            else:
                return +100

        for i in range(len(s)):
            if s[i] == 'M':
                int_value += 1000
            elif s[i] == 'D':
                int_value += 500
            elif s[i] == 'C':
                int_value += c_to_int_value(i)
            elif s[i] == 'L':
                int_value += 50
            elif s[i] == 'X':
                int_value += x_to_int_value(i)
            elif s[i] == 'V':
                int_value += 5
            else:
                int_value += i_to_int_value(i)
            
        return int_value

#other solution
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        int_value = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                int_value -= roman[s[i]]
            else:
                int_value += roman[s[i]]
        
        return int_value