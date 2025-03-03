# Creating a Set
unique_numbers = {1, 2, 3, 4, 5}

# Adding Elements
unique_numbers.add(6)
print("After Adding 6:", unique_numbers)

# Removing Elements
unique_numbers.remove(3)
print("After Removing 3:", unique_numbers)

# Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
print("Union:", set1.union(set2))

# Intersection
print("Intersection:", set1.intersection(set2))

# Difference
print("Difference:", set1.difference(set2))

# Set Length
print("Number of Unique Elements:", len(unique_numbers))
