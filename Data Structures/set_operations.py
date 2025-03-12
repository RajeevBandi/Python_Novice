# Creating Sets with Unique Values
fruits = {"apple", "banana", "cherry", "mango"}
colors = {"red", "blue", "green", "yellow"}
numbers = {10, 20, 30, 40, 50}
print("Fruits Set:", fruits)
print("Colors Set:", colors)
print("Numbers Set:", numbers)

# Creating an Empty Set 
empty_set = set()
print("Empty Set:", empty_set)

# Adding Elements to a Set
fruits.add("orange")
colors.add("purple")
numbers.add(60)
print("After Adding Elements:")
print("Fruits:", fruits)
print("Colors:", colors)
print("Numbers:", numbers)

# Removing Elements from a Set
fruits.remove("banana")  # error if element is missing
colors.discard("blue")  # No error if element is missing
numbers.discard(100)  # No error if element is missing
print("After Removing Elements:")
print("Fruits:", fruits)
print("Colors:", colors)
print("Numbers:", numbers)

# Popping an Element (Removes and returns a random element)
popped_fruit = fruits.pop()
popped_color = colors.pop()
popped_number = numbers.pop()
print("After Pop Operation:")
print("Fruits:", fruits, "Popped Fruit:", popped_fruit)
print("Colors:", colors, "Popped Color:", popped_color)
print("Numbers:", numbers, "Popped Number:", popped_number)

# Checking Element Existence
print("Is 'mango' in fruits?", "mango" in fruits)
print("Is 'pink' in colors?", "pink" in colors)
print("Is 50 in numbers?", 50 in numbers)

# Set Operations: Union, Intersection, Difference, Symmetric Difference
prime_numbers = {2, 3, 5, 7, 11, 13}
even_numbers = {2, 4, 6, 8, 10, 12}

union_set = prime_numbers | even_numbers  # Union (All unique elements)
intersection_set = prime_numbers & even_numbers  # Intersection (Common elements)
difference_set = prime_numbers - even_numbers  # Difference (Elements in prime_numbers but not in even_numbers)
symmetric_diff_set = prime_numbers ^ even_numbers  # Symmetric Difference (Elements in either but not both)

print("Union of Primes and Evens:", union_set)
print("Intersection of Primes and Evens:", intersection_set)
print("Difference (Primes - Evens):", difference_set)
print("Symmetric Difference:", symmetric_diff_set)

# Updating Sets
fruits.update(["grape", "kiwi", "papaya"]) 
colors.update({"black", "white"}) 
numbers.update({70, 80, 90})
print("After update():")
print("Fruits:", fruits)
print("Colors:", colors)
print("Numbers:", numbers)

# Frozenset (Immutable Set)
frozen_days = frozenset({"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"})
print("Frozenset:", frozen_days)

# Clearing a Set
fruits.clear()
print("After Clearing Fruits Set:", fruits)
