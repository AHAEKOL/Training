print('Hello world!')

vysky = [1.75,1.8,1.95]
for x in vysky:
	print(x, end=' ')
print('')

for x in vysky:
    if x >= 1.8:
        print(f"je to dlouhan a meri {x}")


pole = [[1,2], [3, 4]]

for x in pole:
     print(x[0])

slov = {"Jan" : 25 , "Ivan" : 18}

for x, y in slov.items():
    print(f"Jmenuje se {x} a je mu {y}")

n = int(input('Zadej cele cislo: '))

# vytvori list o N prvcich z prvnich prvku listu
l = [1,2,3,4,5,6,7,8,9]
l2 =l[1:n+1]
print(l2)