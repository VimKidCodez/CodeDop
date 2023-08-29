

print("Welcome to Lucky number storer")
user_choice = int(input('1 to enter lucky number , 2 to view lucky number:'))

if user_choice == 1:
	f = open('lku.txt',"w")
	user_input = str(input('Enter number: '))
	f.truncate()
	f.write(user_input)
	f.close()
elif user_choice == 2:
	f_r = open("lku.txt", "r")
	print(f_r.read())