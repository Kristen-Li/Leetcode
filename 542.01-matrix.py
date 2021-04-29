#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        M, N = len(matrix), len(matrix[0])
        queue = collections.deque()
        visited = [[0] * N for _ in range(M)]
        dist = [[0] * N for _ in range(M)]
        
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = 1
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            size = len(queue)
            for i in range(size):
                x, y = queue.popleft()  
                for dx, dy in dirs:
                    newx, newy = x + dx, y + dy
                    if newx >=0  and newx < M and newy >= 0 and newy < N and visited[newx][newy] == 0:
                        dist[newx][newy] = dist[x][y] + 1
                        queue.append((newx, newy))
                        visited[newx][newy] = 1
        return dist
# @lc code=end

