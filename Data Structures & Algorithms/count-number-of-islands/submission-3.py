class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        num_isl = 0

        def bfs(u, v):
                q = deque()
                q.append((u, v))
                grid[u][v] = "0"

                while q:
                    x, y = q.popleft()
                    for dx, dy in directions:
                        nx = x + dx
                        ny = y + dy
                        if nx >= 0 and nx < n and ny >= 0 and ny < m and grid[nx][ny] == "1":
                            q.append((nx, ny))
                            grid[nx][ny] = "0";
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    num_isl += 1
                    bfs(i, j)
        return num_isl
                    