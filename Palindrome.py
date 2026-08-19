# num = (input("Enter a number: "))
# if num.isdigit() and num[::-1] == num:
#     print("The number is a palindrome.")
# else:
#     print("The number is not a palindrome.")

# Palindrome Number Program

num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print(original, "is a Palindrome Number")
else:
    print(original, "is not a Palindrome Number")