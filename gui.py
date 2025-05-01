# Blue Prince is piece of shit game and the developer should delete system32 of his computer and possibly his brain too. :like:

import tkinter as tk
from tkinter import *
from tkinter import ttk, PhotoImage

# Functions

def passbuttonfunc():
    print("passbutton Clicked")

def logbuttonfunc():
    print("logbutton Clicked")

def exitbuttonfunc():    
    print("exitbutton Clicked")

# Main Window functions n shit
bgcolor = '#313131'

PassGen = Tk()
PassGen.title('PassGen') # Names the app at the top
PassGen.resizable(width = False, height = False) # Disables window resize

# Main Menu

# Canvas 
canv = Canvas(PassGen, width = 600, height = 500, bg = bgcolor)
canv.grid(row = 0, column = 0)

# Logo
logophoto = PhotoImage(file="./gui/placeholder.png")
canv.create_image(110, 110, image = logophoto)

# Text
canv.create_text(390, 110, text = "Welcome to PassGen", fill = "white", font = 'Helvectia 26 bold') # Welcome Text

# Password Generator Text stuff
PasswordGenText = '''
Password Generator, Here you can create a password after 
answering some questions that will affect your password, 
also you can also generate a One Time Password that 
you can use for throwaway accounts.
'''
canv.create_text(390, 260, text = PasswordGenText, fill = "white", font = 'Helvectia 10 bold')

# Logged Fies text stuff
LogFilesText = '''
Whenever you save a Generated Password, if it's OTP or a 
normal Password, it will be saved and you can access the 
files directly from this program
'''
canv.create_text(390, 350, text = LogFilesText, fill = "white", font = 'Helvectia 10 bold')

# Exit button
canv.create_text(300, 442, text = "What do you think this does?", fill = "white", font = 'Helvectia 10 bold')

# Password Menu button
passbutton = tk.Button(PassGen, text = "Password Generator", font='Helvectia 10 bold', width= 19, height= 2, command = passbuttonfunc)
passbutton.place(x=30, y=240)

# Password Logging Button
logbutton = tk.Button(PassGen, text = "Logged Files", font='Helvectia 10 bold', width= 19, height= 2, command = logbuttonfunc)
logbutton.place(x=30, y=330)

# Exit Button
exitbutton = tk.Button(PassGen, text = "EXIT", font='Helvectia 10 bold', width= 19, height= 2, command = exitbuttonfunc)
exitbutton.place(x=30, y=420)

# END OF MAIN MENU CODE.

PassGen.mainloop()