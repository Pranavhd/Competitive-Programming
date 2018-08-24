#https://leetcode.com/problems/permutations/description/

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        temp = []
        ans = []
        def back(ans,temp, nums):
            if len(temp)==len(nums):
                another = []
                another += temp
                ans.append(another)
            else:
                for ele in nums:
                    if ele in temp:
                        continue
                    temp.append(ele)
                    back(ans,temp,nums)
                    temp.remove(ele)
        
        back(ans,temp,nums)
        return ans