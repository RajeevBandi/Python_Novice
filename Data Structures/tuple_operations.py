# Creating Tuples
my_tuple = (10, "Python", 3.14, True)
print("Original Tuple:", my_tuple)

# Accessing Elements
print("First Element:", my_tuple[0])
print("Last Element:", my_tuple[-1])

# Slicing a Tuple
numbers = (1, 2, 3, 4, 5, 6, 7, 8)
print("Sliced Tuple [2:5]:", numbers[2:5])
print("Reversed Tuple:", numbers[::-1])

# Tuple Packing and Unpacking
person = ("Alice", 25, "Engineer")
name, age, profession = person 
print(f"Unpacked Values - Name: {name}, Age: {age}, Profession: {profession}")

# Tuple Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated = tuple1 + tuple2
print("Concatenated Tuple:", concatenated)

# Checking Element Existence
print("Is 3 in tuple1?", 3 in tuple1)
print("Is 10 in tuple1?", 10 in tuple1)

# Looping Through a Tuple
for item in my_tuple:
    print("Item:", item)

# Tuple Methods
example_tuple = (10, 20, 30, 40, 20, 20)
print("Count of 20:", example_tuple.count(20))
print("Index of 30:", example_tuple.index(30)) 

# Tuple as Dictionary Keys
coordinates = {(10, 20): "Point A", (30, 40): "Point B"}
print("Dictionary with Tuple Keys:", coordinates)
print("Value for (10,20):", coordinates[(10, 20)])