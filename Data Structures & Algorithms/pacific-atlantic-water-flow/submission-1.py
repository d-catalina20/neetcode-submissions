class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        pac, atl = set(), set()

        dist = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(x, y, viz, h):
            viz.add((x, y))

            for dx, dy in dist:
                nx = x + dx
                ny = y + dy
                if nx >= 0 and nx < n and ny >= 0 and ny < m and (nx, ny) not in viz and heights[nx][ny] >=  h:
                    dfs(nx, ny, viz, heights[nx][ny])

        for i in range(n):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, m - 1, atl, heights[i][m - 1])
        for j in range(m):
            dfs(0, j, pac, heights[0][j])
            dfs(n - 1, j, atl, heights[n - 1][j])
        
        rez = []
        for i in range(n):
            for j in range(m):
                if (i, j) in pac and (i, j) in atl:
                    rez.append([i, j])
        return rez

