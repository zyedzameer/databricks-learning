"""
01_basics.py
============
Python Programming Fundamentals: Indent, Comments, Variables, Types, Casting

Topics Covered:
- Python is indent-based (essential for code organization and readability)
- Variables: dynamic typing, dynamic inference, strongly typed
- Data types: int, float, str, bool, None, bytes
- Type casting: int(), float(), str(), bool()
- Variable naming conventions: snake_case, camelCase, CONSTANT_CASE
- Multiple assignment in single line
- Quotes and escape sequences
"""

print("=" * 70)
print("1. PYTHON FUNDAMENTALS")
print("=" * 70)

# ========================================
# A. INDENT-BASED PROGRAMMING LANGUAGE
# ========================================
print("\n[A] Python is Indent-Based")
print("-" * 70)
print("""
Python uses indentation (typically 4 spaces) to define code blocks.
This enforces code readability and hierarchy.
""")

# FOR LOOP requires indentation
fruit = "apple"
for c in fruit:
    print(c)  # This is indented block for the for loop

print("Outside the for loop")

# ========================================
# B. COMMENTS
# ========================================
print("\n[B] Comments in Python")
print("-" * 70)

# Single-line comment using #
x = 10

"""
Multi-line comments using triple quotes
Can span multiple lines
Useful for docstrings and block comments
"""

# ========================================
# C. QUOTES & ESCAPE SEQUENCES
# ========================================
print("\n[C] Quotes & Escape Sequences")
print("-" * 70)

# Single quotes
name1 = 'Alice'

# Double quotes (useful when string contains single quotes)
company = "Inceptez Tech's"

# Triple quotes (for multi-line strings)
sql_query = """
SELECT * 
FROM employees 
WHERE dept = 'IT'
"""

# Escape sequences
escaped_quote = 'Inceptez Tech\'s'  # Escaping single quote
new_line_str = "Line1\nLine2"  # Newline
tab_str = "Name\tAge\tCity"  # Tab

print(f"Single quote: {name1}")
print(f"With apostrophe: {company}")
print(f"Triple quoted:\n{sql_query}")
print(f"Escaped quote: {escaped_quote}")

# ========================================
# D. VARIABLES & VALUES
# ========================================
print("\n[D] Variables & Values")
print("-" * 70)

# Variable: named container to hold value in memory
# Dynamic inference: Python infers type from assigned value
name = "Python"  # str type (inferred)
age = 30  # int type (inferred)
price = 99.99  # float type (inferred)

print(f"Name: {name} (type: {type(name).__name__})")
print(f"Age: {age} (type: {type(age).__name__})")
print(f"Price: {price} (type: {type(price).__name__})")

# Type hints (for reference, Python doesn't enforce)
count: int = 100
salary: float = 50000.50
is_active: bool = True

# ========================================
# E. DYNAMIC TYPING & STRONGLY TYPED
# ========================================
print("\n[E] Dynamic Typing vs Strongly Typed")
print("-" * 70)

"""
DYNAMIC: A variable can change type after assignment
STRONGLY TYPED: Python enforces type compatibility in operations
"""

# Dynamic typing example
value = 100  # int
print(f"value = {value} (type: {type(value).__name__})")

value = "Hello"  # Same variable, now string
print(f"value = {value} (type: {type(value).__name__})")

# Strongly typed - operations must match types
num1 = 100
num2 = 50
result = num1 + num2  # Both int, works fine
print(f"100 + 50 = {result}")

# This will fail:
# result = 100 + "50"  # int + str -> TypeError

# Must cast to compatible types
num_str = "50"
# result = num1 + int(num_str)  # Now works
print(f"100 + int('50') = {num1 + int(num_str)}")

# ========================================
# F. DATA TYPES - SIMPLE/PRIMITIVE
# ========================================
print("\n[F] Data Types - Simple/Primitive")
print("-" * 70)

# Numeric types
int_val = 100
float_val = 99.99
complex_val = 5 + 3j

