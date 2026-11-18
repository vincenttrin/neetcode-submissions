# non-optimal: have one stack. push, pop, and top as needed. Get min runs a min() operation on the stack (cons: not constant run time.)
# more optimized: have 2 stacks. one tracks the value added to the stack and the other tracks the min value in the stack at the time. this way getMin we just return the top of the min_stack array.

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # if stack is empty, min stack value is val
        if not self.stack:
            self.min_stack.append(val)
        # else: choose min between val and the last min_stack value
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]        
