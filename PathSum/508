```
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.memo = {}
        def dfs(node):
            l = dfs(node.left) if node.left else 0
            r = dfs(node.right) if node.right else 0
            s = node.val + l + r
            self.memo[s] = self.memo.get(s, 0) + 1
            return s
        if not root:
            return []
        dfs(root)
        maxv = max(self.memo.values())
        res = filter(lambda x : self.memo[x] == maxv, self.memo)
        return res
  ```
