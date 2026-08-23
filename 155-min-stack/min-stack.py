class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, value: int) -> None:
        if not self.stack or (self.minstack[-1] >= value):
            self.minstack.append(value)
        self.stack.append(value)

    def pop(self) -> None:
        if not self.stack:
            return None
        popped = self.stack.pop()
        if self.minstack[-1] == popped:
            self.minstack.pop()
        
    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.minstack:
            return None
        return self.minstack[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()