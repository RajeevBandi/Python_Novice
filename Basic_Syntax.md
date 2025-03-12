# Basic Syntax

## Overview
Python is a high-level, interpreted programming language known for its simplicity and readability. Understanding Python's basic syntax is essential for writing efficient and error-free programs. This document provides a detailed explanation of Python's fundamental syntax, including variables, data types, comments, indentation, and operators.

---

## 1. Variables and Assignment
Variables in Python are used to store data values. Unlike many other languages, Python does not require explicit declaration of variable types.

### **Declaring Variables**
Python variables are dynamically typed, meaning their data type is inferred based on the assigned value.
```python
x = 10       # Integer
name = "John" # String
pi = 3.14     # Float
is_valid = True # Boolean
```

### **Reassigning Variables**
Variables can be reassigned with different data types without any explicit type conversion.
```python
x = 10  # Initially an integer
x = "Hello"  # Now a string
```

### **Multiple Assignments**
Python allows assigning multiple variables in a single line.
```python
a, b, c = 1, 2, 3
```

---

## 2. Data Types in Python
Python supports various built-in data types, which can be classified as follows:

### **Numeric Types**
- `int`: Integer values (e.g., `10`, `-5`)
- `float`: Floating-point numbers (e.g., `3.14`, `-0.01`)
- `complex`: Complex numbers (e.g., `3+4j`)

### **Sequence Types**
- `str`: Strings (e.g., "Hello")
- `list`: Ordered, mutable collections (e.g., `[1, 2, 3]`)
- `tuple`: Ordered, immutable collections (e.g., `(1, 2, 3)`)

### **Set Types**
- `set`: Unordered, unique elements (e.g., `{1, 2, 3}`)
- `frozenset`: Immutable set

### **Mapping Type**
- `dict`: Key-value pairs (e.g., `{"name": "Alice", "age": 25}`)

### **Boolean Type**
- `bool`: Represents `True` or `False`

---

## 3. Comments in Python
Comments are used to describe code and improve readability. Python supports both single-line and multi-line comments.

### **Single-Line Comments**
Use `#` to add a single-line comment.
```python
# This is a single-line comment
x = 10  # Variable declaration
```

### **Multi-Line Comments**
Triple quotes (`'''` or `"""`) can be used for multi-line comments.
```python
"""
This is a multi-line comment.
It spans multiple lines.
"""
print("Hello")
```

---

## 4. Indentation in Python
Python uses indentation (whitespace) to define code blocks instead of curly braces (`{}`). Indentation is mandatory and determines the structure of the code. The recommended indentation is **4 spaces per level**.

### **Example of Indentation**
```python
if True:
    print("This is inside the block")
    for i in range(3):
        print(i)
```

Failing to use proper indentation results in a `IndentationError`. Python enforces this strictly, making the code more readable and reducing the chances of missing block delimiters.

---

## 5. Operators in Python
Operators perform operations on variables and values. Python provides several types of operators:

### **Arithmetic Operators**
Used for performing mathematical operations.
```python
x = 10
y = 3
print(x + y)  # Addition (13)
print(x - y)  # Subtraction (7)
print(x * y)  # Multiplication (30)
print(x / y)  # Division (3.3333)
print(x % y)  # Modulus (1)
print(x ** y) # Exponentiation (1000)
```

### **Comparison Operators**
Used to compare values and return Boolean results (`True` or `False`).
```python
print(10 == 10)  # True (Equality check)
print(10 != 5)   # True (Not equal check)
print(10 > 5)    # True (Greater than check)
print(10 < 5)    # False (Less than check)
```

### **Logical Operators**
Used to combine conditional statements.
```python
x = True
y = False
print(x and y)  # False (Both must be True)
print(x or y)   # True (At least one is True)
print(not x)    # False (Negation)
```

### **Assignment Operators**
Used to assign and update variable values efficiently.
```python
a = 5
a += 3  # Equivalent to a = a + 3 (Now a is 8)
print(a)
```
