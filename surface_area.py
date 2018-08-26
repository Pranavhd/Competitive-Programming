#https://leetcode.com/contest/weekly-contest-99/problems/surface-area-of-3d-shapes/

class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area = 0
        row_end = len(grid)
        col_end = len(grid[0])
        for row_ind,row in enumerate(grid):
            for col_ind,col in enumerate(row):
                if grid[row_ind][col_ind]:
                    area += 2*(1+2*grid[row_ind][col_ind])
                    if row_ind>0 and grid[row_ind-1][col_ind]>0:
                        mini = min(grid[row_ind][col_ind],grid[row_ind-1][col_ind])
                        area -= 2*mini
                    if col_ind>0 and grid[row_ind][col_ind-1]>0:
                        mini = min(grid[row_ind][col_ind],grid[row_ind][col_ind-1])
                        area -= 2*mini
        return area         
