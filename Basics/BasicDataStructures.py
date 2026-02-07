print("----- Topic: Basic Data Structures -----")
# List
print("Subtopic: List")
numbers = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20]
fruits = ["apple", "banana", "cherry" , "date" , "orange" , "papaya" , "quince" , "raspberry" , "strawberry" , "tangerine" , "ugli fruit" , "watermelon"]
mixed = [1, "hello", True, 3.5]

print("Value of my_list:", numbers)
print("Value of mixed" , mixed)
print("Type of my_list:", type(numbers))
# Lists are ordered, mutable collections of items. They can contain elements of different data types and are defined using square brackets [].
print(fruits[0]) # O ==> 1st element that is apple
print(fruits[2]) # 2 ==> 3rd element that is cherry
print(fruits[-1]) # -1 ==> last element that is cherry

# Slicing List
# 
print(fruits[0:2]) # ['apple', 'cherry']
print(fruits[1:]) # ['banana', 'cherry']
print(fruits[:2]) # ['apple', 'banana']
print(fruits[-2:]) # ['banana', 'cherry']
print(numbers[::2] ) # [1, 3, 5, 7, 9 , 11 , 13 , 15 , 17 , 19] as it is taking every 2nd element starting from index 0
print(numbers[1::2]) # [2, 4, 6, 8 , 10 , 12 , 14 , 16 , 18 , 20] as it is taking every 2nd element starting from index 1

# Manipulating List
# Lists can be manipulated using various methods such as append(), insert(), remove(), pop(), etc
print("-----Appended kiwi at end of list-----")
fruits.append("kiwi") # adds kiwi to the end of the list
print(fruits) 
print("-----inserted blueberry at end of list-----")
fruits.insert(1 , "blueberry") # adds blueberry at index 1
print(fruits)
print("-----removed banana at end of list-----")
fruits.remove("banana") # removes banana from the list
print(fruits)
print("-----removed last element from list-----")
fruits.pop() # removes the last element from the list
print(fruits)

print("Count of fruits" , len(fruits)) # gives the count of fruits in the list
print("Count of fruits" , fruits.count("apple")) # gives the count of fruits in the list

## Tuples in python 
print("-----Topic: Tuple-----")
# A tuple is a collection of ordered items, just like a list. But unlike a list, you cannot change the elements once a tuple is created. This unchangeable nature is called immutability
my_tuple = (1, 2, 3, "hello", True)
print("Value of my_tuple:", my_tuple)
print("Type of my_tuple:", type(my_tuple))
# Tuples use parentheses (), are immutable, can hold mixed types, and may be used as dictionary keys.
# ACTION: TUPLE ALLOWED
# - Access by index: Yes
# - Count values: Yes
# - Find index: Yes
# - Slice values: Yes
# - Re-assign entire Tuple: Yes
# Operation on tuples
print(my_tuple[0])  # Accesses the first element (index 0), which is 1
print(my_tuple[-1])  # Accesses the last element (index -1), which is True

# Counting occurrences of a value in the tuple
print(my_tuple.count(3))  # Counts how many times 3 appears in the tuple, which is 1
print(my_tuple.count("hello"))  # Counts how many times "hello" appears, which is 1

# Finding the index of a value in the tuple
print(my_tuple.index("hello"))  # Finds the index of the first occurrence of "hello", which is 3
print(my_tuple.index(True))  # Finds the index of the first occurrence of True, which is 4

# Slicing the tuple to get a subset
print(my_tuple[1:4])  # Slices from index 1 to 3 (exclusive), resulting in (2, 3, 'hello')
print(my_tuple[:3])  # Slices from the start to index 2 (exclusive), resulting in (1, 2, 3)
print(my_tuple[::2])  # Slices with step 2, resulting in (1, 3, True)

# Re-assigning the entire tuple (since tuples are immutable, you can't modify elements, but you can replace the whole tuple)
my_tuple = (4, 5, 6, "new", False)  # Re-assigns my_tuple to a new tuple
print("Re-assigned tuple:", my_tuple)

## Set in python
print("-----Topic: Set-----")
# A set is an unordered collection of unique elements in Python. It automatically removes duplicates and does not support indexing or slicing due to its unordered nature. Sets are mutable, meaning you can add or remove elements, but elements must be immutable (e.g., no lists inside sets). They are defined using curly braces {} or the set() function and are useful for membership testing, eliminating duplicates, and performing mathematical set operations like union, intersection, and difference.

# Example: Creating a set with mixed types (duplicates are ignored)
my_set = {1, 2, 3, "hello", True, 2}  # Note: 2 is duplicated, but set will have only one
print("Value of my_set:", my_set)
print("Type of my_set:", type(my_set))

# Sets use curly braces {}, are mutable (add/remove elements), unordered (no indexing), and do not allow duplicates.
# Allowed actions on sets:
# - Access by index: No (unordered)
# - Count values: No (duplicates not allowed)
# - Find index: No (unordered)
# - Slice values: No (unordered)
# - Re-assign entire Set: Yes

# Manipulations and examples:
# Adding elements
my_set.add(4)  # Adds 4 if not already present
print("After adding 4:", my_set)

# Removing elements
my_set.remove(2)  # Removes 2; raises KeyError if not found
print("After removing 2:", my_set)

my_set.discard(5)  # Removes 5 if present, no error if not
print("After discarding 5:", my_set)

# Checking membership
print("Is 'hello' in my_set?", "hello" in my_set)  # True

# Set operations (uses):
# Union: Combine elements from two sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Union of set_a and set_b:", set_a | set_b)  # {1, 2, 3, 4, 5}

# Intersection: Common elements
print("Intersection of set_a and set_b:", set_a & set_b)  # {3}

# Difference: Elements in set_a but not in set_b
print("Difference set_a - set_b:", set_a - set_b)  # {1, 2}

# Uses: Removing duplicates from a list
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)
print("Unique elements from list:", unique_set)  # {1, 2, 3, 4, 5}


# Dictionary
print("-----Topic: Dictionary-----")
