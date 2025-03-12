# Data Structures

## Overview
Python provides a variety of built-in and user-defined data structures that help in efficient data storage, retrieval, and manipulation. Understanding these structures is fundamental for writing optimized and scalable programs. This document provides a detailed overview of the most commonly used data structures in Python.

---

## 1. Lists

Lists are ordered, mutable collections that allow duplicate elements. They are commonly used to store sequences of data and provide various operations such as appending, removing, and sorting elements.

### Key Features:
- Dynamic size, can grow or shrink as needed
- Allows elements of different data types
- Supports indexing and slicing for easy access
- Common operations include `append()`, `remove()`, `sort()`, and `reverse()`

### Example:
```python
my_list = [1, 2, 3, 4, 5]
print(my_list[0]) 
```

---

## 2. Tuples

Tuples are ordered, immutable collections, meaning they cannot be modified after creation. They are useful for storing fixed collections of data where modification is not required.

### Key Features:
- Faster than lists due to immutability
- Used as keys in dictionaries when hashable
- Supports indexing and slicing like lists

### Example:
```python
my_tuple = (1, 2, 3, 4)
print(my_tuple[1]) 
```

---

## 3. Sets

Sets are unordered collections of unique elements. They are primarily used for membership testing, removing duplicates, and mathematical operations such as union and intersection.

### Key Features:
- No duplicate values
- Unordered and unindexed
- Supports operations like union (`|`), intersection (`&`), and difference (`-`)

### Example:
```python
my_set = {1, 2, 3, 4}
print(3 in my_set) 
```

---

## 4. Dictionaries

Dictionaries store key-value pairs and provide fast lookups. They are commonly used to represent structured data and mappings.

### Key Features:
- Keys must be unique and immutable (strings, numbers, or tuples)
- Maintains insertion order (Python 3.7+)
- Efficient lookup, addition, and deletion

### Example:
```python
my_dict = {'name': 'Alice', 'age': 25}
print(my_dict['name']) 
```

---

## 5. Stacks

Stacks follow the **LIFO (Last In, First Out)** principle, meaning the last element added is the first to be removed. They are useful for managing function calls, undo operations, and backtracking algorithms.

### Key Features:
- Operations include `push` (adding an element) and `pop` (removing an element)
- Implemented using lists or `collections.deque` for efficiency

### Example:
```python
stack = []
stack.append(1)  # Pushing an element
stack.pop() 
```

---

## 6. Queues

Queues follow the **FIFO (First In, First Out)** principle, meaning the first element added is the first to be removed. They are commonly used in scheduling tasks and breadth-first search (BFS) algorithms.

### Key Features:
- Operations include `enqueue` (adding an element) and `dequeue` (removing an element)
- Implemented using `collections.deque` for efficiency

### Example:
```python
from collections import deque
queue = deque([1, 2, 3])
queue.popleft()
```

---

## 7. Linked Lists

A linked list consists of nodes connected linearly, where each node contains data and a reference to the next node. Unlike arrays, linked lists do not require contiguous memory allocation.

### Key Features:
- Dynamic memory allocation, no fixed size
- Insertion and deletion are efficient compared to arrays
- Types include singly linked list, doubly linked list, and circular linked list

### Example:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```
