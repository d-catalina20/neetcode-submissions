class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        n = len(nums)
        vis = set()

        def bt():
            if len(sol) == n:
                res.append(list(sol))
                return
            for i in range(0, n):
                if nums[i] not in vis:
                    vis.add(nums[i])
                    sol.append(nums[i])
                    bt()
                    sol.pop()
                    vis.remove(nums[i])

        bt()
        return res
