for i in range(5):
    print("Your Name is Ram")


for i in range(1, 6): # not inclueded 6
    print(i)




fruits = ['apple', 'banana', 'manago']
print(type(fruits))

for fruit in fruits:
    print(fruit)   
print(fruits[1])


for i in range(1,10,2): #start, stop, step
    print(i)




for i in range(10):
    print(i)

text = input("Enter a your text: ")
count = 0
for char in text:
    if char == "a"or char =="e" or char == "i" or char == "o" or char == "u" or char == "A"or char =="E" or char == "I" or char == "O" or char == "U":
        count += 1
    else:
        print("Not a vowel character")
    
print(f" The total number of vowel is {count}")

text = input("Enter your text: ")
count = 0

for char in text:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or \
       char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
        count += 1

if count > 0:
    print(f"The total number of vowels is {count}")
else:
    print("No vowels are present in the text.")