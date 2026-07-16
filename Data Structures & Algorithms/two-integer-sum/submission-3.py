class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}

        for i, val in enumerate(nums):
            dict_nums[val] = i

        for i, val in enumerate(nums):
            diff = target - val
            if diff in dict_nums and dict_nums[diff] != i:
                return [i, dict_nums[diff]]
        
        return []
