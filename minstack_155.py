class MinStack:

    #time complexity = o(1)
    #space complexity = o(n)
    #used two stacks, stack to keep track of the original stack input and min stack to keep track of the minimum value in the stack. 
    #When a value is pushed its added to stack and min stack if minstack is empty or if the value is less than the last value in minstack. Mimimum will always be the last element in min stack.
    #pop removes value from both stacks, top returns the last element in stack and getmin returns the last element in min stack (minimum).
    def __init__(self):
        self.stack = [] 
        self.min_stack = [] #min_stack to store the minimum stack value

    def push(self, val: int) -> None:
        self.stack.append(val) 
        #check if minstack is empty or if the value being pushed is less than or equal to the current minimum value
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)


    def pop(self) -> None:
        if len(self.stack) != 0:
            value = self.stack.pop()
        #remove value from min stack if it's removed from original stack
        if value == self.min_stack[-1]:
                self.min_stack.pop()


    def top(self) -> int:
        if len(self.stack) != 0:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min_stack) != 0:
            return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
