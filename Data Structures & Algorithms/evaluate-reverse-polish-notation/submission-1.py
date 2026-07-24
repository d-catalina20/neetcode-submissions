class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '-', '*', '/'}
        for tok in tokens:
            if tok not in ops:
                stack.append(int(tok))
            else:
                if stack and len(stack) >= 2:
                    b = stack.pop()
                    a = stack.pop()
                    if tok == '+':
                        stack.append(a + b)
                    elif tok == '-':
                        stack.append(a - b)
                    elif tok == '*':
                        stack.append(a * b)
                    else:
                        stack.append(int (a / b))
        return stack[0]
        