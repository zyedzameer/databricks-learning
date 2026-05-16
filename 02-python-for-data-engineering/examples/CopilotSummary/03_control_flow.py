"""
03_control_flow.py
==================
Control Flow: if, elif, else, Nested Conditionals

Topics Covered:
- if statement (simple conditional)
- if-else statement (two-way branching)
- if-elif-else statement (multi-way branching)
- Nested conditionals
- Ternary operator (conditional expression)
"""

print("=" * 70)
print("3. CONTROL FLOW - CONDITIONAL STATEMENTS")
print("=" * 70)

# ========================================
# A. SIMPLE IF STATEMENT
# ========================================
print("\n[A] Simple IF Statement")
print("-" * 70)
"""
Syntax:
if condition:
    statement(s) if condition is True
"""

age = 18

if age >= 18:
    print(f"Age {age}: You are an adult")

# Only executes if condition is True
if age < 13:
    print("This won't print")

print("Code continues after if block")

# ========================================
# B. IF-ELSE STATEMENT
# ========================================
print("\n[B] IF-ELSE Statement")
print("-" * 70)
"""
Syntax:
if condition:
    statement(s) if True
else:
    statement(s) if False
"""

score = 75

if score >= 60:
    print(f"Score {score}: PASS")
else:
    print(f"Score {score}: FAIL")

# Real-world example
salary = 35000
tax_rate = 0.10

if salary > 50000:
    tax_rate = 0.20
else:
    tax_rate = 0.10

tax_amount = salary * tax_rate
print(f"Salary: ${salary}, Tax Rate: {tax_rate*100}%, Tax: ${tax_amount}")

# ========================================
# C. IF-ELIF-ELSE STATEMENT
# ========================================
print("\n[C] IF-ELIF-ELSE Statement")
print("-" * 70)
"""
Multiple conditions can be tested.
First True condition executes, rest skipped.
else is optional.
"""

age = 65

if age < 13:
    category = "Child"
elif age < 18:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior Citizen"

print(f"Age {age}: {category}")

# Grade assignment example
print("\nGrade Assignment Example:")
print("-" * 70)

marks = 87

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Marks: {marks}, Grade: {grade}")

# ========================================
# D. NESTED CONDITIONALS
# ========================================
print("\n[D] Nested Conditionals")
print("-" * 70)
"""
Conditionals within conditionals.
Use when you need to check multiple layers of conditions.
"""

print("Ticket Booking System Example:")
print("-" * 70)

age = 25
has_student_id = False
ticket_type = "regular"

price = 0

if age < 5:
    price = 0
    print("Child: FREE ticket")
elif age < 18:
    if has_student_id:
        price = 5
        ticket_type = "student_discount"
        print(f"Student: ${price} (with discount)")
    else:
        price = 8
        ticket_type = "regular"
        print(f"Minor: ${price} (regular)")
else:
    if has_student_id:
        price = 10
        ticket_type = "student_discount"
        print(f"Adult (Student): ${price} (with discount)")
    else:
        price = 15
        ticket_type = "regular"
        print(f"Adult: ${price} (regular)")

print(f"Final Price: ${price}")

# ========================================
# E. COMPLEX CONDITIONS
# ========================================
print("\n[E] Complex Conditions with AND/OR")
print("-" * 70)

print("Loan Eligibility Check:")
print("-" * 70)

age = 28
salary = 60000
credit_score = 720
employment_years = 5

eligible_for_loan = (
    (age >= 21) and
    (salary >= 30000) and
    (credit_score >= 700) and
    (employment_years >= 2)
)

print(f"Age: {age}, Salary: ${salary}, Credit Score: {credit_score}, "
      f"Employment: {employment_years} years")
print(f"Eligible for loan: {eligible_for_loan}")

# ========================================
# F. COMPOUND CONDITIONS WITH OR
# ========================================
print("\n[F] Compound Conditions with OR")
print("-" * 70)

print("Special Discount Check:")
print("-" * 70)

age = 65
is_student = False
is_government_employee = True

eligible_for_discount = (age >= 60) or (is_student) or (is_government_employee)

print(f"Age: {age}, Student: {is_student}, Govt Employee: {is_government_employee}")
print(f"Eligible for discount: {eligible_for_discount}")

# ========================================
# G. CONDITIONAL USING FUNCTIONS
# ========================================
print("\n[G] Conditional Logic in Functions")
print("-" * 70)

def check_number_type(num):
    """Check if number is positive, negative, or zero"""
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(f"10 is: {check_number_type(10)}")
print(f"-5 is: {check_number_type(-5)}")
print(f"0 is: {check_number_type(0)}")

# ========================================
# H. GREATEST OF THREE NUMBERS
# ========================================
print("\n[H] Comparison: Greatest of Three Numbers")
print("-" * 70)

num1 = 100
num2 = 250
num3 = 150

# Method 1: Using if-elif-else
if num1 > num2 and num1 > num3:
    greatest = num1
elif num2 > num3:
    greatest = num2
else:
    greatest = num3

print(f"Method 1 (if-elif-else): {num1}, {num2}, {num3} -> Greatest: {greatest}")

# Method 2: Using built-in max()
greatest = max(num1, num2, num3)
print(f"Method 2 (built-in max()): {num1}, {num2}, {num3} -> Greatest: {greatest}")

# ========================================
# I. TERNARY OPERATOR (CONDITIONAL EXPRESSION)
# ========================================
print("\n[I] Ternary Operator (Conditional Expression)")
print("-" * 70)
"""
Syntax: value_if_true if condition else value_if_false
One-liner alternative to if-else
"""

age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age {age}: {status}")

score = 75
result = "Pass" if score >= 60 else "Fail"
print(f"Score {score}: {result}")

# Chained ternary (not recommended for readability)
marks = 85
grade = "A" if marks >= 90 else "B" if marks >= 80 else "C" if marks >= 70 else "D"
print(f"Marks {marks}: Grade {grade}")

# ========================================
# J. REAL-WORLD EXAMPLES
# ========================================
print("\n[J] Real-World Examples")
print("-" * 70)

# Example 1: Employee Leave Eligibility
print("Employee Leave Eligibility:")
days_worked = 200
department = "IT"

if days_worked >= 365:
    annual_leave = 20
    if department == "IT":
        annual_leave += 3  # IT gets 3 extra days
elif days_worked >= 180:
    annual_leave = 10
else:
    annual_leave = 0

print(f"Days worked: {days_worked}, Department: {department}")
print(f"Annual leave entitled: {annual_leave} days")

# Example 2: Temperature-based Activity
print("\nTemperature-based Activity Suggestion:")
temp = 28

if temp < 0:
    activity = "Stay indoors (snowing)"
elif temp < 10:
    activity = "Wear jacket (cold)"
elif temp < 20:
    activity = "Light jacket (cool)"
elif temp < 25:
    activity = "Light clothing (pleasant)"
else:
    activity = "Light clothing or shorts (hot)"

print(f"Temperature: {temp}°C -> {activity}")

print("\n" + "=" * 70)
print("END OF CONTROL FLOW MODULE")
print("=" * 70)

