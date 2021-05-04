#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        diag1 = set()
        diag2 = set()
        usedCols = set()
        # Notice here. helper fun need not to be nested. 
        self.ans = 0 
        def helper( n, diag1, diag2, usedCols, row):
            if row == n:
                self.ans += 1
                return 
            
            
            for col in range(n):
                if row + col in diag1 or row - col in diag2 or col in usedCols:
                    continue
                    
                diag1.add(row + col)
                diag2.add(row - col)
                usedCols.add(col)
                
                helper(n, diag1, diag2, usedCols, row + 1)
            
                diag1.remove(row + col)
                diag2.remove(row - col)
                usedCols.remove(col)

        helper(n, diag1, diag2, usedCols, 0)
        return self.ans
        
# @lc code=end

