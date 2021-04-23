#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = [[]]
#         for i in nums:
#             for subres in res[:]:
#                 res.append(subres + [i])
#         return res
# # res = [[]]
# # res =  [[], [1]]
# # res =  [[], [1], [2], [1, 2]]
# # res =  [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
# # 因为append方法是原地址更新元素 所以要用切片获取指定位置元素. 循环中res[:]不更新。

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(s, cur, res):
            res.append(cur)
            for i in range(s, len(nums)):
                dfs(i+1, cur+[nums[i]], res)
            
        dfs(0, [], res)
        return res

        
 
# @lc code=end

