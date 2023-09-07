#I swear on my life and a half that this is my work. I did not use any type of A.I. assistance, or otherwise unfair advantages.
#If you need proof of my struggle to write this correctly, you can look at my GitHub: https://github.com/jddicaro/Compsci892981

print("Welcome to G.R.P.! (Grade Retrieval Program)")
name=input("\nLog in: ")
stuid=input("\nStudent ID/Password: ")
print("\nHello,",name+"!")
ans1=input("Would you like to view a class? (Y/n)")

if ans1=="Y" or ans1=="y" or ans1=="" or ans1=="yes" or ans1=="YES" or ans1=="Yes":
  course=input("\nWhat class would you like to view?\n")
  assignment=input("\nWhat assignment would you like to look at?\n")
  input("Please give me a moment while I retrieve your info... (ENTER to continue)")
  print("Here you go!\n\n",course,"\n\n",assignment,"\n\n",name,"\t\t",stuid,"\n\n Grade: \nComments: \nAssignment correctness: \nQuality of style: \nLate deduction: \nOverall score: \nComments: ")
  input("(ENTER to continue)")
  print("Thank you for using G.R.P.!\n")
  
elif ans1=="n" or ans1=="N" or ans1=="no" or ans1=="NO" or ans1=="No":
  print("Why did you even start this program, then?\n")

else:
  print("Dude, it's a yes/no question. You type either y or n. It's not hard. [ANSWERS LIKE \"nO\" OR \"yES/YeS/yEs/YEs/yeS\" WILL NOT BE ACCEPTED]\n")

print("Press ENTER to close program.")
