N = int(input("zadej cislo: "))

for y in range(1, N + 1):
   for x in range(1, N + 1):
      print(x * y, end='\t')
   print('')