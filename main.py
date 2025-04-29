# "While loops go back on themselves. Thats all that loops are, they repeat themselves" - Maky, probably

# Python Password Generator. It generates a Password for you bassed off a few user made inputs and then exports them into a text file.

import random

# BACK END

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
    
    print("Your password is:", GeneratedPassword)     # Shows the password on screen.

    # Ask if you want to save
    savePass = input("Would you like to save the password? (Y/N)").lower()

    if savePass == 'y':
        print("Saving password.")
        with open("GeneratedPassword.txt", "a") as f:           # After file generates it will add the content of the generated password into the file
            f.write(GeneratedPassword)
    elif savePass == 'n':
        print("Ok, thank you for using my Password Generator.")
        
    return


# FRONT END


# Welcome Screen
name = input("Hi, Whats your name?: ")                      # Asks the user what their name is.
print(f"Hello {name}")                                      # Welcomes the User.

# Make password? Question
while True:
    make_password = input("Do you want me to make you a password? (Y/N): ").strip().lower()

    if make_password == 'y':
        print("Fantastic let's continue")
        PasswordQuestion()
        PasswordGenerator()
        break
    elif make_password == 'n':
        print("Well Ok, Thanks for trying my program")
        break
    else:
        print("Please answer YES 'Y' or NO 'N'")