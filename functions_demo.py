# Function Basics
print("\n--------- Function Basics ---------")
def greet():
    print("Hello, welcome to Python!")

greet()

# Function with Arguments
print("\n--------- Function with Arguments ---------")
def square(n):
    return n * n

print("Square of 5 is", square(5))

# Default Arguments
print("\n--------- Default Arguments ---------")
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Bob")

# Keyword Arguments
print("\n--------- Keyword Arguments ---------")
def user_details(name, age):
    print(f"Name: {name}, Age: {age}")

user_details(age=30, name="Charlie")

# Variable-length Arguments
print("\n--------- Variable-length Arguments ---------")
def add_numbers(*args):
    return sum(args)

print("Sum of numbers is", add_numbers(1, 2, 3, 4, 5))

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="David", age=28, city="NY")

# Lambda Functions
print("--------- Lambda Functions ---------")
square = lambda x: x * x
print("Square of 6 is", square(6))

# Built-in Functions with Functions
print("\n--------- map(), filter(), and reduce() ---------")
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print("Squared numbers are", squared_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers are", even_numbers)

from functools import reduce
sum_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers is", sum_numbers)

# Recursive Function
print("\n--------- Recursive Function ---------")
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5 is", factorial(5))

# Higher-Order Function
print("\n--------- Higher-Order Function ---------")
def apply_func(func, value):
    return func(value)

print("Applying square function to 5 results in", apply_func(lambda x: x**2, 5))

# Decorators
print("\n--------- Decorators ---------")
def decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@decorator
def say_hello():
    print("Hello, World!")

say_hello()

# Generators & `yield`
print("\n--------- Generators ---------")
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

gen = count_up_to(3)
print("Next value is", next(gen))
print("Next value is", next(gen))

# Closures
print("\n--------- Closures ---------")
def outer_function(msg):
    def inner_function():
        print("Message stored is", msg)  
    return inner_function

greet_func = outer_function("Hello")
greet_func()

# Partial Functions
print("\n--------- Partial Functions ---------")
from functools import partial
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=3)
print("5 raised to power 3 is", square(5))

# Pass by Value (Immutable types)
print("\n--------- Pass by Value ---------")
def modify_value(x):
    x = 10
    print("Inside function (Pass by Value): x =", x)

val = 5
print("Before function call: val =", val)
modify_value(val)
print("After function call: val =", val)

# Pass by Reference (Mutable types)
print("\n--------- Pass by Reference ---------")
def modify_list(lst):
    lst.append(4)
    print("Inside function (Pass by Reference): lst =", lst)

my_list = [1, 2, 3]
print("Before function call: my_list =", my_list)
modify_list(my_list)
print("After function call: my_list =", my_list)
