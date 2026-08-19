# A tuple is a built-in data type in Python that stores a collection of multiple items in a single variable.
# Unlike a list, a tuple cannot be changed after it is created (it is immutable).

# syntax
# Tuples are created using parentheses ().

fruits = ("Apple", "Banana", "Mango")
print(fruits)
print(type(fruits))

# Characteristics of a Tuple
# Stores multiple values.
# Ordered (items have a fixed order).
# Immutable (cannot add, remove, or modify items).
# Allows duplicate values.
# Can store different data types.

data = ("Ram", 20, 65.5, True)
print(data)

colors = ("Red", "Green", "Blue")

print(colors[0])
print(colors[2])

# Tuple is Immutable
# You cannot change an item.
colors = ("Red", "Green", "Blue")
colors[1] = "Yellow"