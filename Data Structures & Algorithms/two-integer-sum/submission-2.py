class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = []
        for i, num in enumerate(nums):
            nums_sorted.append([num, i])
        
        nums_sorted.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            curr = nums_sorted[i][0] + nums_sorted[j][0]
            if curr == target:
                return [min(nums_sorted[i][1], nums_sorted[j][1]),
                        max(nums_sorted[i][1], nums_sorted[j][1])]
            elif curr < target:
                i += 1
            else:
                j -= 1
        return []
