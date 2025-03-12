# Functions

## Introduction
Functions in Python are reusable blocks of code designed to perform a specific task. They help improve code organization, readability, and reusability by avoiding redundancy. Using functions allows developers to break down complex problems into smaller, more manageable pieces.

## What is a Function?
A function is a named sequence of statements that performs a specific task. Functions allow us to write modular code that can be executed multiple times with different inputs. They help reduce duplication and make the code more organized and maintainable.

## Defining a Function
Functions are defined using the `def` keyword, followed by a function name, parameters (if any), and a block of code. A function may return a value to the caller using the `return` statement.

### Syntax:
```python
def function_name(parameters):
    """Optional docstring to describe the function."""
    # Function body
    return value  # Optional
```

## Calling a Function
To execute a function, use its name followed by parentheses, passing required arguments if applicable. Calling a function executes its block of code and returns the result (if any).

### Example:
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

## Function Parameters and Arguments
Functions can accept parameters to process different data. Arguments are the actual values passed when calling a function. Parameters help functions become more flexible and dynamic.

### Types of Arguments:
1. **Positional Arguments**: Passed in order and must match function parameters.
2. **Keyword Arguments**: Passed with parameter names to avoid order dependency.
3. **Default Arguments**: Assigned a default value if not provided.
4. **Variable-Length Arguments**:
   - `*args`: Accepts multiple positional arguments as a tuple.
   - `**kwargs`: Accepts multiple keyword arguments as a dictionary.

### Example:
```python
def display_info(name, age=25):  # Default argument
    print(f"Name: {name}, Age: {age}")

display_info("Bob", 30)  # Positional argument
display_info(age=40, name="Charlie")  # Keyword argument
```

## Return Statement
The `return` statement allows a function to send back a value to the caller. Functions can return any data type, including numbers, strings, lists, dictionaries, or even other functions.

### Example:
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

## Lambda Functions
A `lambda` function is an anonymous, single-expression function often used for short, simple operations. They are useful when a function is required for a short period and does not need a formal definition.

### Syntax:
```python
lambda arguments: expression
```

### Example:
```python
square = lambda x: x * x
print(square(4))  # Output: 16
```

## Scope and Lifetime of Variables
Variables in functions have **local scope**, meaning they exist only inside the function. Python also supports **global variables** that persist throughout execution. However, modifying global variables inside a function requires the `global` keyword.

### Example:
```python
global_var = "I am global"

def my_function():
    local_var = "I am local"
    print(local_var)
    print(global_var)

my_function()
print(global_var)
```

## Recursive Functions
A function can call itself, creating recursion. This is useful for solving problems like calculating factorials, generating Fibonacci sequences, and solving divide-and-conquer problems.

### Example:
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

## Nested Functions
Functions can be defined inside other functions to encapsulate logic. Nested functions help in maintaining a cleaner structure and restrict functionality to the scope where it is needed.

### Example:
```python
def outer_function():
    def inner_function():
        return "Hello from inner function!"
    return inner_function()

print(outer_function())
```

## First-Class Functions
Functions in Python are first-class citizens, meaning they can be assigned to variables, passed as arguments, and returned from other functions. This feature enables functional programming techniques.

### Example:
```python
def say_hello():
    return "Hello!"

greet = say_hello  # Assigning function to a variable
print(greet())  # Output: Hello!
```

## Higher-Order Functions
Functions that take other functions as parameters or return them are known as higher-order functions. These allow operations like mapping, filtering, and function composition.

### Example:
```python
def apply_function(func, value):
    return func(value)

double = lambda x: x * 2
print(apply_function(double, 5))  # Output: 10
```

## Decorators
Decorators are a special type of higher-order function used to modify the behavior of another function without altering its code. They are commonly used for logging, authentication, and access control.

### Example:
```python
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print("Display function executed!")

display()
```

## Built-in Functions
Python provides several built-in functions like `print()`, `len()`, `sum()`, `max()`, and `min()`, which perform common operations. These functions help simplify coding tasks and enhance efficiency.
