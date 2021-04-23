#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        used = [0]*len(nums)
        res = []

        def dfs(used, cur):
            if len(cur) == len(nums):
                res.append(cur)
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = 1              
                dfs(used, cur + [nums[i]])
                used[i] = 0
        
        dfs(used, [])
        return res
# time: O(n!*n) backtrack 调用次数O(n!). 我们需要将当前答案使用 O(n) 的时间复制到答案数组中
# space: O(n)
        
# @lc code=end

