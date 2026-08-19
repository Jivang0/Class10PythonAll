# Characteristics of a Python List
# Ordered – Items keep their order.
# Mutable – You can change, add, or remove items.
# Allows duplicates – The same value can appear more than once.
# Written inside square brackets [].

#List of numbers
number = [1,2,3,4,5,1]
print(number)
print(type(number))

#List of strings
fruits = ["Apple", "Banana", "Mango"]
print(fruits)

#Mixed list
student = ["Ram", 20, 85.5, True]
print(student)

colors = ["Red", "Blue", "Green"]
colors[1] = "Yellow"
print(colors)


# Python uses index numbers, starting from 0.
fruits = ["Apple", "Banana", "Mango"]
print(fruits[0])   # Apple
print(fruits[1])   # Banana
print(fruits[2])   # Mango


fruits = ["Apple", "Banana"]
fruits.append("Mango")
print(fruits)

fruits = ["Apple", "Banana", "Mango"]
fruits.remove("Banana")
print(fruits)