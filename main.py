                # "While loops go back on themselves. Thats all that loops are, they repeat themselves" - Maky, probably #
#####################################################################################################################################













#####################################################################################################################################
# Python Password Generator. It generates a Password for you bassed off a few user made inputs and then exports them into a text file.

import random
import time
import datetime
import os
import math

# BACK END
# Calculates how strong the generated passwords are.
def password_entropy(password: str) -> float:
    charset_size = 0
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    if has_lower:
        charset_size += 26
    if has_upper:
        charset_size += 26
    if has_digit:
        charset_size += 10
    if has_symbol:
        charset_size += 33  # Roughly printable special chars

    if charset_size == 0:
        return 0.0


    entropy = len(password) * math.log2(charset_size)

    if entropy < 28:
        strength = "Very weak"
    elif entropy < 36:
        strength = "Weak"
    elif entropy < 60:
        strength = "Reasonable"
    elif entropy < 128:
        strength = "Strong"
    else:
        strength = "Very Strong" 

    return entropy, strength

# Calculates how strong the users personal  passwords are.
def personal_entropy():

    userpass = input("Input the password so we can calculate the strength for you: ")
    entropy, strength = password_entropy(userpass)
    
    print(f"The BIT strength of your password is: {entropy} which means your password is {strength}")
    
    time.sleep(10)
    
    return

# Function that will ask the questions for the password.
def PasswordQuestion():
    print("Im going to ask you some questions. Answer them how ever you like, Keep in mind all your answers will affect your password and it's length.")

    global word, rng, symbol, color, shape # Makes the answers global.

    word = input("Write down a word. It can be anything you like. Answer: ")                     # Word
    rng =  input("Write down a random number. Answer: ")                                         # Random Number
    symbol = input("Write down a special character or symbol. Answer: ")                         # Random Symbol
    color = input("write down a color, It can be your favourite or it can be random Answer: ")   # Color
    shape = input("Write down a shape, any shape Answer: ")                                      # Shape
    
    return 

# Password Generator
def PasswordGenerator():
    
    questions = [word, rng, symbol, color, shape]      # List with variables from questions.
    random.shuffle(questions)
    GeneratedPassword = ''.join(questions)
    
    # Enrtopy calculator.
    entropy, strength = password_entropy(GeneratedPassword)

    print(f"Your password is: {GeneratedPassword}. It's Entropy score is {entropy} which means your password is {strength}")     # Shows the password on screen.

    # Ask if you want to save
    savePass = input("Would you like to save the password? (Y/N): ").lower()

    if savePass == 'y':
        print("Saving password.")
        with open("GeneratedPassword.txt", "a") as f:
            x = datetime.datetime.now()           
            f.write(f"Password Generated on: {x.strftime("%a %d %b %y. At: %H:%M")} Password: {GeneratedPassword} with an Entropy Score of: {entropy} which means the passwords is {strength}\n")           # After file generates it will add the content of the generated password into the file
    elif savePass == 'n':
        print("Ok, thank you for using my Password Generator.")
        
    return

def OTP():

    # List of all alphabet letters. ALl symbols and all numbers
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = list("`-=[]\\;',./~!@#$%^&*()_+{}|:\"<>?")
    char_pool = letters + numbers + symbols

    
    # Parameters for the otp

    while True:
        OTPlength = input("How many characters do you want the password to be?")
        try:
            OTPlength = int(OTPlength)
            break
        except ValueError:
            print("Needs to be a NUMBER.")
            
    # print the OTP
    OTPGenerator = ''.join(random.choices(char_pool, k = OTPlength))        # Randomly pick a range of letters, symbols and numbers and shuffle them around.
    entropy, strength = password_entropy(OTPGenerator)
    
    print(f"Your One Time Password is: {OTPGenerator} with a Entropy Score of: {entropy} which means your password is {strength}")
    
    # Ask if you want to save the OTP
    saveOTP = input("Would you like to save the One time password? (Y/N)").lower()

    if saveOTP == 'y':
        print("Saving OTP.")
        with open("LoggedOTPs.txt", "a") as f: 
            x = datetime.datetime.now()                                                    
            f.write(f"One Time Password Generated on: {x.strftime("%a %d %b %y. At: %H:%I")} Password: {OTPGenerator} with a Entropy Score of: {entropy} which means the password is {strength}\n")    # After file generates it will add the content of the OTP into the file including when the password was created
            print("Ok, One Time Password Saved.")
    elif saveOTP == 'n':
        print("Ok, we won't save it.")
    
    # Implement a timer that will regenerate the OTP after 5 minutes and save it to the file, if one is made.

    return

# FRONT END

name = input("Hi, Whats your name?: ")      # Asks the user what their name is.

# Option screen.

while True:

    # menu look 
    print()
    print(f"Hey {name} welcome to:") # Will add ASCII Art for the Logo and name.
    print()
    print('''
**MENU**"
Select an Option.
P = Password Generator
O = One Time Password Generator
C = Cleans all the generated password logs.
U = Password Strength Calculator. Test if your password is strong.
?P = Opens your GeneratedPassword.txt if one exists.
?O = Opens your LoggedOTPs.txt if one exists.
X = Closes the program 
''')

    menu = input("Select your option: ").lower() # input for the menu

    if menu == 'p':
            print("Fantastic")
            PasswordQuestion()
            PasswordGenerator()  
    
    elif menu == 'o':
        print("Ok, let me generate you a one time password.")
        OTP()
    
    elif menu == 'c':
        print("Cleaning log files...")
        files = ['GeneratedPassword.txt', 'LoggedOTPs.txt']
        for file_name in files:
                if os.path.exists(file_name):
                    os.remove(file_name)
                    print("Files Removed")
        else:
            print("No files to be removed.")
            time.sleep(5)
    
    elif menu == 'u':
        personal_entropy() 

    elif menu == '?o':
        print("Opening LoggedOTPs.txt")
        if os.path.exists("LoggedOTPs.txt"): # Fix not finding file
            f = open("LoggedOTPs.txt")  # Open file in notepad
        else:
            print("File not found.")
    
    elif menu == '?p':
        print("Opening GeneratedPassword.txt")
        if os.path.exists("GeneratedPassword.txt"): # Fix not finding file
            f = open("GenerartedPassword.txt") # Open file in notepad
        else:
            print("File not found.")
    
    elif menu == 'x':
        print("Program shutting down...")
        time.sleep(5)
        break
