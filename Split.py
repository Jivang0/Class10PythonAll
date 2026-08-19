The split() function is a string method used to break a string into smaller parts. It returns the parts as a list.

string.split(separator, maxsplit)

If no separator is given, Python splits the string wherever it finds whitespace (spaces, tabs, or newlines).

text = "I Love programming in python"
word = text.split()
print(word)


fruits = "Apple,Mango,Banana"
result = fruits.split(",")
print(result)

name, age = input("Enter your name and age ").split()
print("Name:", name)
print("Age:", age)
print(type(age))


# Split only a limited number of times (maxsplit)
text = "one two three four"
result = text.split(" ", 2)
print(result)