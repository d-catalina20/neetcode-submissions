class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    grid[i][j] = -1
                elif grid[i][j] == 1:
                    grid[i][j] = -2
                else:
                    grid[i][j] = -3
                    q.append((i, j, 0))
        dist = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        total_min = 0;
        while q:
            x, y, minute = q.popleft()
            for dx, dy in dist:
                nx = x + dx
                ny = y + dy
                if nx >= 0 and nx < n and ny >= 0 and ny < m and grid[nx][ny] == -2:
                    nminute = minute + 1
                    grid[nx][ny] = nminute
                    q.append((nx, ny, nminute))
                    total_min = max(total_min, nminute)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == -2:
                    return -1
        return total_min

