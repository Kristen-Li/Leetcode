#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         if not digits:
#             return[]
        
#         d = ["","","abc","def","ghi","jkl","mno","pqrs","tuv", "wxyz"]
#         res = []
#         def dfs(tmp,idx):
#             if len(tmp) == len(digits):
#                 res.append(tmp)
#                 return
#             letters = d[ord(digits[idx]) - ord('0')]
#             for letter in letters:
#                 dfs(tmp+letter,idx+1)
#         dfs("",0)
#         return res

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return[]
        
        d = ["","","abc","def","ghi","jkl","mno","pqrs","tuv", "wxyz"]
        res = []
        tmp = []
        def dfs(idx):
            if len(tmp) == len(digits):
                res.append(''.join(tmp))
                return
            letters = d[ord(digits[idx]) - ord('0')] # convert "2" to 2
            for letter in letters:
                tmp.append(letter)
                dfs(idx+1)
                tmp.pop()
        dfs(0)
        return res


# 时间复杂度：O(3^m * 4^n), 其中 m是输入中对应 3 个字母的数字个数，n 是输入中对应 4 个字母的数字个数

# 空间复杂度：O(m+n)，m+n是输入数字的总个数。除了返回值以外，
# 空间复杂度主要取决于哈希表以及回溯过程中的递归调用层数，哈希表的大小与输入无关，可以看成常数，递归调用层数最大为 m+n


        
# @lc code=end

