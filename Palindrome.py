##https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        h = len(s)-1
        
        while l<h:
            if s[l]!=s[h]:
                one = s[l:h]
                two = s[l+1:h+1]
                return one==one[::-1] or two==two[::-1]
            l+=1
            h-=1
        return True
