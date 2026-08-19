num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


num = float(input("Enter a number: "))

if num.is_integer():
    if int(num) % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Please enter an integer.")