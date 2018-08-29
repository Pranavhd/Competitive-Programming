#https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join([char*val for char,val in collections.Counter(s).most_common()])