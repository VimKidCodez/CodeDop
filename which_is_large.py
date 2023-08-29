print("Test")

number_1 = int(input('Enter number: '))
number_2 = int(input('Enter number: '))
number_3 = int(input('Enter number: '))

if number_1 > number_2 and number_1 > number_3:
	large = number_1
elif number_2 > number_1 and number_2 > number_3:
	large = number_2
else:
	large = number_3

print("The large number is :",large)