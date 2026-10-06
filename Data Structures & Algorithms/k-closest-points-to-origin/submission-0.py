class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for i in range(len(points)):
            dist.append([points[i][0]**2 + points[i][1]**2, points[i][0], points[i][1]])
        
        heapq.heapify(dist)
        res = []
        while len(res) < k:
            d, x, y = heapq.heappop(dist)
            res.append([x, y])

        return res
        
        
        