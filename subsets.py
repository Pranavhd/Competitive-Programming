#https://leetcode.com/problems/subsets/description/

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size_sets = pow(2,len(nums))
        answer = []
        
        for counter in range(size_sets):
            temp_list = []
            for j in range(len(nums)):
                if counter & 1<<j:
                    temp_list.append(nums[j])
            answer.append(temp_list)
        
        return answer
