import random

def generate_number():
    number = ""
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    index = random.randint(0, len(nums) - 1)
    number += str(nums[index])
    nums.pop(index)
    nums.append(0)

    for x in range(3):
        index = random.randint(0, len(nums) - 1)
        number += str(nums[index])
        nums.pop(index)
    return number


def verify_input(user_input):
    if not user_input.isnumeric():
        print("Input is not numeric")
        return False
    if len(user_input) !=4:
        print("Input has not 4 digits")
        return False
    if user_input[0] == "0":
        print("Input can not start with 0")
        return False
    s = set()
    for x in user_input:
        s.add(x)
    if len(s) != 4:
        print("No duplicities allowed")
        return False
    return True

def calc_bulls_and_cows(num1, num2):

    bulls=0
    for x in range(4):
        if num1[x]==num2[x]:
            bulls+=1
    cows=0
    for x in range(4):
        if num1[x] in num2:
            cows+=1
    cows-=bulls

    return bulls, cows

secret_num = generate_number()

print(secret_num)

while True:
    user_input=input("Guess number: ")

    if not verify_input(user_input):
        continue

    if user_input==secret_num:
        print("Your guess is right")
        break
    bulls, cows= calc_bulls_and_cows(secret_num, user_input)

    bulls_str= "bulls"
    if bulls==1:
        bulls_str="bull"

    cows_str = "cows"
    if cows == 1:
        cows_str = "cow"

    print(f"{bulls} {bulls_str}; {cows} {cows_str}")



