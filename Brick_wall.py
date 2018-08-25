#https://leetcode.com/problems/brick-wall/description/

class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        myd = {}
        myd[0]=0
        
        for row in wall:
            su = 0
            for ele in row[:-1]:
                su += ele
                myd[su] = myd.get(su,0)+1
             
        ind,val = max(myd.items(),key=operator.itemgetter(1))
        if ind==0:
            return len(wall)
        #print(myd)
        #print(ind,val)
        return len(wall)-val
