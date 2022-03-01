#Liam Davis

#getting grade
grade= int(input("What is your assignment grade? "))
verify = print(f"Your grade of {grade}.")

#result if statements
if grade >= 88: 
    print("That is a letter grade of a A!")
elif grade >=80:
    print("That is a letter grade of a B.")
elif grade >=67:
    print("That is a letter grade of a C.")
elif grade >=60:
    print("That is a letter grade of a D.")
elif grade >=59:
    print("That is a letter grade of a F.")

#to continue
cont=input("Would you like to continue? (Y/N): ").lower().strip()
if cont == "y":
    return
elif cont== "n":
    print("Goodbye")
