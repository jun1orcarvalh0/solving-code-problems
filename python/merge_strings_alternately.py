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


#first solution
def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedWords = ''
        if len(word1) > len(word2):
            for index, word in enumerate(word1):
                try:
                    mergedWords += word + word2[index]
                except:
                    mergedWords += word
        else:
            for index, word in enumerate(word2):
                try:
                    mergedWords += word1[index] + word
                except:
                    mergedWords += word
        return mergedWords

##better solution
def mergeAlternately(self, word1: str, word2: str) -> str:
    mergedWords = []
    i = 0
    while i < len(word1) or i < len(word2):
        if i < len(word1):
            mergedWords.append(word1[i])
        if i < len(word2):
            mergedWords.append(word2[i])
        i += 1
    return ''.join(mergedWords)