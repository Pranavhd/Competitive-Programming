#https://leetcode.com/problems/find-duplicate-file-in-system/description/

class Solution:
    def findDuplicate(self,paths):
        my_dict = {}
        for path in paths:
            temp = path.split()
            for ele in temp[1:]:
                for index, char in enumerate(ele):
                    if char=='(':
                        startpos = index
                    if char == ')':
                        endpos = index
                if ele[startpos+1:endpos] in my_dict:
                    my_dict[ele[startpos+1:endpos]].append(temp[0] + "/" + ele[:startpos])
                else:
                    my_dict[ele[startpos+1:endpos]] = []
                    my_dict[ele[startpos+1:endpos]].append(temp[0] + "/" + ele[:startpos])
        ans = []
        for key in my_dict:
            temp = []
            if len(my_dict[key])>1:
                for values in my_dict[key]:
                    temp.append(values)
                ans.append(temp)

        return ans
