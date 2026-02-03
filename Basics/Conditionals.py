# Conditionals in python are used to perform different actions based on whether a certain condition is true or false. The primary conditional statements in Python are `if`, `elif`, and `else`. Here's a brief overview of how they work:
print("----- Topic: Conditionals -----")
# If statement
age = 18
if age >= 18:
    print("You are an adult.")
    
# Elif statement
# Elif (else if) allows you to check multiple conditions.
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")   
    
# Switch case
# Python does not have a built-in switch case statement like some other languages, but you can achieve similar functionality using dictionaries.
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
print("Day 3 is:", switch_case_example(3))
print("Day 8 is:", switch_case_example(8))  # Invalid day

# Nested conditionals
# You can also nest conditional statements within each other.
num = 10
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")

    