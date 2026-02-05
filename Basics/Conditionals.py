# Conditionals in python are used to perform different actions based on whether a certain condition is true or false.
# The primary conditional statements in Python are `if`, `elif`, and `else`. Here's a brief overview of how they work:
print("\n----- Topic: Conditionals -----\n")

# If statement
print(">>> If statement example")
age = 18
print(f"Input: age = {age}")
if age >= 18:
    print("Output: You are an adult.")
print()  # blank line for readability

# ------------------
# Important Question related to TRUE and FALSE
print(">>> Logical AND example (age > 18 and age < 60)")
age = 25
print(f"Input: age = {age}")
if age > 18 and age < 60:
    print("Output: Valid")
else:
    print("Output: Not Valid")
print()

# ------------------

# Elif statement
# Elif (else if) allows you to check multiple conditions.
print(">>> Elif (multiple-branch) example - Grade evaluation")
score = 85
print(f"Input: score = {score}")
if score >= 90:
    print("Output: Grade: A")
elif score >= 80:
    print("Output: Grade: B")
elif score >= 70:
    print("Output: Grade: C")
else:
    print("Output: Grade: F")
print()

# Switch case
# Python does not have a built-in switch case statement like some other languages,
# but you can achieve similar functionality using dictionaries.
# Here's an example:
def switch_case_example(day):
    switcher = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return switcher.get(day, "Invalid day")

print(">>> Switch-case (dict) example - Day lookup")
print(f"Input: day = 3 -> Output: {switch_case_example(3)}")
print(f"Input: day = 8 -> Output: {switch_case_example(8)}")  # Invalid day
print()

# Nested conditionals
# You can also nest conditional statements within each other.
print(">>> Nested conditionals example")
num = 10
print(f"Input: num = {num}")
if num > 0:
    if num % 2 == 0:
        print("Output: The number is positive and even.")
    else:
        print("Output: The number is positive and odd.")
else:
    print("Output: The number is not positive.")
print()