class Solution:
    def bt(self, step: int, n: int, rez: List[List[int]], sol: List[int], nums: List[int]) -> List[List[int]]:
        rez.append(list(sol))
        for i in range(step, n):
            sol.append(nums[i])
            self.bt(i + 1, n, rez, sol, nums)
            sol.pop()
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rez = []
        self.bt(0, len(nums), rez, [], nums)
        return rez
        
        