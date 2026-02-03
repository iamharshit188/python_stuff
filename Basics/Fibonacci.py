# Implementation of Fibonacci sequence in Python
# What is Fibonacci sequence?
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding
# numbers. The sequence typically starts with 0 and 1. Thus, the sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.
# The Fibonacci sequence has applications in computer science, mathematics, and nature.


# RAM Efficient one
import sys
import time

# Increase string conversion limit for printing huge numbers
try:
    sys.set_int_max_str_digits(2000000)
except AttributeError:
    pass

def fib_fast(n):
    """
    Calculates F(n) using Fast Doubling.
    Complexity: O(log n) arithmetic operations.
    Memory: O(1) - only stores a few large integers at a time.
    """
    if n == 0:
        return 0, 1
    else:
        # Recursively calculate F(n//2)
        a, b = fib_fast(n // 2)
        
        # Apply doubling formulas
        c = a * (2 * b - a)
        d = a * a + b * b
        
        if n % 2 == 0:
            return c, d
        else:
            return d, c + d

target_index = 8726305056

print(f"Calculating Fibonacci of {target_index}...")
start_time = time.time()

# We only want the first return value (F_n)
result, _ = fib_fast(target_index)

end_time = time.time()
print(f"Calculation done in {end_time - start_time:.4f} seconds.")

# Convert to string to check size (this is the only RAM-heavy part, ~1MB)
str_res = str(result)
print(f"Digits: {len(str_res)}")
print(f"RAM is safe. First 20 digits: {str_res[:]}")


# ---- Simple one -----

def fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence
# Example usage
num_terms = 4802012
print(f"Fibonacci sequence with {num_terms} terms:")
print(fibonacci(num_terms))
