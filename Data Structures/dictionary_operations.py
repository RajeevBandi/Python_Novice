# Creating a Dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "skills": ["Python", "Java", "C++"]
}
print("Original Dictionary:", my_dict)

# Accessing Values
print("Name:", my_dict["name"])
print("Skills:", my_dict.get("skills"))

# Adding & Updating Key-Value Pairs
my_dict["email"] = "alice@example.com"  
my_dict["age"] = 26
print("Updated Dictionary:", my_dict)

# Removing Elements
removed_value = my_dict.pop("city")
print("After pop():", my_dict, "Removed Value:", removed_value)

del my_dict["email"]
print("After del:", my_dict)

# Looping Through a Dictionary
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# Checking Existence of a Key
print("Is 'age' in dictionary?", "age" in my_dict)
print("Is 'salary' in dictionary?", "salary" in my_dict)

# Merging Two Dictionaries
extra_info = {"gender": "Female", "hobby": "Reading"}
my_dict.update(extra_info) 
print("After Merging:", my_dict)

# Copying a Dictionary 
original_dict = {"a": 1, "b": 2}
copied_dict = original_dict.copy()
copied_dict["c"] = 3
print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copied_dict)

# Dictionary Methods
example_dict = {"x": 100, "y": 200, "z": 300}
print("Keys:", example_dict.keys())
print("Values:", example_dict.values())
print("Items:", example_dict.items())

# Dictionary clear
example_dict.clear()
print("After clear():", example_dict)

