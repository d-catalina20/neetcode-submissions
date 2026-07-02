class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<int>> island(n, vector<int>(m, 0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '1') {
                    island[i][j] = 1;
                }
            }
        }

        int isl_count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (island[i][j] == 1) {
                    isl_count++;
                    bfs(i, j, n, m, island);
                }
            }
        }

        return isl_count;
    }

    void bfs(int u, int v, int n, int m, vector<vector<int>>& island) {
        int dx[] = {0, 1, 0, -1};
        int dy[] = {1, 0, -1, 0};
        queue<pair<int,int>> q;
        q.push({u, v});
        while(!q.empty()) {
            int x = q.front().first;
            int y = q.front().second;
            q.pop();

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && island[nx][ny] == 1) {
                    q.push({nx, ny});
                    island[nx][ny] = 0;
                }
            }
        }
    }
};
