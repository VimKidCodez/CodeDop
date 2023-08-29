"""
Rule based ai use a few IF-ELSE parameters to predict or take decisions from the given data

eg: Estimate the probality of something happening

"""

user_choice = str(input("Are you hungry? YES OR NO: "))

if user_choice == "NO":
	print("Go to sleep")
elif user_choice == "YES":
	user_choice_2 = str(input("Do you have 20$?: "))
	if user_choice_2 == "NO":
		print("Work at WageDonalds and buy Burger.")
	elif user_choice_2 == "YES":
		print("Eat at a restaraunt.")

# These are static model as these do not impove from the previous data given by the user