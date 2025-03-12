# Control Flow

## Overview
Control flow in Python determines the order in which statements are executed. It includes conditional statements, loops, and exception handling. Understanding control flow is crucial for writing logical and efficient programs, as it allows the developer to direct the execution of code based on conditions and loops.

---

## 1. Default Execution Flow

By default, Python executes code sequentially, line by line, from top to bottom. When a script runs, each statement is processed in the order it appears unless redirected by control structures such as conditions, loops, or function calls. 

Python follows an **interpreted execution model**, meaning that it reads and executes each line of code one at a time. Unlike compiled languages, Python does not require a separate compilation step; instead, it translates code into bytecode dynamically at runtime.

### Example:
```python
print("Step 1: Start")
print("Step 2: Execute")
print("Step 3: End")
```

This will output:
```
Step 1: Start
Step 2: Execute
Step 3: End
```

However, this default execution flow can be altered by using control structures such as conditionals, loops, and functions.

---

## 2. Conditional Statements

Conditional statements allow the execution of different blocks of code based on conditions.

### **if Statement**
The `if` statement evaluates a condition and executes the indented block of code if the condition is `True`.
```python
x = 10
if x > 5:
    print("x is greater than 5")
```

### **if-else Statement**
An `if-else` statement executes one block of code if the condition is `True` and another block if it is `False`.
```python
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")
```

### **if-elif-else Statement**
When multiple conditions need to be checked, `elif` (short for "else if") allows for multiple conditions in a structured way.
```python
x = 10
if x > 10:
    print("Greater than 10")
elif x == 10:
    print("Equal to 10")
else:
    print("Less than 10")
```

---

## 3. Loops

Loops allow repeated execution of a block of code as long as a condition is met.

### **for Loop**
The `for` loop is used to iterate over a sequence (such as a list, tuple, dictionary, or string).
```python
for i in range(5):
    print(i)
```
This prints numbers from `0` to `4`.

### **while Loop**
The `while` loop runs as long as the condition remains `True`.
```python
x = 0
while x < 5:
    print(x)
    x += 1
```

If the condition never becomes `False`, the loop can run indefinitely, leading to an infinite loop.

---

## 4. Loop Control Statements

Loop control statements alter the normal execution flow inside loops.

### **break Statement**
The `break` statement terminates the loop immediately.
```python
for i in range(5):
    if i == 3:
        break
    print(i)
```
This stops execution when `i` reaches `3`.

### **continue Statement**
The `continue` statement skips the rest of the code in the current iteration and moves to the next iteration.
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```
This skips `2` but continues execution for other values.

### **pass Statement**
The `pass` statement acts as a placeholder for future code.
```python
for i in range(5):
    if i == 2:
        pass
    print(i)
```
This ensures that an empty loop does not result in an error.

---

## 5. Exception Handling

Exception handling allows a program to handle runtime errors gracefully instead of crashing.
