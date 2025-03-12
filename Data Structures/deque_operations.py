from collections import deque

# Creating Deque
dq1 = deque([10, 20, 30, 40, 50]) 
dq2 = deque("Python")  
dq3 = deque() 

print("Deque 1:", dq1)
print("Deque 2:", dq2)
print("Empty Deque:", dq3)

# Adding Elements
dq1.append(60) 
dq1.appendleft(5)
print("After Append Operations:", dq1)

# Removing Elements
dq1.pop() 
dq1.popleft()
print("After Pop Operations:", dq1)

# Accessing Elements
print("First Element:", dq1[0])
print("Last Element:", dq1[-1])

# Reversing a Deque
dq1.reverse()
print("Reversed Deque:", dq1)

# Rotating a Deque
dq1.rotate(2)
print("After Right Rotation:", dq1)

dq1.rotate(-2)
print("After Left Rotation:", dq1)

# Extending a Deque
dq1.extend([70, 80, 90])
dq1.extendleft([0, -10, -20]) 
print("After Extending Deque:", dq1)

# Removing Specific Elements
dq1.remove(30) 
print("After Removing 30:", dq1)

# Finding the Length of Deque
print("Length of Deque:", len(dq1))

# Clearing a Deque
dq1.clear()
print("Cleared Deque:", dq1)
