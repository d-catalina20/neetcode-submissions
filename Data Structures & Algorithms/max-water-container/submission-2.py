class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # A = min(a, b) * (b - a)
        idx_a, idx_b = 0, len(heights) - 1
        a = heights[idx_a]
        b = heights[idx_b]
        maxA = 0
        while idx_a < idx_b:
            maxA = max(maxA, min(a, b) * (idx_b - idx_a))
            if a <= b:
                idx_a += 1
                a = heights[idx_a]
            else:
                idx_b -= 1
                b = heights[idx_b]
        return maxA

        