vstup= input("Zadej slovo: ")

if vstup==vstup[::-1]:
	print("slovo je palindrom")
else:
	print("nejde o palindrom")