class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = None

    def push(self, val: int) -> None:
        if self.minVal == None or self.minVal > val:
            self.minVal = val
        self.stack.append(val)        

    def pop(self) -> None:
        if self.stack.pop() == self.minVal:
            self.minVal = None
            for i in range(len(self.stack)):
                if self.minVal == None or self.stack[i] < self.minVal:
                    self.minVal = self.stack[i]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal