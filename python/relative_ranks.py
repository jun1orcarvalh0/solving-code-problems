"""leetcode link: https://leetcode.com/problems/relative-ranks

You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

 

Example 1:

Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
Example 2:

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].
"""
# first solution
class Solution:
    def find_relative_ranks(self, score: list[int]) -> list[str]:
        list_score = {}

        for index, athlete_score in enumerate(score):
            list_score[index] = athlete_score
        
        list_score = sorted(list_score.items(), key=lambda x: x[1], reverse=True)

        for index, athelete in enumerate(list_score):
            if index == 0:
                score[athelete[0]] = "Gold Medal"
            elif index == 1:
                score[athelete[0]] = "Silver Medal"
            elif index == 2:
                score[athelete[0]] = "Bronze Medal"
            else:
                score[athelete[0]] = str(index + 1)
        
        return score
    
# other solution (better)
class Solution:
    def find_relative_ranks(self, score: list[int]) -> list[str]:
        sorted_score = sorted(score, reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rank_mapping = {score: medals[i] if i < 3 else str(i + 1) for i, score in enumerate(sorted_score)}
        return [rank_mapping[athlete_score] for athlete_score in score]