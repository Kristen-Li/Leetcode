#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        step1: start from the board to use dfs
        step2: def dfs to mark the o's  as # connected to the boarderline
        step 3: flip the # to O, and flip the O to X
        """
        # m rows and n columns
        if not board:
            return

        m = len(board)
        n = len(board[0])
        dir = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(x, y):

            if not 0<= x < m or not 0<=y<n   or board[x][y] != 'O':                
                return

            board[x][y] = '#'
            for (i, j) in dir:
                dfs(x+i, y+j)

        # # use dfs at the boarderline
        # for j in range(n):
            
        #     dfs(0, j)
        #     dfs(m-1, j)

        # for i in range(m):
        #     dfs(i, 0)
        #     dfs(i, n-1)

        for i in range(m):
            for j in range(n):
                if i == 0  or i == m-1 or j == 0 or j == n -1 and board[i][j] == 'O':
                    dfs(i, j)
        
        # flip
        for i in range(m):
            for j in range(n):
                if board[i][j] == "#":
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        
# @lc code=end

