class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxA = 0
        # A = min(a, b) * (b - a)
        l = 0
        r = n - 1
        while l < r:
            hl = heights[l]
            hr = heights[r]
            maxA = max(maxA, min(hl, hr) * (r - l))
            if hl < hr:
                l += 1
            else:
                r -= 1

        return maxA

        