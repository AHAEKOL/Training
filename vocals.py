word=input("type any word: ").lower()
vowels= "aeiyou"

vowels_count=0

for x in word:
	if x in vowels:
		vowels_count=vowels_count+1
print(f"no. of vowels is: {vowels_count}")

	
