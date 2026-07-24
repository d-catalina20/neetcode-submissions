class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            if idx == 0:
                stack.append((idx, temp))
            else:
                cur_idx, cur_temp = stack[-1]
                while stack and temp > cur_temp:
                    res[cur_idx] = idx - cur_idx
                    stack.pop()
                    if stack:
                        cur_idx, cur_temp = stack[-1]
                stack.append((idx,temp))
            # print(stack)
        return res


        