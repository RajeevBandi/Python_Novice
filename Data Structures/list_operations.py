
# Creating Lists
my_list = [10, "Python", 3.14, True]
print("Original List:", my_list)

# Accessing Elements
print("First Element:", my_list[0])
print("Last Element:", my_list[-1])

# Slicing a List
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print("Sliced List [2:5]:", numbers[2:5])
print("Reversed List:", numbers[::-1])

# Modifying a List
my_list[1] = "Java"
my_list.append("New Item")
my_list.insert(2, "Inserted Item")
print("Modified List:", my_list)

# Removing Elements
my_list.remove("Java")
del my_list[1]
popped_item = my_list.pop()
print("After Removals:", my_list, "Popped Item:", popped_item)

# Looping Through a List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit.upper())

# Sorting
nums = [5, 2, 8, 1, 9]
nums.sort()
print("Sorted List:", nums)

# Reversing
nums.sort(reverse=True)
print("Descending Sort:", nums)

# Copying Lists 
original_list = [1, 2, 3]
copied_list = original_list.copy()
copied_list.append(4)
print("Original List:", original_list)
print("Copied List:", copied_list)

# List Methods
example_list = [10, 20, 30, 40, 50]
print("Count of 20:", example_list.count(20))
print("Index of 30:", example_list.index(30))

example_list.reverse()
print("Reversed List:", example_list)

example_list.sort()
print("Sorted List:", example_list)

