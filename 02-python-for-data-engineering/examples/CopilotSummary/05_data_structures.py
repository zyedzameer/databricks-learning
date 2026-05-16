"""
05_data_structures.py
=====================
Collection Data Types: list, tuple, dict, set

Topics Covered:
- Lists: mutable, ordered, indexed, allow duplicates
- Tuples: immutable, ordered, indexed, allow duplicates
- Dictionaries: mutable, unordered, key-value pairs
- Sets: mutable, unordered, unique elements
- Slicing and indexing
- Built-in methods for each type
"""

print("=" * 70)
print("5. DATA STRUCTURES - COLLECTIONS")
print("=" * 70)

# ========================================
# A. LISTS
# ========================================
print("\n[A] LISTS - Mutable, Ordered Collections")
print("-" * 70)
"""
Characteristics:
- Notation: []
- Mutable: Can add, remove, modify elements
- Ordered: Maintains insertion order
- Indexed: Access by position (0-based)
- Iterable: Can loop through
- Homogeneous recommended, but heterogeneous allowed
"""

# Create lists
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]
empty_list = []

print(f"fruits: {fruits}")
print(f"mixed types: {mixed}")
print(f"type: {type(fruits)}, length: {len(fruits)}")

# Access elements (indexing)
print(f"\nIndexing:")
print(f"  First element: {fruits[0]}")
print(f"  Last element: {fruits[-1]}")
print(f"  Second element: {fruits[1]}")

# Slicing
print(f"\nSlicing:")
print(f"  fruits[0:2]: {fruits[0:2]}")  # From index 0 to 1
print(f"  fruits[1:]: {fruits[1:]}")   # From index 1 to end
print(f"  fruits[::-1]: {fruits[::-1]}")  # Reverse

# Modifying lists
print(f"\nModifying lists:")
fruits[0] = "orange"  # Update
print(f"  After update: {fruits}")

fruits.append("date")  # Add to end
print(f"  After append: {fruits}")

fruits.insert(1, "blueberry")  # Insert at index
print(f"  After insert at index 1: {fruits}")

fruits.extend(["papaya", "kiwi"])  # Add multiple elements
print(f"  After extend: {fruits}")

# Removing elements
removed = fruits.pop()  # Remove last element
print(f"  Removed '{removed}': {fruits}")

removed = fruits.pop(0)  # Remove by index
print(f"  Removed '{removed}' at index 0: {fruits}")

fruits.remove("blueberry")  # Remove by value
print(f"  After remove('blueberry'): {fruits}")

# Useful list methods
print(f"\nList methods:")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"  Original: {numbers}")
print(f"  index(1): {numbers.index(1)}")  # Find first occurrence
print(f"  count(1): {numbers.count(1)}")  # Count occurrences
numbers_sorted = sorted(numbers)
print(f"  sorted(): {numbers_sorted}")

# Remove duplicates using set
numbers_unique = list(set(numbers))
print(f"  Remove duplicates: {numbers_unique}")

# ========================================
# B. TUPLES
# ========================================
print("\n[B] TUPLES - Immutable, Ordered Collections")
print("-" * 70)
"""
Characteristics:
- Notation: ()
- Immutable: Cannot add, remove, or modify
- Ordered: Maintains insertion order
- Indexed: Access by position
- Iterable: Can loop through
- Useful for: Fixed data, dictionary keys, function returns
"""

# Create tuples
coords = (10, 20, 30)
single_item = ("only",)  # Note: comma required for single element
empty_tuple = ()

print(f"coords: {coords}")
print(f"single_item: {single_item}")
print(f"type: {type(coords)}, length: {len(coords)}")

# Access elements
print(f"\nIndexing:")
print(f"  coords[0]: {coords[0]}")
print(f"  coords[-1]: {coords[-1]}")

# Slicing
print(f"\nSlicing:")
print(f"  coords[0:2]: {coords[0:2]}")
print(f"  coords[::-1]: {coords[::-1]}")

# Tuple methods (limited)
print(f"\nTuple methods:")
print(f"  index(20): {coords.index(20)}")
print(f"  count(10): {coords.count(10)}")

# Tuple unpacking
print(f"\nTuple unpacking:")
x, y, z = coords
print(f"  x={x}, y={y}, z={z}")

# Immutability - this will cause error if uncommented
# coords[0] = 100  # TypeError: 'tuple' object does not support item assignment

# Convert tuple to list for modification
print(f"\nConvert to list for modification:")
coords_list = list(coords)
coords_list[0] = 100
coords = tuple(coords_list)
print(f"  Modified coords: {coords}")

# ========================================
# C. DICTIONARIES
# ========================================
print("\n[C] DICTIONARIES - Key-Value Collections")
print("-" * 70)
"""
Characteristics:
- Notation: {}
- Mutable: Can add, remove, modify pairs
- Unordered (in older Python): Uses key-value pairs
- Keys must be immutable (str, int, tuple)
- Values can be any type
- Lookup by key (not index)
"""

