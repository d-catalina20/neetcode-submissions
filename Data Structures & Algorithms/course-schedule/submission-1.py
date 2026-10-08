class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[b].append(a)
        c = [0] * numCourses

        def dfs(x):
            c[x] = 1
            for y in adj[x]:
                if c[y] == 1:
                    return True
                if c[y] == 0 and dfs(y):
                    return True
            c[x] = 2
            return False
        
        isCycle = False
        for i in range(numCourses):
            if c[i] == 0:
                if dfs(i):
                    return False
        return True


        