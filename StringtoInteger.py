numbers = [ "10", "20", "30", "40", "50"]

int_numbers = [int(num) for num in numbers]
print(int_numbers)

ints_numbers = []
for nums in numbers:
    ints_numbers.append(int(nums))
print(ints_numbers)

data = ["1", "2", "3", "4", "5"]

for i in range(len(data)):
    data[i] = int(data[i])

print(data)