class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        res = [intervals[0]]
        for x, y in intervals:
            if x <= res[-1][1]:
                res[-1][1] = max(res[-1][1], y)
            else:
                res.append([x, y])
        return res