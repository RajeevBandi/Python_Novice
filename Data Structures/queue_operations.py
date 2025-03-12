from collections import deque
from queue import Queue

# Queue Implementation Using Queue
print("\n--------- Queue Implementation Using list ---------")

class QueueList:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item) 
        print(f"Enqueued {item} -> Queue: {self.queue}")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Cannot dequeue from an empty queue.")
            return None
        return self.queue.pop(0) 

    def front(self):
        return self.queue[0] if not self.is_empty() else None 

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

queue1 = QueueList()
queue1.enqueue(10)
queue1.enqueue(20)
queue1.enqueue(30)

print("Dequeued:", queue1.dequeue()) 
print("Front Element:", queue1.front()) 
print("Queue Size:", queue1.size()) 

# Queue Implementation Using Queue
print("\n--------- Queue Implementation Using deque ---------")

from collections import deque

class QueueDeque:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item} -> Queue: {self.queue}")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Cannot dequeue from an empty queue.")
            return None
        return self.queue.popleft()

    def front(self):
        return self.queue[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example Usage
queueDq = QueueDeque()
queueDq.enqueue(100)
queueDq.enqueue(200)
queueDq.enqueue(300)

print("Dequeued:", queueDq.dequeue()) 
print("Front Element:", queueDq.front())
print("Queue Size:", queueDq.size()) 

# Queue Implementation Using Queue
print("\n--------- Queue Implementation Using Queue ---------")

queue = Queue(maxsize=5) 

queue.put(1)
queue.put(2)
queue.put(3)

print("Queue size:", queue.qsize()) 
print("Dequeued element:", queue.get()) 
print("Is queue empty?", queue.empty())
print("Is queue full?", queue.full())