print(f"int: {int_val} -> {type(int_val)}")
print(f"float: {float_val} -> {type(float_val)}")
print(f"complex: {complex_val} -> {type(complex_val)}")

# String type (sequence of characters)
str_val = "DataEngineering"
print(f"str: {str_val} -> {type(str_val)}")
print(f"First char: {str_val[0]}, Length: {len(str_val)}")

# Boolean type (True/False)
is_true = True
is_false = False
print(f"bool: {is_true} -> {type(is_true)}")

# Exponential notation (floating-point)
exp_val = 3e2  # 3 * 10^2 = 300.0
print(f"exponential: {exp_val} (type: {type(exp_val).__name__})")

# None type (null/nothing)
empty_value = None
print(f"None: {empty_value} (type: {type(empty_value).__name__})")

# ========================================
# G. NAMING CONVENTIONS
# ========================================
print("\n[G] Naming Conventions")
print("-" * 70)

# snake_case (recommended for variables/functions in Python)
first_name = "Alice"
employee_age = 28
total_salary = 50000

# camelCase (sometimes used)
firstName = "Bob"

# PascalCase (used for class names)
class PersonData:
    pass

# CONSTANT_CASE (used for constants)
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 300

# Rules for variable names:
# 1. Must start with letter or underscore (_)
# 2. Can contain alphanumeric and underscore (A-z, 0-9, _)
# 3. Case-sensitive (Name != name)
# 4. Cannot be Python keywords

_private_var = "starts with underscore"
var_123 = "contains numbers"

print(f"snake_case example: {first_name}")
print(f"camelCase example: {firstName}")
print(f"CONSTANT_CASE example: MAX_RETRIES = {MAX_RETRIES}")

# ========================================
# H. TYPE CASTING
# ========================================
print("\n[H] Type Casting")
print("-" * 70)

"""
Convert value from one type to another using:
- int() -> convert to integer
- float() -> convert to float
- str() -> convert to string
- bool() -> convert to boolean
- list(), tuple(), set(), dict() -> convert to collection types
"""

# String to int
str_num = "123"
int_from_str = int(str_num)
print(f"'{str_num}' (str) -> {int_from_str} (int)")

# Float to int (truncates decimal)
float_num = 99.99
int_from_float = int(float_num)
print(f"{float_num} (float) -> {int_from_float} (int)")

# String to float
price_str = "199.99"
price_float = float(price_str)
print(f"'{price_str}' (str) -> {price_float} (float)")

# Int to string
num = 100
str_from_num = str(num)
print(f"{num} (int) -> '{str_from_num}' (str)")

# String to bool
bool_str1 = bool("Hello")  # Non-empty string = True
bool_str2 = bool("")  # Empty string = False
bool_num1 = bool(1)  # Non-zero = True
bool_num2 = bool(0)  # Zero = False
print(f"bool('Hello') = {bool_str1}")
print(f"bool('') = {bool_str2}")
print(f"bool(1) = {bool_num1}")
print(f"bool(0) = {bool_num2}")

# Type checking
value = "100"
print(f"\ntype() check: type('{value}') = {type(value)}")
print(f"isinstance() check: isinstance('{value}', str) = {isinstance(value, str)}")
print(f"isinstance() check: isinstance('{value}', int) = {isinstance(value, int)}")

# ========================================
# I. MULTIPLE ASSIGNMENT
# ========================================
print("\n[I] Multiple Assignment")
print("-" * 70)

# Assign multiple variables in one line
name, age, city = "Alice", 28, "NYC"
print(f"Name: {name}, Age: {age}, City: {city}")

# Assign same value to multiple variables
x = y = z = 100
print(f"x={x}, y={y}, z={z}")

# Unpacking from tuple/list
data = (1, "Bob", 30)
emp_id, emp_name, emp_age = data
print(f"ID: {emp_id}, Name: {emp_name}, Age: {emp_age}")

print("\n" + "=" * 70)
print("END OF BASICS MODULE")
print("=" * 70)

