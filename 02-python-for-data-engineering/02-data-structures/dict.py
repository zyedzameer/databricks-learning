emp_dict = {"name":"john","age":25,"dept":"IT"}

print(emp_dict["name"]) #reading element with key

emp_dict["salary"] = 20000 #adding an element to dict

print(emp_dict.get("city","Chennai")) #get method use default value if key not found

print(emp_dict.get("city")) #returns none if no key found (not key error)

# print(emp_dict["city"]) # direct read will throw key error - KeyError: 'city'

print(emp_dict)

removed_age = emp_dict.pop("age") # removes key and returns value

print("****************after popping age..")
print(emp_dict)

emp_dict.update({"city":"Mumbai","currency":"INR"}) #updates existing dictionary
print("****************after updating city and currency...")
print(emp_dict)

removed_item = emp_dict.popitem() #removes last inserted key-value pair
print("****************after popitem the last value...")
print(emp_dict)

print("****************keys()...")
print(emp_dict.keys()) #returns keys in a list

print("****************values()...")
print(emp_dict.values()) #returns values in a list

print("****************items()...")
print(emp_dict.items()) #returns list of tuple of all the key value pairs

for key,value in emp_dict.items():
    print(f"key is: {key} ; its value: {value}")

fruits = ["apple", "banana", "cherry"]

name_length = {}

for f in fruits:
    name_length[f] = len(f)

print(name_length)

sample_data = {
    "app": {
        "name": "DataEngineApp",
        "version": "0.1.0",
        "features": ["ingest", "transform", "serve"],
    },
    "users": {
        1001: {
            "id": 1001,
            "name": "Alice",
            "email": "alice@example.com",
            "age": 29,
            "active": True,
            "roles": ["analyst", "admin"],
            "preferences": {
                "theme": "dark",
                "notifications": {"email": True, "sms": False},
            },
            "last_login": None,
            "scores": (95.5, 87.0, 92.3),
            "metadata": {"signup_source": "web", "tags": {"beta", "premium"}},
        },
        1002: {
            "id": 1002,
            "name": "Bob",
            "email": "bob@example.com",
            "age": 34,
            "active": False,
            "roles": ["engineer"],
            "preferences": {
                "theme": "light",
                "notifications": {"email": False, "sms": False},
            },
            "scores": (),
            "metadata": {"signup_source": "referral", "tags": set()},
        },
    },
    "counters": {"total_users": 2, "active_users": 1},
    "config": None,
}

print(sample_data["users"][1002]["roles"][0]) #accessing inner elements

# Sample employee dataset: list of tuples (id, name, age, salary, address_dict)
EMPLOYEE_DATA = [
    (
        1,
        "John Doe",
        28,
        55000.00,
        {"street": "123 Elm St", "city": "Springfield", "state": "IL", "zip": "62704"},
    ),
    (
        2,
        "Jane Smith",
        34,
        72000.50,
        {"street": "456 Oak Ave", "city": "Rivertown", "state": "CA", "zip": "90210"},
    ),
    (
        3,
        "Samuel Green",
        41,
        88000,
        {"street": "789 Pine Rd", "city": "Lakeview", "state": "NY", "zip": "10001"},
    ),
    (
        4,
        "Priya Patel",
        30,
        63000,
        {"street": "321 Maple Ln", "city": "Hilltop", "state": "TX", "zip": "73301"},
    ),
    (
        5,
        "Liu Wei",
        26,
        48000,
        {"street": "654 Cedar Blvd", "city": "Metrocity", "state": "WA", "zip": "98101"},
    ),
]


for employee in EMPLOYEE_DATA:
    print(f"employee {employee[1]} is from {employee[4]["state"]} ")