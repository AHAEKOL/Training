n=input("zadej text: ")

print(n[0])

str = ""

for x in range(len(n)):
    str += n[len(n) - 1 - x]

print(str)


str2 = n[::-1]
print(str2)