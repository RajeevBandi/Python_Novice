# 1. Creating Strings
greeting = "Hello, World!"
quote = 'Python is amazing!'
multiline_string = """This is a 
multi-line string in Python."""
print("Greeting:", greeting)
print("Quote:", quote)
print("Multiline String:\n", multiline_string)

# Accessing Characters in a String
first_char = greeting[0] 
last_char = greeting[-1]
print("First Character:", first_char)
print("Last Character:", last_char)

# Slicing a String
substring1 = quote[0:6]  
substring2 = quote[-8:] 
print("Substring 1:", substring1)
print("Substring 2:", substring2)

# String Length
print("Length of greeting:", len(greeting))

# String Methods
uppercase = greeting.upper()
lowercase = greeting.lower()
title_case = quote.title()
capitalized = quote.capitalize()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Title Case:", title_case)
print("Capitalized:", capitalized)

# String Replace
modified_quote = quote.replace("amazing", "powerful")
print("Modified Quote:", modified_quote)

# Checking Substrings
print("Does 'Python' exist in quote?", "Python" in quote)
print("Does 'Java' exist in quote?", "Java" in quote)

# String Formatting
name = "Alice"
age = 25
formatted_string = f"My name is {name} and I am {age} years old."
print("Formatted String:", formatted_string)

# Checking String Properties
print("Is 'Python123' alphanumeric?", "Python123".isalnum())
print("Is '12345' numeric?", "12345".isdigit())
print("Is 'HELLO' uppercase?", "HELLO".isupper())

# Reversing a String
reversed_string = greeting[::-1]
print("Reversed String:", reversed_string)

# Counting Occurrences
count_l = greeting.count("l")
print("Count of 'l' in greeting:", count_l)

# Finding a Substring
index_python = quote.find("Python")
index_not_found = quote.find("Java")
print("Index of 'Python':", index_python)
print("Index of 'Java' (not found):", index_not_found)

# Checking Start and End
print("Does greeting start with 'Hello'?", greeting.startswith("Hello"))
print("Does quote end with 'amazing!'?", quote.endswith("amazing!"))

# Multiline String Using Escape Characters
escaped_string = "Line 1\nLine 2\nLine 3"
print("Escaped Multiline String:\n", escaped_string)

# Encoding and Decoding
encoded_str = quote.encode("utf-8")
decoded_str = encoded_str.decode("utf-8")
print("Encoded String:", encoded_str)
print("Decoded String:", decoded_str)
