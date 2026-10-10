class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        end = n
        for i in range(n - 1, -1, -1):
            if i + nums[i] >= end:
                end = i
        return end == 0
        