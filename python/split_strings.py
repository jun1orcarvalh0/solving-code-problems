"""codewars link: https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python

Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""


#solution
def solution(s):
    s_array = [word for word in s]
    list_of_pairs = []
    for i, word in enumerate(s_array):
        if i % 2 == 0:
            try:
                list_of_pairs.append(word + s_array[i+1])
            except IndexError:
                list_of_pairs.append(word + '_')
    return list_of_pairs