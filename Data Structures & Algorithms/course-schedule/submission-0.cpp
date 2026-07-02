class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        int m = prerequisites.size();
        for (int i = 0; i < m; i++) {
            int x = prerequisites[i][0];
            int y = prerequisites[i][1];
            adj[y].push_back(x);
        }
        vector<int> c(numCourses, 0); // 0 - white, 1 - gray, 2 - black

        bool isCycle = false;
        for (int i = 0; i < numCourses; i++) {
            if (c[i] == 0) {
                if (dfs(i, c, adj)) {
                    isCycle = true;
                    break;
                }
            }
        } 

        return !isCycle;
    }

    bool dfs(int node, vector<int>& c, vector<vector<int>>& adj) {
        c[node] = 1;
        for (int neigh : adj[node]) {
            if (c[neigh] == 1) {
                return true;
            }

            else if (c[neigh] == 0 && dfs(neigh, c, adj)) {
                return true;
            }
        }

        c[node] = 2;
        return false;
    }
};
