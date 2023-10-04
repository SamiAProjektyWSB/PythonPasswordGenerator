import random
import string
import customtkinter
from tkinter import *
import tkinter


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

    """   def check_box_valid(self):
        if var_checkbox1.get() == "off":
            self.have_uppercase =="n"
        if var_checkbox2.get() == "on":
            self.have_num =="y"
        if var_checkbox3.get() == "on":
            self.have_special_character =="y"
        return self.have_uppercase, self.have_num, self.have_special_character
    """    

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
        self.password = "".join(random.sample(self.pwd_requirements(), self.length))
        return self.password


        



print("Welcome to password generator! Answer the questions below to help us generate perfect password for you :)")
pwd_len = int(input("How many characters should password contain?(max number of letters): "))
pwd_min_len = int(input("Min length: "))
pwd_upper = input("Do the password need to have uppercase letters?(y/n): ")
pwd_digit = input("Do the password need to contain numbers?(y/n): ")
pwd_special_character = input("Do the password need to contain special characters?(y/n): ")


pwd1 = Password(pwd_len, pwd_min_len, pwd_upper, pwd_digit, pwd_special_character, "")

pwd1.pwd_creator()
#print(pwd1.special_characters)

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("340x400")
app.title("Password Generator by Sami")

string_var = StringVar()
def button_down():
    wynik = pwd1.pwd_creator()
    string_var.set(str(pwd1.password))
    

#rama
frame = customtkinter.CTkFrame(master=app)
frame.pack(pady= 20, padx=60, fill="both", expand=True)
#tytuł
label1 = customtkinter.CTkLabel(master=frame, text="Password Generator", font=("Arial Black", 17))
label1.pack(pady=12, padx=10)
#pole wprowadzenia ile znaków ma mieć hasło

"""
#pola checkbox o duze znaki, znaki specjalne i cyfry
var_checkbox1 = tkinter.StringVar(value=on)
var_checkbox2 = tkinter.StringVar(value=on)
var_checkbox3 = tkinter.StringVar(value=on)

checkbox1 = customtkinter.CTkCheckBox(master=frame, text="Uppercase letters", command=pwd1.check_box_valid, variable = var_checkbox1, onvalue="on", offvalue="off")
checkbox1.pack(pady=12, padx=10)
checkbox2 = customtkinter.CTkCheckBox(master=frame, text="Digits", command=pwd1.check_box_valid, variable = var_checkbox2, onvalue="on", offvalue="off")
checkbox2.pack(pady=12, padx=10)
checkbox3 = customtkinter.CTkCheckBox(master=frame, text="Special characters", command=pwd1.check_box_valid, variable = var_checkbox3, onvalue="on", offvalue="off")
checkbox3.pack(pady=12, padx=10)
"""
#przycisk zatwierdzenia i generowania hasla
submit = customtkinter.CTkButton(master=frame, text="Generate Password", command=button_down)
submit.pack(pady=12, padx=10)

#wynik
label2 = customtkinter.CTkLabel(master=frame, text="Result:")
label2.pack(pady=12, padx=10)
pwd = customtkinter.CTkLabel(master=frame, text="n", width=120, fg_color=("white", "black"), textvariable = string_var)
pwd.pack(pady=12, padx=10)



app.mainloop()