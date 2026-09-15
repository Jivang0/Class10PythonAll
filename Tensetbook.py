def calculate(a,b=5):
    return a * b
print(calculate(10))


fruits = ["Apple", "Mango", "Banana"]
for x in fruits:
    print(x)

count = 1
while count < 5:
    print("Running") # Infinite loop 


file = open("data.txt","r") 
file.write("hello")
file.close()



import turtle
t = turtle.Turtle()
for i in range(3):
    t.forward(100)
    t.left(120)
turtle.done()

import math
print(math.sqrt(25))

from math import*
print(sqrt(16))

# 3
for i in range(3,16,3):
    print(i)

for i in range(1,7):
    print(3*i)


# 4 
def multiple_numbers(x,y):
    return x*y
print("The product is ",multiple_numbers(2,3))

#5 
import math
print(math.pi*10)


# 6
file = open("records.txt","a")
file.write("New Data")
file.close()


# 7
import turtle
t = turtle.Turtle()
t.forward(100)
t.left(90)
t.forward(50)
turtle.done()
turtle.exitonclick()



# 8
import pandas as pd 
df = pd.read_csv("inventory.csv")
print(df)



# 9 

try:
    num = int(input("Enter an integer: "))
    print(num)
except ValueError:
    print("Please enter a valid number")


# 10 
import matplotlib.pyplot as plt
plt.plot([1,2,3],[10,20,30])

x = [1,2,3]
y = [10,20,30]
plt.plot(x,y)
plt.show()


# 31. while loop without increment/decrement
count = 1
while count <= 5:
    print(count)
# This creates an infinite loop because count never changes.

# Fix 
count = 1
while count <= 5:
    print(count)
    count += 1


# 32. Default arguments
# A default argument is an argument that already has a value in the function definition.

def interest(p, t, r=10):
    return (p * t * r) / 100
interest(5000,4)

# or 
interest(5000, 2, 12)
# It makes the function more flexible.


# 33. Handle FileNotFoundError
try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File not found.")
# The program does not crash when the file does not exist.


# 34. Void vs Non-Void function
# Void function
# A void function performs an operation but does not return a value.
def greet():
    print("Hello")
greet()

# Non-Void function
# A non-void function returns a value.

def add(a, b):
    return a + b
print(add(2,3))
# A programmer needs a non-void function when the result needs to be used later.

# 35. Return multiple values

# Python functions can return multiple values using a tuple.

def calculate(a, b):
    return a + b, a * b

sum_value, product = calculate(5, 4)

print(sum_value)
print(product)


# 36. CSV module vs Pandas
# CSV Module	                  Pandas
# Basic CSV handling	        Advanced data analysis
# More manual coding	        Simple and powerful
# Suitable for simple files  	Suitable for large datasets
# Fewer data operations	        Filtering, sorting, grouping, etc.

# For millions of rows, Pandas is generally preferred because it provides powerful and convenient data-processing operations.

# 37. Draw a hexagon using Turtle

# A hexagon has 6 sides.

# Turning angle:

# 360/6 = 60 degree
import turtle
for i in range(6):
    turtle.forward(100)
    turtle.left(360 / 6)
turtle.exitonclick()

# 38. from math import sqrt vs import math
# Import entire module:
import math
print(math.sqrt(25))

# Import only required function:
from math import sqrt
print(sqrt(25))

# Importing only the required function can make the code shorter and avoid unnecessary names in the program's namespace.

# 39. Importance of finally
# The finally block executes whether an exception occurs or not.
# Example:

try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    print("File operation completed.")

# In file handling, closing the file in finally is useful because it ensures the file is closed even if an error occurs.

# finally:
#     file.close()

# This helps release resources properly.

# 40. Pie Chart vs Line Chart
# For showing the market-share percentage of 5 products, a Pie Chart is more appropriate.

import matplotlib.pyplot as plt

products = ["A", "B", "C", "D", "E"]
share = [30, 25, 20, 15, 10]

plt.pie(share, labels=products, autopct="%1.1f%%")
plt.title("Market Share")
plt.show()

# Reason: A pie chart clearly shows how each product contributes to the whole (100%).

# Group C — Long Answer Questions
# 21. Find the largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("Largest number =", largest)

# 22. Simple Interest using a function

# Formula:

# SI = {P * T * R}/{100} 


def calculate_interest(p, t, r):
    return (p * t * r) / 100


p = float(input("Enter Principal: "))
t = float(input("Enter Time: "))
r = float(input("Enter Rate: "))

si = calculate_interest(p, t, r)
print("Simple Interest =", si)

# 23. Sum of first 10 even numbers
num = 2
count = 1
total = 0

while count <= 10:
    total = total + num
    num = num + 2
    count = count + 1

print("Sum =", total)

# Output:

Sum = 110

# 24. Colored square using Turtle
import turtle

t = turtle.Turtle()

t.color("blue")
t.begin_fill()

for i in range(4):
    t.forward(100)
    t.right(90)

t.end_fill()

turtle.exitonclick()

# If you specifically need blue pen and red fill, use:

t.pencolor("blue")
t.fillcolor("red")

# Complete:

import turtle

t = turtle.Turtle()

t.pencolor("blue")
t.fillcolor("red")

t.begin_fill()

for i in range(4):
    t.forward(100)
    t.right(90)

t.end_fill()

turtle.exitonclick()

# 25. File handling
# a) Create file and write text
file = open("students.txt", "w")
file.write("Class 10 Computer Science")
file.close()

# b) Append text
file = open("students.txt", "a")
file.write("\nProgramming in Python")
file.close()

# 26. Read CSV and filter Computer marks > 80
import pandas as pd

df = pd.read_csv("marks.csv")

result = df[df["Computer"] > 80]

print(result)

# This displays only students whose Computer score is greater than 80.

# 27. Handle ZeroDivisionError
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero!")

# 28. Dice roller — roll 5 times
import random

for i in range(5):
    dice = random.randint(1, 6)
    print("Dice =", dice)

random.randint(1, 6) # generates a random integer from 1 to 6.

# 29. Bar chart using Matplotlib
import matplotlib.pyplot as plt

products = ["A", "B", "C"]
sales = [150, 300, 250]

plt.bar(products, sales)

plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()

# 30. Sum of digits

# For example:

# 456 → 4 + 5 + 6 = 15


def sum_of_digits(num):
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    return total


num = int(input("Enter a number: "))

print("Sum of digits =", sum_of_digits(num))
