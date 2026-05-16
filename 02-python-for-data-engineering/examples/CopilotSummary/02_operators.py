"""
02_operators.py
===============
Python Operators: Arithmetic, Relational, Logical, Assignment

Topics Covered:
- Assignment operators (=, +=, -=, *=, /=, etc.)
- Arithmetic operators (+, -, *, /, %, **, //)
- Relational/Comparison operators (==, !=, <, >, <=, >=)
- Logical operators (and, or, not)
- Operator precedence (BODMAS/PEMDAS)
"""

print("=" * 70)
print("2. OPERATORS IN PYTHON")
print("=" * 70)

# ========================================
# A. ASSIGNMENT OPERATORS
# ========================================
print("\n[A] Assignment Operators")
print("-" * 70)

# Basic assignment
x = 50
print(f"x = 50 -> x = {x}")

# Augmented assignment (shorthand)
x += 10  # x = x + 10
print(f"x += 10 -> x = {x}")

x -= 5  # x = x - 5
print(f"x -= 5 -> x = {x}")

x *= 2  # x = x * 2
print(f"x *= 2 -> x = {x}")

x /= 2  # x = x / 2
print(f"x /= 2 -> x = {x}")

x %= 10  # x = x % 10
print(f"x %= 10 -> x = {x}")

x **= 2  # x = x ** 2
print(f"x **= 2 -> x = {x}")

x //= 3  # x = x // 3
print(f"x //= 3 -> x = {x}")

# ========================================
# B. ARITHMETIC OPERATORS
# ========================================
print("\n[B] Arithmetic Operators")
print("-" * 70)

num1 = 100
num2 = 25

# Addition
result = num1 + num2
print(f"Addition: {num1} + {num2} = {result}")

# Subtraction
result = num1 - num2
print(f"Subtraction: {num1} - {num2} = {result}")

# Multiplication
result = num1 * num2
print(f"Multiplication: {num1} * {num2} = {result}")

# Division (returns float)
result = num1 / num2
print(f"Division: {num1} / {num2} = {result}")

# Floor Division (returns integer)
result = num1 // num2
print(f"Floor Division: {num1} // {num2} = {result}")

# Modulo (remainder)
remainder = num1 % num2
print(f"Modulo: {num1} % {num2} = {remainder}")
print(f"  (Used for: partitioning, sharding, bucketing, even/odd checks)")

# Exponent (power)
result = 2 ** 3  # 2 * 2 * 2 = 8
print(f"Exponent: 2 ** 3 = {result}")

# Real-world example: Salary with bonus percentage
print("\nReal-World Example: Salary Calculation with Bonus")
print("-" * 70)
employee_name = "Alice"
salary = 50000
bonus_percentage = 15

bonus_amount = salary * bonus_percentage / 100
total_salary = salary + bonus_amount

print(f"Employee: {employee_name}")
print(f"Base Salary: ${salary:,.2f}")
print(f"Bonus ({bonus_percentage}%): ${bonus_amount:,.2f}")
print(f"Total Salary: ${total_salary:,.2f}")

# ========================================
# C. RELATIONAL / COMPARISON OPERATORS
# ========================================
print("\n[C] Relational/Comparison Operators")
print("-" * 70)
"""
Compare two values and return boolean (True/False)
Used in conditional statements (if, while, etc.)
"""

num1 = 100
num2 = 50

# Equal to (==)
print(f"{num1} == {num2}: {num1 == num2}")  # False
print(f"{num1} == {num1}: {num1 == num1}")  # True

# Not equal to (!=)
print(f"{num1} != {num2}: {num1 != num2}")  # True
print(f"{num1} != {num1}: {num1 != num1}")  # False

# Less than (<)
print(f"{num1} < {num2}: {num1 < num2}")  # False
print(f"{num2} < {num1}: {num2 < num1}")  # True

# Greater than (>)
print(f"{num1} > {num2}: {num1 > num2}")  # True
print(f"{num2} > {num1}: {num2 > num1}")  # False

# Less than or equal (<=)
print(f"{num1} <= {num2}: {num1 <= num2}")  # False
print(f"{num1} <= {num1}: {num1 <= num1}")  # True

# Greater than or equal (>=)
print(f"{num1} >= {num2}: {num1 >= num2}")  # True
print(f"{num1} >= {num1}: {num1 >= num1}")  # True

# ========================================
# D. LOGICAL OPERATORS
# ========================================
print("\n[D] Logical Operators")
print("-" * 70)
"""
Combine multiple conditions to reduce complexity.
- and: Both conditions must be True
- or: At least one condition must be True
- not: Reverses the boolean value
"""

age = 25
salary = 60000
avg_salary = 50000
is_active = True

print("Condition 1: age > 20 ->", age > 20)
print("Condition 2: salary > avg_salary ->", salary > avg_salary)

# AND operator
print(f"\nAND Operator:")
result_and = (age > 20) and (salary > avg_salary)
print(f"(age > 20) and (salary > {avg_salary}): {result_and}")  # True

result_and = (age > 30) and (salary > avg_salary)
print(f"(age > 30) and (salary > {avg_salary}): {result_and}")  # False

# OR operator
print(f"\nOR Operator:")
result_or = (age > 30) or (salary > avg_salary)
print(f"(age > 30) or (salary > {avg_salary}): {result_or}")  # True

result_or = (age > 30) or (salary < avg_salary)
print(f"(age > 30) or (salary < {avg_salary}): {result_or}")  # False

# NOT operator
print(f"\nNOT Operator:")
print(f"is_active: {is_active}")
print(f"not is_active: {not is_active}")  # False

# Real-world example: Employee eligibility
print("\nReal-World Example: Employee Eligibility Check")
print("-" * 70)

age = 28
experience_years = 5
has_required_cert = True

eligible = (age >= 25) and (experience_years >= 3) and (has_required_cert)
print(f"Age: {age}, Experience: {experience_years} years, Certification: {has_required_cert}")
print(f"Eligible for promotion: {eligible}")

# ========================================
# E. OPERATOR PRECEDENCE (PEMDAS/B0DMAS)
# ========================================
print("\n[E] Operator Precedence (PEMDAS/BODMAS)")
print("-" * 70)
"""
Parentheses/Brackets
Exponents/Orders
Multiplication & Division (left to right)
Addition & Subtraction (left to right)
"""

# Without precedence awareness
result1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {result1}")  # 14 (mult before add)

# With explicit parentheses
result2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result2}")  # 20

# Complex expression
result3 = 10 + 5 * 2 - 3 / 1 ** 2
print(f"10 + 5 * 2 - 3 / 1 ** 2 = {result3}")

# Real-world: Discount calculation
print("\nReal-World Example: Discount Calculation")
print("-" * 70)

original_price = 1000
discount_percent = 20
tax_percent = 5

# Calculate final price: (original - discount) + tax
discount_amount = original_price * discount_percent / 100
price_after_discount = original_price - discount_amount
tax_amount = price_after_discount * tax_percent / 100
final_price = price_after_discount + tax_amount

print(f"Original Price: ${original_price}")
print(f"Discount ({discount_percent}%): ${discount_amount}")
print(f"Price after discount: ${price_after_discount}")
print(f"Tax ({tax_percent}%): ${tax_amount:.2f}")
print(f"Final Price: ${final_price:.2f}")

print("\n" + "=" * 70)
print("END OF OPERATORS MODULE")
print("=" * 70)

