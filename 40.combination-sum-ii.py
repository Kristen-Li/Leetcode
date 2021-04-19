#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def  dfs(s, cur, target):  
            if target < 0:
                return                   
            if target == 0:
                ans.append(cur[:])
                return
            for i in range(s, len(candidates)):  
                           
                if i > s and candidates[i] == candidates[i-1]:
                    continue     
                cur.append(candidates[i])
                dfs(i+1, cur, target - candidates[i])
                cur.pop()
        dfs(0, [], target)
        return ans
# 每得到一个满足要求的组合，需要O(n) 的时间将其放入答案中，因此我们将 O(2^n)
#  ) 与 O(n) 相乘，即可估算出一个宽松的时间复杂度上界
# 空间复杂度：O(n)

        
# @lc code=end

