"""
06_functions.py
===============
Functions: FBP (Function-Based Programming)
Function definition, parameters, return values, scope

Topics Covered:
- Function definition and calling
- Parameters and arguments (positional, keyword, default, *args, **kwargs)
- Return values and return types
- Docstrings
- Variable scope (local vs global)
- Built-in functions vs User-defined
"""

print("=" * 70)
print("6. FUNCTIONS - FUNCTION-BASED PROGRAMMING (FBP)")
print("=" * 70)

# ========================================
# A. SIMPLE FUNCTION DEFINITION
# ========================================
print("\n[A] Simple Function Definition")
print("-" * 70)
"""
Syntax:
def function_name():
    \"\"\"Optional docstring\"\"\"
    statements
    
Function is defined but not executed until called
"""

def greet():
    """Prints a greeting message"""
    print("Hello, welcome to Python learning!")

# Call the function
print("Calling greet():")
greet()

# ========================================
# B. FUNCTION WITH PARAMETERS
# ========================================
print("\n[B] Functions With Parameters")
print("-" * 70)

def greet_person(name):
    """Greet a specific person"""
    print(f"Hello, {name}! Welcome!")

greet_person("Alice")
greet_person("Bob")

# Multiple parameters
def add_numbers(num1, num2):
    """Add two numbers and display result"""
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

add_numbers(10, 20)
add_numbers(100, 250)

# ========================================
# C. FUNCTION WITH RETURN VALUES
# ========================================
print("\n[C] Functions With Return Values")
print("-" * 70)

def multiply(a, b):
    """Multiply two numbers and return result"""
    return a * b

result = multiply(5, 10)
print(f"multiply(5, 10) = {result}")

# Multiple return values (as tuple)
def calculate(x, y):
    """Return sum, difference, and product"""
    return x + y, x - y, x * y

sum_val, diff_val, prod_val = calculate(10, 3)
print(f"calculate(10, 3):")
print(f"  Sum: {sum_val}, Diff: {diff_val}, Product: {prod_val}")

# ========================================
# D. POSITIONAL VS KEYWORD ARGUMENTS
# ========================================
print("\n[D] Positional vs Keyword Arguments")
print("-" * 70)

def create_email(first_name, last_name, domain):
    """Generate email from name and domain"""
    email = f"{first_name.lower()}.{last_name.lower()}@{domain}"
    return email

# Positional arguments (order matters)
print("Positional arguments:")
email1 = create_email("John", "Doe", "example.com")
print(f"  {email1}")

# Keyword arguments (order doesn't matter)
print("\nKeyword arguments:")
email2 = create_email(domain="example.com", first_name="Jane", last_name="Smith")
print(f"  {email2}")

# Mix of positional and keyword
email3 = create_email("Bob", domain="example.com", last_name="Johnson")
print(f"  {email3}")

# ========================================
# E. DEFAULT PARAMETERS
# ========================================
print("\n[E] Default Parameters")
print("-" * 70)

def power(base, exponent=2):
    """Calculate power with default exponent of 2"""
    return base ** exponent

print(f"power(5): {power(5)}")        # Uses default exponent=2
print(f"power(5, 3): {power(5, 3)}")  # Override default

def print_info(name, age=25, city="Unknown"):
    """Print person info with defaults"""
    print(f"  Name: {name}, Age: {age}, City: {city}")

print("\nWith defaults:")
print_info("Alice")
print_info("Bob", 30)
print_info("Charlie", 35, "NYC")

# ========================================
# F. *ARGS (VARIABLE POSITIONAL ARGUMENTS)
# ========================================
print("\n[F] *args - Variable Positional Arguments")
print("-" * 70)

def sum_all(*numbers):
    """Sum any number of arguments"""
    return sum(numbers)

print(f"sum_all(1, 2, 3): {sum_all(1, 2, 3)}")
print(f"sum_all(10, 20, 30, 40): {sum_all(10, 20, 30, 40)}")

def print_items(*items):
    """Print multiple items"""
    for i, item in enumerate(items, 1):
        print(f"  {i}. {item}")

print("\nItems:")
print_items("apple", "banana", "cherry", "date")

# ========================================
# G. **KWARGS (VARIABLE KEYWORD ARGUMENTS)
# ========================================
print("\n[G] **kwargs - Variable Keyword Arguments")
print("-" * 70)

def print_attributes(**kwargs):
    """Print key-value pairs"""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("Person attributes:")
print_attributes(name="Alice", age=28, city="NYC", job="Engineer")

