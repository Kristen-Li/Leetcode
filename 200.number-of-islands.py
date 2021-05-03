#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':  
                    ans += 1            
                    self.dfs(grid, i, j, m, n)
        return ans
    
    def dfs(self, grid: List[List[str]], i: int, j: int, m: int, n: int) -> None:
        if not 0 <=i< m or not 0 <= j<n or grid[i][j] == '0':
            return
        
        grid[i][j] = '0'
        self.dfs(grid, i+1, j, m, n)
        self.dfs(grid, i-1, j, m, n)
        self.dfs(grid, i, j+1, m, n)
        self.dfs(grid, i, j-1, m, n)
        
# @lc code=end

