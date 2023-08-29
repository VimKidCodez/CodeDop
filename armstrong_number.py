"""

In an armstrong number is 153 , 407 , 9,etc

the cube of the digits added are equal to a number itself

for example:
	in 153
	1^3 = 1
	5^3 = 125
	3^3 = 27
	their sum = 1 +125+27 = 153 
	thus 153 is an armstrong number


"""

User_number = int(input("Enter number: "))
Sum = 0

temp = User_number

while temp >0:
	digit = temp% 10
	Sum = Sum + (digit**3)	
	temp = temp // 10
if Sum == User_number:
	print("It is an armstrong number.")
else:
	print("It is not an armstrong number.")