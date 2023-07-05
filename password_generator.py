import random

#Characters that can be used to generate a password.
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"

#Ask the user for the length of the password.
password_length = int(input("Enter the length of the password: "))

#Initialise the variable where the password will be written to.
password = ""

#Generate a random password of a given length.
for i in range(password_length):
    password += random.choice(characters)

#Display the generated password on the screen.
print("Generated password:", password)

import random
import string

def generate_password(length):
    #Characters to be used in the password.
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    
    #Combining symbols.
    all_chars = letters + numbers + symbols
    
    #Generating a password.
    password = "".join(random.sample(all_chars, length))
    
    return password

#Generate an 8-character password
password = generate_password(8)
print(password)

import random
import string
import tkinter as tk

def generate_password(length):
    # Characters to be used in the password.
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    
    # Combining symbols.
    all_chars = letters + numbers + symbols
    
    # Generating a password.
    password = "".join(random.sample(all_chars, length))
    
    return password

def generate_new_password():
    password_length = int(length_entry.get())
    password = generate_password(password_length)
    password_label.config(text="Generated password: " + password)

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter the length of the password:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_new_password)
generate_button.pack()

password_label = tk.Label(root, text="")
password_label.pack()

root.mainloop()