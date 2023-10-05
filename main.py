import random
import string
import tkinter as tk
import pyperclip
import customtkinter

# GUI setting
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("340x500")
app.title("Password Generator by Sami")

# Class responsible for generating passwords logic
class PasswordGenerator:
    def __init__(self):
        self.result = None
        self.letters = string.ascii_letters
        self.digits = string.digits
        self.special_characters = string.punctuation

    def generate_password(self, length, use_uppercase, use_digits, use_special_characters):
        password_characters = self.letters

        if not use_uppercase:
            password_characters = password_characters.lower()

        if use_digits:
            password_characters += self.digits

        if use_special_characters:
            password_characters += self.special_characters

        self.result = ''.join(random.sample(password_characters, length))

# Function responsible for generating password
def generate_password():
    length = int(entry_length.get())
    use_uppercase = var_uppercase.get() == 1
    use_digits = var_digits.get() == 1
    use_special_characters = var_special_characters.get() == 1

    generator = PasswordGenerator()
    generator.generate_password(length, use_uppercase, use_digits, use_special_characters)
    generated_password.set(generator.result)


def copy_to_clipboard():
    password = generated_password.get()
    if password:
        pyperclip.copy(password)


frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand=True)


label_title = customtkinter.CTkLabel(master=frame, text="Password Generator", font=("Arial Black", 17))
label_title.pack(pady=12, padx=10)

# Password lenght input
entry_length = customtkinter.CTkEntry(master=frame)
entry_length.pack(pady=12, padx=10)
entry_length.insert(0, "12")  # 12 is default value

# Checkboxes
var_uppercase = tk.IntVar(value=1)
var_digits = tk.IntVar(value=1)
var_special_characters = tk.IntVar(value=1)

checkbox_frame = customtkinter.CTkFrame(master=frame)
checkbox_frame.pack(pady=12, padx=10)

checkbox_uppercase = customtkinter.CTkCheckBox(master=checkbox_frame, text="Uppercase letters", variable=var_uppercase)
checkbox_uppercase.grid(row=0, column=0, sticky="w")

checkbox_digits = customtkinter.CTkCheckBox(master=checkbox_frame, text="Digits", variable=var_digits)
checkbox_digits.grid(row=1, column=0, sticky="w")

checkbox_special_characters = customtkinter.CTkCheckBox(master=checkbox_frame, text="Special characters", variable=var_special_characters)
checkbox_special_characters.grid(row=2, column=0, sticky="w")

# Password Generate button
button_generate = customtkinter.CTkButton(master=frame, text="Generate Password", command=generate_password)
button_generate.pack(pady=12, padx=10)

# Result display
label_result = customtkinter.CTkLabel(master=frame, text="Result:")
label_result.pack(pady=12, padx=10)

generated_password = tk.StringVar()
label_password = customtkinter.CTkLabel(master=frame, textvariable=generated_password, width=120, fg_color=("white", "black"))
label_password.pack(pady=12, padx=10)

# Copy to clipboard button
button_copy = customtkinter.CTkButton(master=frame, text="Copy", command=copy_to_clipboard)
button_copy.pack(pady=12, padx=10)

app.mainloop()