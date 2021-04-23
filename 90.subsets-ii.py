#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(s, cur, res):
            res.append(cur)
            for i in range(s, len(nums)):
                if i > s and nums[i] == nums[i-1]:
                    continue
                dfs(i+1, cur+[nums[i]], res)

        dfs(0, [], res)
        return res
#  remember nums.sort   
# Time : O(n*2^n)
# Space: O(n)
# @lc code=end

