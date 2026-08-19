# if_statement
number = int(input("Enter a number:"))
if number < 0:
    print("The number is negative.")


number = int(input("Enter a number:"))
if number < 0:
    print("The number is negative.")
else:
    print("The number is positive.")

    
# Grade Calculator
marks = int(input("Enter your marks: "))
if marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")



# if-elif-else example
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")



#Odd or Even Number Checker
num = int(input("Enter a number:"))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.") 


age = int(input("Enter your age: "))
if age >= 16:
    print("You are eligible for citizenship.")
    if age >= 18:
        print("You are eligible to cast a vote.")
    else:
        print("You are not eligible to cast vote.")
print("You are a minor.")



user_number = int(input("Enter a number: ")) 
if user_number > 0:
    print("The number is positive.")
    if user_number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
elif user_number == 0:
    print("The number is zero.")
elif user_number < 0:
    print("The number is negative.")
else:
    print("Please provide a valid number.")