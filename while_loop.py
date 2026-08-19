count = 1;
while count <= 5:
    print(count)
    count += 1



number = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(number, "x", i, "=", number * i)
    i = i + 1



count = 1
while count <=5:
    print("Hii how are you?")
    count += 1


password = ""

while password != "python":
    password = input("Enter password: ")

print("Access Granted!")


# Break Statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break  
  i += 1


# Continue Statement
  i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)