values=[1,2,3]
print(f"max value is:{max(values)}")

max_value= values[0]
for x in values:
	if x>max_value:
		max_value=x
print(f"max value is:{max_value}")

min_value=values[0]
for x in values:
	if x<min_value:
		min_value=x
print(f"min value is:{min_value}")

sum=0
for x in values:
	sum=sum+x
print(f"sum is: {sum}")

print(f"average is: {sum/len(values)}")

values.sort()

print(f"Median of the list is: {values[len(values)//2]}")