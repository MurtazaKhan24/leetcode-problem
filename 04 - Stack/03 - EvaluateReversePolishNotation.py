class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['+', '-', '*', '/']
        for n in tokens:
            if n == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif n == "-":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1 - num2)
            elif n == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif n == "/":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(int(num1 / num2))
            else:
                stack.append(int(n))
        print(stack)
        return stack[-1]