from collections import deque
from queue import LifoQueue


# Stack Implementation Using List
print("\n--------- Stack Implementation Using List ---------")

class StackList:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item) 
        print(f"Pushed {item} -> Stack: {self.stack}")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop from an empty stack.")
            return None
        return self.stack.pop()  

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.stack[-1]  

    def is_empty(self):
        return len(self.stack) == 0  

    def size(self):
        return len(self.stack)  

stack1 = StackList()
stack1.push(10)
stack1.push(20)
stack1.push(30)

print("Popped:", stack1.pop())
print("Top Element:", stack1.peek())
print("Stack Size:", stack1.size()) 


# Stack Implementation Using deque
print("\n--------- Stack Implementation Using deque ---------")

class StackDeque:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} -> Stack: {self.stack}")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop from an empty stack.")
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

stackDq = StackDeque()
stackDq.push(100)
stackDq.push(200)
stackDq.push(300)

print("Popped:", stackDq.pop()) 
print("Top Element:", stackDq.peek())
print("Stack Size:", stackDq.size()) 


# Stack Implementation Using LifoQueue
print("\n--------- Stack Implementation Using LifoQueue ---------")

stack = LifoQueue(maxsize=5) 

stack.put(1)
stack.put(2)
stack.put(3)

print("Stack size:", stack.qsize()) 
print("Popped element:", stack.get())
print("Is stack empty?", stack.empty())  
print("Is stack full?", stack.full()) 

