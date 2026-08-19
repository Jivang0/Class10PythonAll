num = int(input("Enter a number: "))
sum = 0
temp = num 
while num >0:
    digit = num % 10
    sum = sum + digit ** 3
    num = num // 10
if temp == sum:
    print(temp, "is an Armstrong number")
else:
    print(temp, "is not an Armstrong number")
    