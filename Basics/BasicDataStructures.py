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