class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == "-":
                a = int(stack.pop())
                b = int(stack.pop())
                ans = b-a
                stack.append(ans)
            elif tokens[i] == "*":
                stack.append(stack.pop() * stack.pop())
            elif tokens[i] == "/":
                a = int(stack.pop())
                b = int(stack.pop())
                ans = int(b/a)
                stack.append(ans)
            else:
                stack.append(int(tokens[i]))
        return stack[0]