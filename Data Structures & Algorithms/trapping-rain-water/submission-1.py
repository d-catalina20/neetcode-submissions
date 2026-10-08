class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        maxHl, maxHr = height[l], height[r]
        res = 0

        while l < r:
            if maxHl < maxHr:
                l += 1
                maxHl = max(maxHl, height[l])
                res += maxHl - height[l]
            else:
                r -= 1
                maxHr = max(maxHr, height[r])
                res += maxHr - height[r]
        
        return res