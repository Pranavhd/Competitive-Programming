#https://leetcode.com/contest/weekly-contest-99/problems/groups-of-special-equivalent-strings/

from collections import Counter

class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        final_A = []
        for word in A:
            even_list = []
            odd_list = []
            i = 0
            while i<len(word):
                even_list.append(word[i])
                i+=2
            i = 1
            while i<len(word):
                odd_list.append(word[i])
                i+=2
            even_list.sort()
            odd_list.sort()
            temp = ''.join(even_list)+''.join(odd_list)
            final_A.append(temp)
        
        c = Counter(final_A)
        return len(c)