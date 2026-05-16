"""
04_loops.py
===========
Looping Constructs: for, while, break, continue, range()

Topics Covered:
- for loops (unconditional, fixed iterations)
- while loops (conditional, variable iterations)
- range() function
- break statement (exit loop early)
- continue statement (skip to next iteration)
- Nested loops
- for-else, while-else
"""

print("=" * 70)
print("4. LOOPING CONSTRUCTS")
print("=" * 70)

# ========================================
# A. FOR LOOP BASICS
# ========================================
print("\n[A] FOR Loop - Iterating Over Iterables")
print("-" * 70)
"""
Syntax:
for variable in iterable:
    statement(s)

FOR loop iterates over: strings, lists, tuples, dicts, sets, range()
Number of iterations is known/fixed
"""

# Example 1: Iterate over string
print("Iterate over string 'hello':")
for char in "hello":
    print(char, end=" ")
print()

# Example 2: Iterate over list
print("\nIterate over list:")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"  - {fruit}")

# Example 3: Iterate using enumerate (get index + value)
print("\nUsing enumerate() to get index and value:")
for index, fruit in enumerate(fruits):
    print(f"  Index {index}: {fruit}")

# ========================================
# B. RANGE() FUNCTION
# ========================================
print("\n[B] RANGE() Function - Generate Sequences")
print("-" * 70)
"""
range(stop)              -> 0 to stop-1
range(start, stop)       -> start to stop-1
range(start, stop, step) -> start to stop-1, increment by step

Returns range object (iterable), not list
"""

# range(stop)
print("range(5) - prints 0 to 4:")
for i in range(5):
    print(i, end=" ")
print()

# range(start, stop)
print("\nrange(2, 7) - prints 2 to 6:")
for i in range(2, 7):
    print(i, end=" ")
print()

# range(start, stop, step)
print("\nrange(0, 10, 2) - prints 0, 2, 4, 6, 8:")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# Reverse range
print("\nrange(10, 0, -1) - prints 10 down to 1:")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# ========================================
# C. NESTED FOR LOOPS
# ========================================
print("\n[C] Nested FOR Loops")
print("-" * 70)

# Multiplication table
print("Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end=" | ")
    print()  # New line after inner loop

# Pattern printing
print("\nPattern printing:")
for row in range(1, 4):
    for col in range(row):
        print("*", end=" ")
    print()

# ========================================
# D. WHILE LOOP BASICS
# ========================================
print("\n[D] WHILE Loop - Conditional Looping")
print("-" * 70)
"""
Syntax:
while condition:
    statement(s)
    
WHILE loop continues as long as condition is True
Number of iterations is unknown/variable
Entry-controlled (checks condition before entering)
"""

# Count from 1 to 5
print("Count from 1 to 5 using while:")
counter = 1
while counter <= 5:
    print(counter, end=" ")
    counter += 1
print()

# Read input until valid
print("\nRead input until negative (simulated):")
numbers = [5, 3, 8, -1, 2]
index = 0
while index < len(numbers):
    num = numbers[index]
    if num < 0:
        break
    print(f"Number {index}: {num}")
    index += 1

# ========================================
# E. BREAK STATEMENT
# ========================================
print("\n[E] BREAK Statement - Exit Loop Early")
print("-" * 70)
"""
break: Terminates the current loop and exits
Works with both for and while loops
"""

# Break in for loop
print("Find first even number in list:")
numbers = [1, 3, 5, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"Found even number: {num}")
        break
    print(f"  Checking {num} (odd)")

# Break in while loop
print("\nSearch for target in list (using while):")
items = ['apple', 'banana', 'cherry', 'date', 'elderberry']
target = 'cherry'
index = 0
found = False

while index < len(items):
    if items[index] == target:
        print(f"Found '{target}' at index {index}")
        found = True
        break
    index += 1

if not found:
    print(f"'{target}' not found")

# ========================================
# F. CONTINUE STATEMENT
# ========================================
print("\n[F] CONTINUE Statement - Skip to Next Iteration")
print("-" * 70)
"""
continue: Skips current iteration and moves to next
Works with both for and while loops
"""

# Skip odd numbers
print("Print only even numbers (using continue):")
for num in range(1, 11):
    if num % 2 != 0:  # If odd
        continue  # Skip to next iteration
    print(num, end=" ")
print()

# Skip certain days
print("\nSkip Saturdays and Sundays:")
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
for day in days:
    if day in ['Sat', 'Sun']:
        continue
    print(day, end=" ")
print()

# ========================================
# G. BREAK + CONTINUE COMBINATIONS
# ========================================
print("\n[G] BREAK and CONTINUE Together")
print("-" * 70)

print("Process numbers: skip multiples of 3, stop at 30:")
num = 0
while num < 50:
    num += 1
    if num % 3 == 0:  # Skip multiples of 3
        continue
    if num > 30:     # Stop at 30
        break
    print(num, end=" ")
print()

# ========================================
# H. FOR-ELSE AND WHILE-ELSE
# ========================================
print("\n[H] FOR-ELSE and WHILE-ELSE")
print("-" * 70)
"""
else block executes when loop completes normally
(without break statement)
Does NOT execute if break is used
"""

# for-else: Normal completion
print("for-else (normal completion):")
for i in range(1, 4):
    print(i, end=" ")
else:
    print("Loop completed normally")

# for-else: With break (else won't execute)
print("\nfor-else (with break):")
for i in range(1, 10):
    if i == 5:
        print(f"Found 5, breaking...")
        break
    print(i, end=" ")
else:
    print("This won't print")

# while-else
print("\nwhile-else (normal completion):")
count = 1
while count <= 3:
    print(count, end=" ")
    count += 1
else:
    print("While completed normally")

# ========================================
# I. REAL-WORLD EXAMPLES
# ========================================
print("\n[I] Real-World Examples")
print("-" * 70)

# Example 1: Process list of salaries
print("Calculate average salary (skip zero values):")
salaries = [50000, 0, 60000, 75000, 0, 55000]
total = 0
count = 0

for salary in salaries:
    if salary == 0:
        continue
    total += salary
    count += 1

average = total / count if count > 0 else 0
print(f"  Salaries: {salaries}")
print(f"  Average: ${average:,.2f} (excluded {len(salaries)-count} zero values)")

# Example 2: Search in list
print("\nFind first employee with salary > 60000:")
employees = [
    {"name": "Alice", "salary": 55000},
    {"name": "Bob", "salary": 65000},
    {"name": "Charlie", "salary": 50000}
]

for emp in employees:
    if emp["salary"] > 60000:
        print(f"  Found: {emp['name']} with salary ${emp['salary']}")
        break
else:
    print("  No employee with salary > 60000")

# Example 3: Multiplication table generator
print("\nMultiplication Tables (1-3):")
for table_num in range(1, 4):
    print(f"Table of {table_num}:")
    for multiplier in range(1, 6):
        product = table_num * multiplier
        print(f"  {table_num} x {multiplier} = {product}")

print("\n" + "=" * 70)
print("END OF LOOPS MODULE")
print("=" * 70)

