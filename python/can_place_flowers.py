"""leetcode link: https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""


##first solution 113 / 129 testcases passed
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        number_of_ones = 0
        number_of_zeros = 0
        
        for plot in flowerbed:
            if plot == 0:
                number_of_zeros += 1
            else:
                number_of_ones += 1

        if (len(flowerbed) % 2) == 0:
            if number_of_ones + n == number_of_zeros - n:
                return True
            else:
                return False
        else:
            if number_of_ones + n == (number_of_zeros - n) + 1:
                return True
            else:
                return False

##better solution (all testcases passed)
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0: return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == (len(flowerbed) - 1) or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False