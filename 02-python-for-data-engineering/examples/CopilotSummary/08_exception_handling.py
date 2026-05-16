"""
08_exception_handling.py
========================
Exception Handling: try, except, finally, else

Topics Covered:
- try-except blocks
- Multiple exceptions
- Exception hierarchy
- finally block
- else block
- Raising exceptions
- Custom exceptions
"""

print("=" * 70)
print("8. EXCEPTION HANDLING")
print("=" * 70)

# ========================================
# A. BASIC TRY-EXCEPT
# ========================================
print("\n[A] Basic Try-Except Block")
print("-" * 70)
"""
Syntax:
try:
    code that might cause error
except ExceptionType:
    handle the error
"""

# Example 1: Division by zero
print("Example 1: Handle ZeroDivisionError")
try:
    result = 10 / 0
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

print("Program continues normally\n")

# Example 2: Index out of range
print("Example 2: Handle IndexError")
try:
    numbers = [1, 2, 3]
    print(f"Element at index 10: {numbers[10]}")
except IndexError:
    print("Error: Index out of range!")

# ========================================
# B. MULTIPLE EXCEPTIONS
# ========================================
print("\n[B] Multiple Exception Handlers")
print("-" * 70)

data = ["10", "abc", "20", "0"]

for item in data:
    try:
        result = 100 / int(item)
        print(f"100 / {item} = {result}")
    except ValueError:
        print(f"  Error: '{item}' is not a valid integer")
    except ZeroDivisionError:
        print(f"  Error: Cannot divide by zero")

# ========================================
# C. EXCEPTION HIERARCHY
# ========================================
print("\n[C] Exception Hierarchy - Specific then General")
print("-" * 70)
"""
Always place specific exceptions before general ones.
More specific exceptions should be caught first.
"""

def process_data(value):
    try:
        # This could raise multiple exceptions
        list_data = ["a", "b", "c"]
        index = int(value)
        result = 100 / index
        item = list_data[index]
        return f"Item: {item}, Result: {result}"
    except ValueError as e:
        return f"ValueError: '{value}' is not a valid number"
    except ZeroDivisionError as e:
        return f"ZeroDivisionError: {e}"
    except IndexError as e:
        return f"IndexError: Index out of range"
    except Exception as e:
        return f"General Exception: {e}"

print(process_data("abc"))     # ValueError
print(process_data("0"))       # ZeroDivisionError
print(process_data("10"))      # IndexError
print(process_data("2"))       # Success

# ========================================
# D. TRY-EXCEPT-FINALLY
# ========================================
print("\n[D] Try-Except-Finally Block")
print("-" * 70)
"""
finally block always executes, whether exception occurs or not
Used for cleanup (closing files, releasing resources)
"""

def file_operation_example():
    try:
        print("  Opening file...")
        # Simulating file operation
        result = 10 / 2
        print(f"  Processing complete: result = {result}")
    except ZeroDivisionError:
        print("  Error: Division by zero!")
    finally:
        print("  Closing file... (cleanup happens here)")

print("File operation with finally:")
file_operation_example()

# Another example
print("\nFile operation with error:")

def file_operation_with_error():
    try:
        print("  Opening file...")
        result = 10 / 0
        print(f"  Processing: {result}")
    except ZeroDivisionError:
        print("  Error: Cannot divide by zero!")
    finally:
        print("  Closing file... (cleanup happens regardless)")

file_operation_with_error()

# ========================================
# E. TRY-EXCEPT-ELSE
# ========================================
print("\n[E] Try-Except-Else Block")
print("-" * 70)
"""
else block executes only if NO exception occurs in try block
"""

def divide_with_else(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"  Error: Cannot divide by zero!")
        return None
    else:
        # This code runs only if no exception occurred
        print(f"  Division successful: {a} / {b} = {result}")
        return result
    finally:
        print("  Operation completed")

print("Division with else clause:")
print("\nSuccess case (20 / 5):")
divide_with_else(20, 5)

print("\nError case (20 / 0):")
divide_with_else(20, 0)

