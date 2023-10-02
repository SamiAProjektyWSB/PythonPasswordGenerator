import random

letters = "abcdefghjklmnoprstuwyzx"
digits = "1234567890"
special_characters = "!@#$%^&*()_-+=[]}{/?><,.;':`"
up_letters = letters.upper()


password = letters


print("Welcome to password generator! Answer the questions below to help us generate perfect password for you :)")
input_pass_len = int(input("How many characters should password contain?(max number of letters): "))
pass_upper = input("Do the password need to have uppercase letters?(y/n): ")
pass_digit = input("Do the password need to contain numbers?(y/n): ")
pass_special_character = input("Do the password need to contain special characters?(y/n): ")


#inputs handling
if  input_pass_len < 1:
    print("Password length can't be less than 1")
else: 
    pass_len = input_pass_len

if pass_upper == "y" or pass_upper =="Y":
    pass_upper = True
else:
    pass_upper = False

if pass_digit == "y" or pass_digit =="Y":
    pass_digit = True
else:
    pass_digit = False

if pass_special_character == "y" or pass_special_character =="Y":
    pass_special_character = True
else:
    pass_special_character = False

#password generating

if pass_upper == True:
    password = password + up_letters

if pass_digit == True:
    password = password + digits

if pass_special_character == True:
    password += special_characters


password = "".join(random.sample(password, pass_len))

print(password)