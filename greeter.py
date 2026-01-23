# creating a simple program that asks for the user's name and birth year, then tells them their current age!
user_name = input("Enter your name: ")
birth_year = input("What year were you born? ")
birth_year_num = int(birth_year)

current_year = 2026
user_age = current_year - birth_year_num

print ("Hello " + user_name + "! " + "You are " + user_age + "years old." )