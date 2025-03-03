# Creating a Dictionary
person = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}

# Accessing Values
print("Name:", person["name"])
print("Age:", person["age"])

# Modifying Values
person["age"] = 26
print("Updated Age:", person["age"])

# Adding New Key-Value Pairs
person["height"] = 5.9
print("Updated Dictionary:", person)

# Removing Key-Value Pairs
del person["is_student"]
print("After Deletion:", person)

# Dictionary Length
print("Number of Keys:", len(person))
