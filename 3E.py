# Take an integer input from the user
num = int(input("Enter an integer: "))

# Check whether the number is positive, negative, or zero
if num > 0:
    print("Positive")

    # Check if the positive number is even or odd
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

elif num < 0:
    print("Negative")

else:
    print("Zero")