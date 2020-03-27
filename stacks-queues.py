class StackMin:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, num):
        if len(self.mins) == 0 or num <= self.mins[-1]:
            self.mins.append(num)
        self.stack.append(num)

    def pop(self):
        if self.stack[-1] == self.mins[-1]:
            self.mins.pop()
        return self.stack.pop()

    def min(self):
        return self.mins[-1]

class SetOfStacks:
    def __init__(self, cap):
        self.stacks = [[]]
        self.cap = cap

    def push(self, elem):
        stack = self.stacks[-1]
        if len(stack) >= self.cap:
            stack = []
            self.stacks.append(stack)

        stack.append(elem)

    def pop(self):
        stack = self.stacks[-1]
        elem = stack.pop()
        if len(stack) == 0:
            self.stacks.pop()
        return elem

    def pop_at(self, i):
        stack = self.stacks[i]
        elem = stack.pop()
        if len(stack) == 0:
            self.stacks.pop(i)
        return elem

# 1 2 3 4
# 4 3 2 

class MyQueue:
    def __init__(self):
        self.stack = []
        self.stack_reversed = []

    def enqueue(self, elem):
        self.stack.append(elem)
        length = len(self.stack_reversed)
        for _ in range(length):
            self.stack.append(self.stack_reversed.pop())
        self.stack_reversed.append(elem)
        for _ in range(length):
            self.stack_reversed.append(self.stack.pop())
        
    def dequeue(self):
        if len(self.stack_reversed) == 0:
            return None
        elem = self.stack_reversed.pop()
        length = len(self.stack_reversed)
        for _ in range(length):
            self.stack_reversed.append(self.stack.pop())
        self.stack.pop()
        for _ in range(length):
            self.stack.append(self.stack_reversed.pop())
        return elem


if __name__ == "__main__":
    q = MyQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.stack, q.stack_reversed)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.stack, q.stack_reversed)





