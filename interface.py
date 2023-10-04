import customtkinter
from tkinter import *
from main import *
import tkinter


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