# ========================================
# F. RAISING EXCEPTIONS
# ========================================
print("\n[F] Raising Exceptions Manually")
print("-" * 70)

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return f"Age {age} is valid"

print("Validate age:")
try:
    print(validate_age(25))
    print(validate_age(-5))  # This will raise exception
except ValueError as e:
    print(f"Caught error: {e}")

# ========================================
# G. CUSTOM EXCEPTIONS
# ========================================
print("\n[G] Custom Exception Classes")
print("-" * 70)

class InsufficientStockError(Exception):
    """Custom exception for inventory management"""
    pass

class InvalidPriceError(Exception):
    """Custom exception for invalid price"""
    pass

class Product:
    def __init__(self, name, price, stock):
        if price < 0:
            raise InvalidPriceError(f"Price cannot be negative: {price}")
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
        if quantity > self.stock:
            raise InsufficientStockError(
                f"Not enough stock. Available: {self.stock}, Requested: {quantity}"
            )
        self.stock -= quantity
        return self.stock

# Use custom exceptions
print("Custom exception handling:")
data = [
    {"name": "Laptop", "price": 1200, "stock": 5, "buy": 2},
    {"name": "Mouse", "price": -50, "stock": 10, "buy": 1},  # Invalid price
    {"name": "Keyboard", "price": 100, "stock": 3, "buy": 5},  # Insufficient stock
]

for item_data in data:
    try:
        product = Product(item_data["name"], item_data["price"], item_data["stock"])
        remaining = product.reduce_stock(item_data["buy"])
        print(f"✓ {item_data['name']}: Purchased {item_data['buy']}, "
              f"Remaining: {remaining}")
    except InvalidPriceError as e:
        print(f"✗ {item_data['name']}: {e}")
    except InsufficientStockError as e:
        print(f"✗ {item_data['name']}: {e}")
    except Exception as e:
        print(f"✗ {item_data['name']}: Unexpected error: {e}")

# ========================================
# H. NESTED TRY-EXCEPT
# ========================================
print("\n[H] Nested Try-Except Blocks")
print("-" * 70)

def nested_exception_handling():
    try:
        print("  Outer try block")
        try:
            result = 10 / 0
        except ZeroDivisionError:
            print("  Inner except: Caught division by zero")
            # Re-raise or handle
            value = int("abc")  # Cause another error
    except ValueError:
        print("  Outer except: Caught value error")

print("Nested exception handling:")
nested_exception_handling()

# ========================================
# I. BEST PRACTICES
# ========================================
print("\n[I] Best Practices for Exception Handling")
print("-" * 70)

print("""
1. Be specific: Catch specific exceptions, not general Exception
2. Use finally for cleanup: Always runs, use for resource management
3. Avoid bare except: except: catches all, including KeyboardInterrupt
4. Use context managers: with statement for resource management
5. Log exceptions: Use logging module for debugging
6. Fail gracefully: Provide meaningful error messages
7. Re-raise when needed: Use 'raise' to propagate exceptions
""")

# Example of good practice
def safe_file_read(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except IOError:
        print(f"Error: Cannot read file '{filename}'")
        return None

# ========================================
# J. REAL-WORLD EXAMPLE
# ========================================
print("\n[J] Real-World Example: Bank Transaction")
print("-" * 70)

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive")
            if amount > self.balance:
                raise InsufficientStockError(f"Insufficient balance: {self.balance}")
            self.balance -= amount
            print(f"✓ Withdrew ${amount}. New balance: ${self.balance}")
        except ValueError as e:
            print(f"✗ Invalid amount: {e}")
        except InsufficientStockError as e:
            print(f"✗ Transaction failed: {e}")
        except Exception as e:
            print(f"✗ Unexpected error: {e}")

account = BankAccount("Alice", 1000)
print("Bank Account Transactions:")
account.withdraw(200)      # Success
account.withdraw(-50)      # Invalid amount
account.withdraw(1500)     # Insufficient balance
account.withdraw(300)      # Success

print("\\n" + "=" * 70)
print("END OF EXCEPTION HANDLING MODULE")
print("=" * 70)

