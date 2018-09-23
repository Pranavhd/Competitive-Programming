#https://leetcode.com/problems/shopping-offers/description/

class Solution:
    def __init__(self):
        self.memo = {}
        
    def shop(self,price,special,needs):
        if str(needs) in self.memo:
            return self.memo[str(needs)]
        res = 0
        
        for i in range(len(needs)):
            res += int(needs[i])*int(price[i])
        for sp in special:
            success = 1
            new_needs = []
            for j in range(len(needs)):
                if sp[j]>needs[j]:
                    success = 0
                    break
                new_needs.append(int(needs[j]-sp[j]))
            if success==1:
                res = min(res,sp[len(needs)]+self.shop(price,special,new_needs))
                self.memo[str(needs)] = res
        return res
            
    
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        return self.shop(price,special,needs)