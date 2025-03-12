# Basic try-except block
try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError as e:
    print(f"Invalid input! Error: {e}")


# Handling multiple exceptions
try:
    x = 10 / 0 
except ZeroDivisionError as e:
    print(f"Cannot divide by zero! Error: {e}")
except Exception as e:
    print(f"General error occurred: {e}")


# Using else and finally
try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print(f"File not found! Error: {e}")
else:
    print("File read successfully.")
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File closed.")


# Raising an exception manually
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")


# Custom Exception Class
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be above 18"):
        self.message = message
        super().__init__(self.message)

def validate_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. You must be 18 or older.")
    return "Age is valid."

try:
    print(validate_age(15))
except InvalidAgeError as e:
    print(f"Custom Exception Caught: {e}")


# Centralized Exception Handling
class ExceptionHandler:
    @staticmethod
    def handle_exception(exception):
        error_messages = {
            ValueError: "Invalid value provided!",
            ZeroDivisionError: "Math error: Division by zero is not allowed.",
            FileNotFoundError: "Requested file could not be found.",
            InvalidAgeError: "Age validation failed."
        }
        return error_messages.get(type(exception), f"An unexpected error occurred: {exception}")

try:
    raise FileNotFoundError("sample.txt is missing")
except Exception as e:
    print(ExceptionHandler.handle_exception(e))
