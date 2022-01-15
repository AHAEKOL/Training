l = [6,5,4,3,2,1]

sorted = False
while not sorted:
    sorted = True
    for x in range(len(l) - 1):
        if l[x] > l[x+1]:
            tmp = l[x]
            l[x] = l[x + 1]
            l[x + 1] = tmp
            sorted = False

print(l)