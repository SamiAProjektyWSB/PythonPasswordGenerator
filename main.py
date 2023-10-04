import random
import string


class Password:
    question = ''
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation
    def __init__(self, length: int, min_len: int, have_uppercase: str, have_num: str, have_special_character: str, result: str):
        # Run validation to received arguments
        assert length >= 0, f"Password length can't be negative"
        assert min_len >= 0, f"Password minimal length can't be negative"
        assert min_len <= length, f"Password minimal length can't be grater than password length"
        assert len(have_uppercase) <= 1 and have_uppercase == "y" or have_uppercase == "n", f"Only y or n"
        assert len(have_num) <= 1, f"Only y or n"
        assert len(have_special_character) <= 1, f"Only y or n"


        # Assign to self obejct
        self.result = result
        self.length =  length
        self.min_length = min_len
        self.have_uppercase = have_uppercase
        self.have_num = have_num
        self.have_special_character = have_special_character

    def pwd_requirements(self):
        self.result = self.letters
        if self.have_uppercase == "n" or self.have_uppercase =="N":
            self.result = self.result.lower()        
        if self.have_num == "y" or self.have_num =="Y":
            self.result += self.digits
        if self.have_special_character == "y" or self.have_special_character  =="Y":
            self.result += self.special_characters
        return self.result
    
    def pwd_creator(self):
        password = "".join(random.sample(self.pwd_requirements(), self.length))
        return print(password)
        



print("Welcome to password generator! Answer the questions below to help us generate perfect password for you :)")
pwd_len = int(input("How many characters should password contain?(max number of letters): "))
pwd_min_len = int(input("Min length: "))
pwd_upper = input("Do the password need to have uppercase letters?(y/n): ")
pwd_digit = input("Do the password need to contain numbers?(y/n): ")
pwd_special_character = input("Do the password need to contain special characters?(y/n): ")


pwd1 = Password(pwd_len, pwd_min_len, pwd_upper, pwd_digit, pwd_special_character, "")

pwd1.pwd_creator()
#print(pwd1.special_characters)