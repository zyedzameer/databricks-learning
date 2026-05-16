"""
07_oop.py
=========
Object-Oriented Programming: Classes, Objects, Methods, Inheritance

Topics Covered:
- Class definition and instantiation
- Instance variables and methods
- __init__ constructor
- self reference
- Inheritance (single)
- Encapsulation (public, private)
"""

print("=" * 70)
print("7. OBJECT-ORIENTED PROGRAMMING (OOP)")
print("=" * 70)

# ========================================
# A. BASIC CLASS DEFINITION
# ========================================
print("\n[A] Basic Class Definition")
print("-" * 70)

class Person:
    """A class to represent a person"""

    # Class variable (shared by all instances)
    species = "Homo sapiens"

    # Constructor - called when object is created
    def __init__(self, name, age):
        """Initialize person with name and age"""
        # Instance variables (unique to each object)
        self.name = name
        self.age = age

    # Instance method
    def introduce(self):
        """Introduce the person"""
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")

    def birthday(self):
        """Increment age by 1"""
        self.age += 1
        print(f"{self.name} is now {self.age} years old")

# Create objects (instances)
print("Creating person objects:")
person1 = Person("Alice", 28)
person2 = Person("Bob", 32)

# Call methods
person1.introduce()
person2.introduce()

# Access instance variables
print(f"\nAccess attributes:")
print(f"  person1.name: {person1.name}")
print(f"  person1.age: {person1.age}")

# Call method to modify state
print(f"\nBirthday update:")
person1.birthday()

# ========================================
# B. CLASS WITH MULTIPLE METHODS
# ========================================
print("\n[B] Class With Multiple Methods")
print("-" * 70)

class BankAccount:
    """A class to represent a bank account"""

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        """Add money to account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        """Remove money from account"""
        if amount > self.balance:
            print(f"Insufficient balance. Available: ${self.balance}")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}")
        else:
            print("Withdrawal amount must be positive")

    def get_balance(self):
        """Return current balance"""
        return self.balance

    def display_info(self):
        """Display account information"""
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")

# Use the account
print("Bank Account Operations:")
account = BankAccount("Charlie", 1000)
account.display_info()

print("\nDeposit $500:")
account.deposit(500)

print("\nWithdraw $200:")
account.withdraw(200)

print("\nTry to withdraw $2000 (more than balance):")
account.withdraw(2000)

account.display_info()

# ========================================
# C. INHERITANCE
# ========================================
print("\n[C] Inheritance - Extending Classes")
print("-" * 70)

class Animal:
    """Base class for animals"""

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        """Make a sound"""
        print(f"{self.name} makes a sound")

class Dog(Animal):
    """Dog class inheriting from Animal"""

    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Call parent constructor
        self.breed = breed

    def speak(self):
        """Override parent method"""
        print(f"{self.name} barks: Woof Woof!")

    def fetch(self):
        """Dog-specific method"""
        print(f"{self.name} is fetching...")

class Cat(Animal):
    """Cat class inheriting from Animal"""

    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    def speak(self):
        """Override parent method"""
        print(f"{self.name} meows: Meow!")

# Create objects
print("Inheritance example:")
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

dog.speak()
dog.fetch()

cat.speak()
print(f"Cat color: {cat.color}")

# ========================================
# D. ENCAPSULATION (PRIVATE ATTRIBUTES)
# ========================================
print("\n[D] Encapsulation - Private Attributes")
print("-" * 70)

class Employee:
    """Employee class with private attributes"""

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute (by convention)

    def get_salary(self):
        """Getter for salary"""
        return self.__salary

    def set_salary(self, new_salary):
        """Setter for salary with validation"""
        if new_salary > 0:
            self.__salary = new_salary
            print(f"Salary updated to ${new_salary}")
        else:
            print("Salary must be positive")

    def give_raise(self, percent):
        """Give salary raise by percentage"""
        raise_amount = self.__salary * percent / 100
        self.__salary += raise_amount
        print(f"Raise given: ${raise_amount:.2f}. New salary: ${self.__salary}")

emp = Employee("Diana", 50000)

print(f"Employee: {emp.name}")
print(f"Salary: ${emp.get_salary()}")

emp.give_raise(10)
emp.set_salary(65000)

# Try to access private attribute directly (discouraged)
# print(emp.__salary)  # Would cause AttributeError

# But you can access it as (not recommended):
print(f"Private attribute (not recommended): ${emp._Employee__salary}")

# ========================================
# E. CLASS VARIABLES VS INSTANCE VARIABLES
# ========================================
print("\n[E] Class Variables vs Instance Variables")
print("-" * 70)

class Counter:
    """Counter with class and instance variables"""

    count = 0  # Class variable (shared)

    def __init__(self, name):
        self.name = name  # Instance variable
        Counter.count += 1  # Modify class variable

    def show_count(self):
        print(f"Total counters created: {Counter.count}")

c1 = Counter("first")
c1.show_count()

c2 = Counter("second")
c2.show_count()

c3 = Counter("third")
c3.show_count()

# ========================================
# F. REAL-WORLD EXAMPLE: E-COMMERCE
# ========================================
print("\n[F] Real-World Example: E-Commerce Product")
print("-" * 70)

class Product:
    """Product in an e-commerce system"""

    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.__price = price  # Private
        self.__stock = stock  # Private

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def apply_discount(self, discount_percent):
        """Apply discount on price"""
        discount_amount = self.__price * discount_percent / 100
        self.__price -= discount_amount
        print(f"Discount applied. New price: ${self.__price:.2f}")

    def purchase(self, quantity):
        """Purchase items"""
        if quantity > self.__stock:
            print(f"Not enough stock. Available: {self.__stock}")
            return False
        self.__stock -= quantity
        total_price = self.__price * quantity
        print(f"Purchase successful: {quantity}x {self.name} = ${total_price:.2f}")
        return True

    def display_info(self):
        print(f"Product: {self.name}")
        print(f"  Price: ${self.__price:.2f}")
        print(f"  Stock: {self.__stock}")

# Use product
product = Product(1, "Laptop", 1200, 5)
product.display_info()

print("\nApply 15% discount:")
product.apply_discount(15)
product.display_info()

print("\nPurchase 2 units:")
product.purchase(2)
product.display_info()

print("\nTry to purchase 5 units (more than stock):")
product.purchase(5)

print("\n" + "=" * 70)
print("END OF OOP MODULE")
print("=" * 70)
print("=" * 70)

