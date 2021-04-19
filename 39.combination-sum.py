#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(start, path, target):
            if target < 0:
                return
            if target == 0:
                ans.append(path[:])
                return
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                dfs(i, path, target-candidates[i])
                path.pop()
        dfs(0, [], target)
        return ans
# @lc code=end

