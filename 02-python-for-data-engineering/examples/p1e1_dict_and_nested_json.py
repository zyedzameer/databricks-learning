# EXERCISE 1 - Nested JSON Handling

events1 = [
    {
        "id": 1,
        "customer": {
            "name": "Alice",
            "city": "Chennai"
        },
        "amount": 100
    },
    {
        "id": 2,
        "customer": {
            "name": "Bob"
        },
        "amount": 200
    },
    {
        "id": 3,
        "amount": 300
    }
]

# expected output

output1 = [
    ("Alice", "Chennai"),
    ("Bob", "Unknown"),
    ("Unknown", "Unknown")
]

output_list = []
for e in events1:
    cust = e.get("customer", {})

    cust_name = cust.get("name", "Unknown")
    cust_city = cust.get("city", "Unknown")
    output_list.append((cust_name, cust_city))

print(output_list)



# EXERCISE 2 - Amount Categorization

events2 = [
    {"id": 1, "amount": 100},
    {"id": 2, "amount": None},
    {"id": 3},
    {"id": 4, "amount": 250}
]

output2 = {
    "LOW": [100],
    "HIGH": [250],
    "MISSING": [2, 3]
}

res_dict = {
    "LOW": [],
    "HIGH": [],
    "MISSING": []
}

for e in events2:
    amt = e.get("amount")

    if amt is None:
        res_dict["MISSING"].append(e["id"])

    elif amt < 200:
        res_dict["LOW"].append(amt)

    else:
        res_dict["HIGH"].append(amt)

print(res_dict)



# EXERCISE 3 - Python Truthiness with Lists

records = [
    {"name": "Alice", "skills": ["Python", "Spark"]},
    {"name": "Bob", "skills": []},
    {"name": "Charlie"},
    {"name": "David", "skills": ["SQL"]}
]

result3 = {
    "HAS_SKILLS": ["Alice", "David"],
    "NO_SKILLS": ["Bob", "Charlie"]
}

res = {"HAS_SKILLS":[],"NO_SKILLS":[]}

for r in records:
    skill = r.get("skills",[])

    if skill:
        res["HAS_SKILLS"].append(r["name"])

    else:
        res["NO_SKILLS"].append(r["name"])

print(res)

# ============================================================
# PYTHON FOUNDATION LEARNINGS
# ============================================================

# 1. dict.get(key, default)
#    - Safely fetch dictionary values
#    - Prevents KeyError if key missing

# 2. Nested JSON Handling
#    - Use {} as default for nested objects
#    - Allows chained .get() safely

# 3. Safe List Defaults
#    - Use [] as default for list fields
#    - Prevents crashes when field missing

# 4. Handling Missing and Null Values
#    - Missing key and explicit None can both be checked using:
#         if value is None

# 5. Result Initialization
#    - Initialize dictionary/list structures before loops
#    - Prevents KeyError during append()

# 6. append()
#    - Used to accumulate values into lists

# 7. Python Truthiness
#    - Empty list => False
#    - Non-empty list => True
#    - Preferred style:
#         if skills:

# 8. Production-Safe Thinking
#    - Handle bad/incomplete data safely
#    - Avoid runtime crashes
#    - Important for ETL/API/Kafka/Spark processing

# ============================================================