numbers = {}

# Read file line by line and convert each line into a number and store it in a dictionary
with open('numbers.txt') as f:
    for line in f.readlines():
        number = int(line)
        if not number in numbers:
            numbers[number] = 0
        else:
            numbers[number] += 1

# Find the most common number in the dictionary
max_val = 0
max_key = 0
for k,v in numbers.items():
    if (v > max_val):
        max_val = v
        max_key = k

print(f"The most common number is: {max_key} ({max_val} times)")


# Convert the dictionary to a sorted list and check the sequence
numbers = list(numbers)
numbers.sort()
tmp = numbers[0] - 1
for x in numbers:
    if x != tmp + 1:
        print(f"The missing number is: {x-1}" )
        break
    else:
        tmp = x

