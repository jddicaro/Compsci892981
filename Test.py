print("Welcome to G.R.P.! (Grade Retrieval Program)")
name=input("\nLog in: ")
stuid=input("\nStudent ID/Password: ")
print("\nHello,",name+"!")
ans1=input("Would you like to view a class? (Y/n)")
if ans1=="n"or"N":
    print("Why did you even start this program, then?")
else:
    if ans1!="Y"or"y"or"N"or"n":
        print("Dude, it's a Y/N question. It's not hard.")
    else:
        if ans1=="Y"or"y":
            course=input("\nWhat class would you like to view?\n")
            assignment=input("\nWhat assignment would you like to look at?\n")
            input("Please give me a moment while I retrieve your info... (ENTER to continue)")
            print("Here you go!\n\n ",course,"\n\n",assignment,"\n\n",name,"\t\t",stuid,"\n\n Grade: \nComments: \nAssignment correctness: \nQuality of style: \nLate deduction: \nOverall score: \nComments: ")
            input("(ENTER to continue)")
print("Thank you for using G.R.P.!")
