# Operator and Expression in python 
# An operator is a special symbol that performs a specific operation on one or more operands (values or variables) and produces a result.
# An expression is a combination of operators and operands that can be evaluated to produce a value.
#
print("----- Topic: Operators and Expressions -----")
# Arithmetic Operators
# These operators perform mathematical operations on numeric operands.
a = 10
b = 3
print("Arithmetic Operators:")
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division
print("a % b =", a % b)  # Modulus
print("a ** b =", a ** b)  # Exponentiation
print("a // b =", a // b)  # Floor Division

# Comparison Operators
# These operators compare two values and return a boolean result (True or False).
print("\n------Comparison Operators:------")
print("a == b:", a == b)  # Equal to
print("a != b:", a != b)  # Not equal to
print("a > b:", a > b)    # Greater than
print("a < b:", a < b)    # Less than
print("a >= b:", a >= b)  # Greater than or equal to
print("a <= b:", a <= b)  # Less than or equal to

# Logical Operators
# These operators are used to combine multiple boolean expressions.
x = True
y = False
print("\n------Logical Operators:------")
print("x and y:", x and y)  # Logical AND
print("x or y:", x or y)    # Logical OR
print("not x:", not x)      # Logical NOT
# These operators are commonly used in conditional statements and loops to control the flow of execution based on multiple conditions.

# Assignment Operators
# These operators are used to assign values to variables.
print("\n------Assignment Operators:------")
c = 5
print("Initial value of c:", c)
c += 2  # Equivalent to c = c + 2
print("After c += 2, c =", c)
c *= 3  # Equivalent to c = c * 3
print("After c *= 3, c =", c)
# Assignment operators are used to simplify the process of updating variable values.

# Bitwise Operators
# These operators perform operations on the binary representations of integers.
# They are used in low-level programming, such as systems programming and embedded systems.
# For example, they can be used for setting, clearing, and toggling specific bits in a binary number.
print("\n------Bitwise Operators:------")
p = 5  # Binary: 0101
q = 3  # Binary: 0011
print("p & q =", p & q)  # Bitwise AND
print("p | q =", p | q)  # Bitwise OR
print("p ^ q =", p ^ q)  # Bitwise XOR
print("~p =", ~p)        # Bitwise NOT
print("p << 1 =", p << 1)  # Left Shift
print("p >> 1 =", p >> 1)  # Right Shift   

# Membership Operators
# These operators are used to test whether a value is present in a sequence (like a list, tuple, or string).
# They return a boolean result (True or False).
# Membership operators are commonly used in conditional statements to check for the presence of an element in a collection.
print("\n------Membership Operators:------")
a = [1, 2, 3, 4, 5]
print("3 in a:", 3 in a)      # True
print("6 not in a:", 6 not in a)  # True

# Identity Operators
print("\n------Identity Operators:------")

# These operators are used to compare the memory locations of two objects.
# They return a boolean result (True or False).
# Identity operators are used to check if two variables refer to the same object in memory.
# This is particularly useful when dealing with mutable objects, where two variables may have the same value but refer to different objects.
x = ["apple", "banana"]
y = x
z = ["apple", "banana"]
print("x is y:", x is y)      # True
print("x is z:", x is z)      # False
print("x is not z:", x is not z)  # True
