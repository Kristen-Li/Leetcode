#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        
        def dfs(s, cur, target):
            if target == 0 and len(cur) ==k:
                ans.append(cur[:])
                return
            elif len(cur)==k:
                return
            for i in range(s, 10):
                if target < i:
                    continue
                cur.append(i)
                dfs(i+1, cur, target-i)
                cur.pop()
        dfs(1,[], n)

        return ans

# @lc code=end