def build_url(**params):
    """Build URL query string from keyword arguments"""
    query_strings = [f"{k}={v}" for k, v in params.items()]
    return "?" + "&".join(query_strings)

url_params = build_url(user="john", page=2, limit=10)
print(f"URL: /api/users{url_params}")

# ========================================
# H. COMBINING *ARGS AND **KWARGS
# ========================================
print("\n[H] Combining *args and **kwargs")
print("-" * 70)

def flexible_function(required, *args, **kwargs):
    """Function with all parameter types"""
    print(f"Required: {required}")
    if args:
        print(f"Extra positional args: {args}")
    if kwargs:
        print("Extra keyword arguments:")
        for key, value in kwargs.items():
            print(f"  {key}: {value}")

print("Test 1:")
flexible_function("must-have")

print("\nTest 2:")
flexible_function("item1", "item2", "item3", color="red", size="large")

# ========================================
# I. DOCSTRINGS
# ========================================
print("\n[I] Docstrings and Help")
print("-" * 70)

def calculate_salary(base_salary, bonus_percent=0):
    """
    Calculate total salary with optional bonus.

    Args:
        base_salary (float): The base salary amount
        bonus_percent (float): Bonus percentage (default: 0)

    Returns:
        float: Total salary including bonus

    Example:
        >>> calculate_salary(50000, 10)
        55000.0
    """
    bonus_amount = base_salary * bonus_percent / 100
    return base_salary + bonus_amount

print(f"calculate_salary(50000, 15): ${calculate_salary(50000, 15)}")
print(f"\nFunction help:")
print(calculate_salary.__doc__)

# ========================================
# J. VARIABLE SCOPE
# ========================================
print("\n[J] Variable Scope - Local vs Global")
print("-" * 70)

global_var = 100  # Global scope

def test_scope():
    """Demonstrate local and global scope"""
    local_var = 200  # Local scope
    print(f"  Inside function:")
    print(f"    global_var: {global_var}")
    print(f"    local_var: {local_var}")

print(f"Outside function:")
print(f"  global_var: {global_var}")

test_scope()

# Accessing local variable outside function would cause error:
# print(local_var)  # NameError: name 'local_var' is not defined

# Using global keyword
def modify_global():
    """Modify global variable"""
    global global_var
    global_var = 500
    print(f"  Modified global_var to: {global_var}")

print(f"\nBefore modify_global: global_var = {global_var}")
modify_global()
print(f"After modify_global: global_var = {global_var}")

# ========================================
# K. LAMBDA FUNCTIONS (ANONYMOUS FUNCTIONS)
# ========================================
print("\n[K] Lambda Functions (Anonymous)")
print("-" * 70)

# Lambda: One-line anonymous function
# Syntax: lambda arguments: expression

square = lambda x: x ** 2
print(f"square(5): {square(5)}")

add = lambda x, y: x + y
print(f"add(10, 20): {add(10, 20)}")

# Common use with map, filter, sorted
numbers = [1, 2, 3, 4, 5]

# map: Apply lambda to each element
squared = list(map(lambda x: x ** 2, numbers))
print(f"\nmap(lambda x: x**2, {numbers}): {squared}")

# filter: Keep elements where lambda returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"filter(lambda x: x%2==0, {numbers}): {evens}")

# sorted with lambda
students = [("Alice", 85), ("Bob", 75), ("Charlie", 95)]
sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Sorted by score (descending):")
for name, score in sorted_by_score:
    print(f"  {name}: {score}")

# ========================================
# L. REAL-WORLD EXAMPLES
# ========================================
print("\n[L] Real-World Examples")
print("-" * 70)

def calculate_tax(income, tax_rate=0.20):
    """Calculate income tax"""
    return income * tax_rate

def calculate_monthly_emi(principal, rate, months):
    """Calculate EMI (Equated Monthly Installment)"""
    monthly_rate = rate / 100 / 12
    if monthly_rate == 0:
        return principal / months
    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / \
          ((1 + monthly_rate) ** months - 1)
    return emi

# Test
print(f"Annual income: $100,000")
print(f"Income tax (20%): ${calculate_tax(100000):,.2f}")

print(f"\nLoan: $200,000, 8% annual rate, 5 years (60 months)")
emi = calculate_monthly_emi(200000, 8, 60)
print(f"Monthly EMI: ${emi:,.2f}")
print(f"Total paid: ${emi * 60:,.2f}")

print("\n" + "=" * 70)
print("END OF FUNCTIONS MODULE")
print("=" * 70)

