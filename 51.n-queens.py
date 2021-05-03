#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for i in range(n)] for j in range(n)]
        cols = [0]*n
        diag1 = [0]*(2*n-1)
        diag2 = [0]*(2*n-1)
        ans = []

        
        def updateBoard( r, c, n, isPut):
            cols[c], diag1[r+c], diag2[r-c + n-1] = isPut, isPut, isPut
            board[r][c] = 'Q' if isPut else '.'
    
        
        def nqueens(ans, r, n):        
            if r == n:
                ans.append([''.join(lst) for lst in board]) # notice here
                return

    
            for c in range(n):
                if cols[c] or diag1[r+c] or diag2[r-c + n -1]: continue # these positions cannot have 'Q'
                updateBoard(r, c, n, True)
                nqueens(ans, r+1, n)
                updateBoard(r, c, n, False)
                

        nqueens(ans,0, n)
        return ans
        
# @lc code=end

