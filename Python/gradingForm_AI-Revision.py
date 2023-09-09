#THIS CODE WAS REVISED BY AI, PLEASE DO NOT TAKE AS A GRADE!
#Well, I did add a bit to it after and forgot to save that to a new file, so i'll just comment where my code is

#AI
def query_yes_no(question):
	"""Ask a yes/no question via standard input and return the answer. If invalid input is given, the user will be asked until they acutally give valid input.

	Args:
		question(str): A question that is presented to the user.

	Returns:
		A bool indicating whether user has entered yes or no.

	Side Effects:
		Blocks program execution until valid input(y/n) is given.
	"""
	yes_list = ["yes", "y"]
	no_list = ["no", "n"]
	prompt = question + " (y/n) "
	while True:
		choice = input(prompt).lower()
		if choice in yes_list:
			return True
		elif choice in no_list:
			return False
		else:
			print("Please respond with 'y' or 'n'")

#me
print("[THIS CODE WAS REVISED BY AI, PLEASE DO NOT TAKE AS A GRADE]")
print("Welcome to G.R.P.! (Grade Retrieval Program)")
name = input("\nLog in: ")
stuid = input("\nStudent ID/Password: ")
print("\nHello,", name + "!")

ans1 = query_yes_no("Would you like to view a class? ")

if ans1:
	course = input("\nWhat class would you like to view?\n")
	assignment = input("\nWhat assignment would you like to look at?\n")
	input("Please give me a moment while I retrieve your info... (ENTER to continue)")
	print("Here you go!\n\n", course, "\n\n", assignment, "\n\n", name, "\t\t", stuid, "\n\n Grade: \nComments: \nAssignment correctness: \nQuality of style: \nLate deduction: \nOverall score: \nComments: ")
	input("(ENTER to continue)")
	while True:
		#I added this while true loop after looking at what Bard did at the beginning, bc I thought it was cool
		ans2 = query_yes_no("Would you like to check another grade?")
		if ans2: 
			course = input("\nWhat class would you like to view?\n")
			assignment = input("\nWhat assignment would you like to look at?\n")
			input("Please give me a moment while I retrieve your info... (ENTER to continue)")
			print("Here you go!\n\n", course, "\n\n", assignment, "\n\n", name, "\t\t", stuid, "\n\n Grade: \nComments: \nAssignment correctness: \nQuality of style: \nLate deduction: \nOverall score: \nComments: ")
			input("(ENTER to continue)")
		else:
			print("Thank you for using G.R.P.!\n")
			break
else:
	print("Why did you even start this program, then?\n")

input("Press ENTER to close program.")
