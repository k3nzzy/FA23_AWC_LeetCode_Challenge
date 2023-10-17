class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        
        # populate the stacks
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(t))
        
        return stack[-1]
        
