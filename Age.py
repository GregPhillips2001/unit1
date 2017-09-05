#Greg Phillips
#9/5/17
#Age.py

fullName = input("Write name here ")
age = int(input("Write age here "))
firstName, lastName = fullName.split()
print("Your first name has", len(firstName), "letters")
print("Your last name has", len(lastName), "letters")
print("Next year you will be", age+1, "years old")