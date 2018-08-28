#https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/

class Solution:
    def findMaximumXOR(self,nums):
        maxi = 0
        mask = 0
        for i in range(32)[::-1]:
            mask = mask | (1<<i)
            my_set = set()
            for num in nums:
                my_set.add(num&mask)
            tmp = maxi | (1<<i)
            for ele in my_set:
                if ele^tmp in my_set:
                    maxi = tmp
                    break
        return maxi

# def findMaximumXOR(nums):
#     maxi = 0
#     mask = 0
#     for i in range(6)[::-1]:
#         mask = mask | (1<<i)
#         my_set = set()
#         for num in nums:
#             my_set.add(num&mask)
#         for ele in my_set:
#             print(ele,bin(ele))
        
#         tmp = maxi | (1<<i)
#         print("temp is ",tmp,bin(tmp))
#         for pre in my_set:
#             if pre^tmp in my_set:
#                 maxi = tmp
#                 print("this also exists ",pre^tmp)
#                 print("updated maxi = ",maxi)
#                 break
#         print("----------------")
#     return maxi