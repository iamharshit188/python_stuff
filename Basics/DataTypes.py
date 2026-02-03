print("Printing something")

print("----- Topic: Integer datatypes -----")
# Integer datatypes
print("Subtopic: Integer")
# Integer
a = 10
print("Value of a:", a)
print("Type of a:", type(a))
# Type of tells the type of a variable

print("Subtopic: Float")
# Float
b = 20.5
print("Value of b:", b)
print("Type of b:", type(b))

print("----- Topic: List, tuple, range -----")
# List, tuple, range
list1 = [1, 2, 3, 4, 5]
print("Value of list1:", list1)
print("Type of list1:", type(list1))

tuple1 = (10, 20, 30, 40)
print("Value of tuple1:", tuple1)
print("Type of tuple1:", type(tuple1))

# Lists are mutable (values can be changed), whereas tuples are immutable (values cannot be changed)
# Range is used to generate a sequence of numbers: range(start, stop, step)
# By default start is 0 and step is 1. Stop is exclusive.
range1 = range(0, 10, 2)
print("Value of range1:", list(range1))
print("Type of range1:", type(range1))

# Where are range list and tuple used? With real life examples?
# Lists are used when we need a collection of items that may change, such as a list of students in a class.
# Tuples are used when we need a collection of items that should not change, such as the coordinates of a point in 2D space.
# Ranges are used in loops to iterate over a sequence of numbers, such as iterating over the indices of a list.
print("-----String and Binary Datatypes-----")
print("Subtopic: String")
# String
str1 = "Hello, World!"
print("Value of str1:", str1)
print("Type of str1:", type(str1))

print("----- Topic: Binary datatype -----")
# Binary datatype
print("Subtopic: Bytes and bytearray")
# Bytes and bytearray
bytes1 = b"Hello"
print("Value of bytes1:", bytes1)
print("Type of bytes1:", type(bytes1))
bytearray1 = bytearray(5)
print("Value of bytearray1:", bytearray1)
print("Type of bytearray1:", type(bytearray1))
# Bytes are immutable sequences of bytes, whereas bytearrays are mutable sequences of bytes.
# These are used in scenarios where we need to handle binary data, such as reading from or writing to files, or working with network protocols.