# Create dictionaries
person = {"name": "Alice", "age": 28, "city": "NYC"}
employee = {
    "id": 101,
    "name": "Bob",
    "salary": 60000,
    "skills": ["Python", "SQL", "BigQuery"]
}

print(f"person: {person}")
print(f"employee: {employee}")
print(f"type: {type(person)}")

# Access values
print(f"\nAccessing values:")
print(f"  person['name']: {person['name']}")
print(f"  person.get('city'): {person.get('city')}")
print(f"  person.get('country', 'USA'): {person.get('country', 'USA')}")

# Add/Update items
print(f"\nAdd/Update items:")
person["country"] = "USA"  # Add
print(f"  After adding country: {person}")
person["age"] = 29  # Update
print(f"  After updating age: {person}")

person.update({"city": "LA", "state": "CA"})
print(f"  After update(): {person}")

# Remove items
print(f"\nRemove items:")
removed_value = person.pop("country")
print(f"  Removed 'country': {person}")

key_value_pair = person.popitem()  # Remove last added
print(f"  Removed {key_value_pair}: {person}")

# Iterate over dictionary
print(f"\nIterate dictionary:")
student = {"name": "Charlie", "marks": 85, "grade": "B"}
for key in student:
    print(f"  {key}: {student[key]}")

for key, value in student.items():
    print(f"  {key} = {value}")

print(f"\nKeys: {list(student.keys())}")
print(f"Values: {list(student.values())}")

# ========================================
# D. SETS
# ========================================
print("\n[D] SETS - Unordered, Unique Collections")
print("-" * 70)
"""
Characteristics:
- Notation: {}  (not {k:v})
- Mutable: Can add, remove elements
- Unordered: No indexing or slicing
- Unique: Duplicates not allowed
- Iterable: Can loop through
- Use for: Remove duplicates, set operations (union, intersection)
"""

# Create sets
colors = {"red", "blue", "green"}
numbers_set = {1, 2, 3, 3, 2, 1}  # Duplicates removed

print(f"colors: {colors}")
print(f"numbers removed_duplicates: {numbers_set}")
print(f"type: {type(colors)}")

# Add elements
colors.add("yellow")
print(f"\nAfter add('yellow'): {colors}")

colors.update(["purple", "orange"])
print(f"After update: {colors}")

# Remove elements
colors.discard("purple")  # Won't error if not found
print(f"After discard('purple'): {colors}")

# Set operations
print(f"\nSet operations:")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"  set1: {set1}")
print(f"  set2: {set2}")
print(f"  union: {set1 | set2}")
print(f"  intersection: {set1 & set2}")
print(f"  difference: {set1 - set2}")

# Remove duplicates from list using set
duplicated_list = [1, 2, 2, 3, 3, 3, 4]
unique_list = list(set(duplicated_list))
print(f"\nRemove duplicates from list:")
print(f"  Original: {duplicated_list}")
print(f"  Unique: {unique_list}")

# ========================================
# E. COMPARISON TABLE
# ========================================
print("\n[E] Data Structure Comparison")
print("-" * 70)

comparison = """
┌──────────┬─────────┬───────────┬──────────┬──────────┐
│ Type     │ Ordered │ Indexed   │ Mutable  │ Unique   │
├──────────┼─────────┼───────────┼──────────┼──────────┤
│ List     │ Yes     │ Yes       │ Yes      │ No       │
│ Tuple    │ Yes     │ Yes       │ No       │ No       │
│ Dict     │ Yes*    │ By key    │ Yes      │ Keys     │
│ Set      │ No      │ No        │ Yes      │ Yes      │
└──────────┴─────────┴───────────┴──────────┴──────────┘
*Python 3.7+: Dict maintains insertion order
"""
print(comparison)

# ========================================
# F. REAL-WORLD EXAMPLE
# ========================================
print("\n[F] Real-World Example: Employee Data Processing")
print("-" * 70)

employees = [
    {"id": 101, "name": "Alice", "dept": "IT", "salary": 60000},
    {"id": 102, "name": "Bob", "dept": "HR", "salary": 50000},
    {"id": 103, "name": "Charlie", "dept": "IT", "salary": 65000}
]

# Find all IT employees
it_employees = [emp for emp in employees if emp["dept"] == "IT"]
print(f"IT Department Employees: {len(it_employees)}")
for emp in it_employees:
    print(f"  - {emp['name']}: ${emp['salary']}")

# Total IT salary
total_salary = sum(emp["salary"] for emp in it_employees)
print(f"Total IT Salary: ${total_salary}")

# Average salary
avg_salary = total_salary / len(it_employees)
print(f"Average IT Salary: ${avg_salary:,.2f}")

# Department set
departments = {emp["dept"] for emp in employees}
print(f"Departments: {departments}")

print("\n" + "=" * 70)
print("END OF DATA STRUCTURES MODULE")
print("=" * 70)

