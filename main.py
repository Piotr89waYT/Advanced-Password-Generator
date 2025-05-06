#"While loops go back on themselves. Thats all that loops are, they repeat themselves" - Maky, probably
# Python Password Generator. It generates a Password for you bassed off a few user made inputs and then exports them into a text file.
# Vibe coding went crazy for this 🔥🔥🔥🔥🔥🔥🔥🔥
import random
import time
import datetime
import os
import math
import webbrowser

import tkinter as tk
from tkinter import PhotoImage, Image

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

    os.system('cls')
    
    return

# Function that will ask the questions for the password.
# def PasswordQuestion():
    print("Im going to ask you some questions. Answer them how ever you like, Keep in mind all your answers will affect your password and it's length.")

    global word, rng, symbol, color, shape # Makes the answers global.

    '''word = input("Write down a word. It can be anything you like. Answer: ")                  # Word
    rng =  input("Write down a random number. Answer: ")                                         # Random Number
    symbol = input("Write down a special character or symbol. Answer: ")                         # Random Symbol
    color = input("write down a color, It can be your favourite or it can be random Answer: ")   # Color
    shape = input("Write down a shape, any shape Answer: ")'''                                   # Shape
    
    PasswordGenerator()

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
            f.write(f"Password Generated on: {x.strftime('%a %d %b %y. At: %H:%M')} Password: {GeneratedPassword} with an Entropy Score of: {entropy} which means the passwords is {strength}\n")           # After file generates it will add the content of the generated password into the file
            time.sleep(3)
            os.system('cls')
    elif savePass == 'n':
        print("Ok, thank you for using my Password Generator.")
        time.sleep(3)
        os.system('cls')
        
    return

def savePassword(password: str, entropy: float, strength: str):
    """
    Saves the generated password along with its entropy and strength to a file.
    :param password: The generated password.
    :param entropy: The entropy score of the password.
    :param strength: The strength rating of the password.
    """
    try:
        print("Saving password...")
        with open("GeneratedPassword.txt", "a") as f:
            x = datetime.datetime.now()
            f.write(
                f"Password Generated on: {x.strftime('%a %d %b %y. At: %H:%M')} "
                f"Password: {password} with an Entropy Score of: {entropy:.2f} "
                f"which means the password is {strength}\n"
            )
        print("Password saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving the password: {e}")

def OTP():

    # List of all alphabet letters. ALl symbols and all numbers
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = list("`-=[]\\;',./~!@#$%^&*()_+{}|:\"<>?")
    char_pool = letters + numbers + symbols

    
    # Parameters for the otp

    while True:
        OTPlength = input("How many characters do you want the password to be?: ")
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
    saveOTP = input("Would you like to save the One time password? (Y/N): ").lower()

    if saveOTP == 'y':
        print("Saving OTP.")
        with open("LoggedOTPs.txt", "a") as f: 
            x = datetime.datetime.now()                                                    
            f.write(f"One Time Password Generated on: {x.strftime('%a %d %b %y. At: %H:%I')} Password: {OTPGenerator} with a Entropy Score of: {entropy} which means the password is {strength}\n")    # After file generates it will add the content of the OTP into the file including when the password was created
            print("Ok, One Time Password Saved.")
            time.sleep(3)
            os.system('cls')
    elif saveOTP == 'n':
        print("Ok, we won't save it.")
        time.sleep(3)
        os.system('cls')
    
    # Implement a timer that will regenerate the OTP after 5 minutes and save it to the file, if one is made.

    return

def cleanupfunc():
        os.system('cls')
        print("Cleaning log files...")
        files = ['GeneratedPassword.txt', 'LoggedOTPs.txt']
        for file in files:
                if os.path.exists(file):
                    os.remove(file)
                    print("Files Removed")
        else:
            print("No files to be removed.")
            time.sleep(3)


# ===FRONT END===


# Making main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("600x500")
window.resizable(False, False)
window.configure(bg="#313131")

def windowUpdate():
    # Destroy all widgets in the window
    for widget in window.winfo_children():
        widget.destroy()

def createButton(window, text, command, width=150, height=40, font=("Helvetica", 14), bg="#414141", fg="#ffffff"):
    """
    A reusable function to create a styled button.
    :param window: The parent window where the button will be placed.
    :param text: The text to display on the button.
    :param command: The function to call when the button is clicked.
    :param width: The width of the button.
    :param height: The height of the button.
    :param font: The font of the button text.
    :param bg: The background color of the button.
    :param fg: The foreground (text) color of the button.
    :return: A configured tk.Button instance.
    """
    return tk.Button(
        window,
        text=text,
        font=font,
        bg=bg,
        fg=fg,
        highlightthickness=0,
        command=command,
    )

# Drawing main menu
def drawMainMenu():
    windowUpdate()  # Clear the window
    global mainMenuAccentPhoto  # Keep a reference to the image

    # Load the image
    mainMenuAccentPhoto = PhotoImage(file="./gui/placeholder.png")
    mainMenuAccentPhotoLabel = tk.Label(window, image=mainMenuAccentPhoto, bg="#313131")
    mainMenuAccentPhotoLabel.place(x=25, y=25)  # Place the image at (25, 25)

    # Add text next to the image
    imageTextLabel = tk.Label(
        window,
        text="Piotr's Password Generator\nCreate secure passwords easily.",
        font=("Helvetica", 15, "bold"),
        fg="#ffffff",
        bg="#313131",
        justify="left",
    )
    imageTextLabel.place(x=220, y=75)  # Place the text next to the image

    # Calculate button dimensions
    button_width = 560  # Fixed width for buttons
    button_height = 60  # Height for each button
    button_spacing = 20  # Spacing between buttons
    lower_half_start = 250  # Starting y-coordinate for the lower half

    # Password Menu Button
    passwordMenuButton = tk.Button(
        window,
        text="Password Menu",
        font=("Helvetica", 14),
        bg="#414141",  # Button background color
        fg="#ffffff",  # Button text color
        highlightthickness=0,  # Remove the white highlight border
        highlightbackground="#414141",  # Match the button background
        highlightcolor="#414141",  # Match the button background
        command=drawPasswordMenu  # Replace with actual functionality
    )
    passwordMenuButton.place(
        x=(600 - button_width) // 2,  # Center horizontally
        y=lower_half_start,  # Start at the lower half
        width=button_width,
        height=button_height
    )

    # Password Log Files Button
    logFilesButton = tk.Button(
        window,
        text="Password Log Files",
        font=("Helvetica", 14),
        bg="#414141",
        fg="#ffffff",
        highlightthickness=0,
        highlightbackground="#414141",
        highlightcolor="#414141",
        command=lambda: print("Password Log Files clicked")  # Replace with actual functionality
    )
    logFilesButton.place(
        x=(600 - button_width) // 2,  # Center horizontally
        y=lower_half_start + button_height + button_spacing,  # Below the first button
        width=button_width,
        height=button_height
    )

    # Exit Button
    exitButton = tk.Button(
        window,
        text="Exit",
        font=("Helvetica", 14),
        bg="#414141",
        fg="#ffffff",
        highlightthickness=0,
        highlightbackground="#414141",
        highlightcolor="#414141",
        command=window.quit  # Closes the application
    )
    exitButton.place(
        x=(600 - button_width) // 2,  # Center horizontally
        y=lower_half_start + 2 * (button_height + button_spacing),  # Below the second button
        width=button_width,
        height=button_height
    )

def drawPasswordMenu():
    # Clear the window
    windowUpdate()

    # Add the title
    titleLabel = tk.Label(
        window,
        text="Password Menu",
        font=("Helvetica", 30, "bold"),
        fg="#ffffff",
        bg="#313131",
    )
    titleLabel.place(relx=0.5, y=50, anchor="center")  # Centered at the top

    # Load the back button image
    global backButtonImage  # Keep a reference to the image to prevent garbage collection
    backButtonImage = PhotoImage(file="./gui/backbutton.png")

    # Add the Back Button
    backButton = tk.Button(
        window,
        image=backButtonImage,  # Use the image for the button
        bg="#313131",  # Match the background color
        highlightthickness=0,  # Remove white highlight
        bd=0,  # Remove border
        command=drawMainMenu  # Navigate back to the main menu
    )
    backButton.place(x=10, y=10, width=40, height=40)  # Place in the top-left corner

    # Button dimensions
    button_width = 400
    button_height = 50
    button_spacing = 20
    start_y = 150  # Starting y-coordinate for the buttons

    # Password Generator Button
    passwordGeneratorButton = tk.Button(
        window,
        text="Password Generator",
        font=("Helvetica", 14),
        bg="#414141",  # Darker background for dark mode
        fg="#ffffff",  # White text for contrast
        highlightthickness=0,
        command=drawQuestionScreen  # Call drawQuestionScreen when clicked
    )
    passwordGeneratorButton.place(
        relx=0.5, y=start_y, anchor="center", width=button_width, height=button_height
    )

    # One Time Password Generator Button
    otpButton = tk.Button(
        window,
        text="One Time Password Generator",
        font=("Helvetica", 14),
        bg="#414141",  # Darker background for dark mode
        fg="#ffffff",  # White text for contrast
        highlightthickness=0,
        command=lambda: print("One Time Password Generator clicked")  # Replace with actual functionality
    )
    otpButton.place(
        relx=0.5, y=start_y + button_height + button_spacing, anchor="center", width=button_width, height=button_height
    )

    # Password Strength Checker Button
    strengthCheckerButton = tk.Button(
        window,
        text="Password Strength Checker",
        font=("Helvetica", 14),
        bg="#414141",  # Darker background for dark mode
        fg="#ffffff",  # White text for contrast
        highlightthickness=0,
        command=lambda: print("Password Strength Checker clicked")  # Replace with actual functionality
    )
    strengthCheckerButton.place(
        relx=0.5, y=start_y + 2 * (button_height + button_spacing), anchor="center", width=button_width, height=button_height
    )

def drawQuestionScreen():
    # Clear the window
    windowUpdate()

    # Questions and their corresponding prompts
    questions = [
        "Write down a word. It can be anything you like:",
        "Write down a random number:",
        "Write down a special character or symbol:",
        "Write down a color (e.g., your favorite color):",
        "Write down a shape (e.g., circle, square):"
    ]
    answers = []  # To store user inputs
    current_question_index = [0]  # Use a list to allow modification inside nested functions

    # Function to handle the next question
    def nextQuestion(event=None):  # Add `event` to handle key binding
        # Get the current input and store it
        if current_question_index[0] > 0:  # Skip storing on the first question
            answers.append(entry.get())
            entry.delete(0, tk.END)  # Clear the entry field

        # Check if all questions are answered
        if current_question_index[0] == len(questions):
            # Generate the password using the answers
            generatePassword(answers)
            return

        # Update the question label
        questionLabel.config(text=questions[current_question_index[0]])
        current_question_index[0] += 1

    # Add a title
    titleLabel = tk.Label(
        window,
        text="Answer the Following Questions",
        font=("Helvetica", 20, "bold"),
        fg="#ffffff",
        bg="#313131",
    )
    titleLabel.place(relx=0.5, y=50, anchor="center")

    # Add a question label
    questionLabel = tk.Label(
        window,
        text=questions[0],  # Start with the first question
        font=("Helvetica", 14),
        fg="#ffffff",
        bg="#313131",
        wraplength=500,  # Wrap text if it's too long
        justify="center",
    )
    questionLabel.place(relx=0.5, y=150, anchor="center")

    # Add an entry widget for user input
    entry = tk.Entry(
        window,
        font=("Helvetica", 14),
        bg="#414141",
        fg="#ffffff",
        insertbackground="#ffffff",  # Cursor color
        highlightthickness=0,
    )
    entry.place(relx=0.5, y=200, anchor="center", width=400, height=30)

    # Bind the Enter key to the nextQuestion function
    entry.bind("<Return>", nextQuestion)

    # Add a "Next" button
    nextButton = tk.Button(
        window,
        text="Next",
        font=("Helvetica", 14),
        bg="#414141",
        fg="#ffffff",
        highlightthickness=0,
        command=nextQuestion,  # Call the nextQuestion function
    )
    nextButton.place(relx=0.5, y=300, anchor="center", width=100, height=40)

    # Start with the first question
    nextQuestion()


def generatePassword(answers):
    # Shuffle and combine the answers to create the password
    random.shuffle(answers)
    GeneratedPassword = ''.join(answers)

    # Calculate entropy and strength
    entropy, strength = password_entropy(GeneratedPassword)

    # Clear the screen
    windowUpdate()

    # Create and display the generated password label
    global passwordLabel, entropyLabel  # Make the labels global to update them later
    passwordLabel = tk.Label(
        window,
        text=f"Your password is:\n{GeneratedPassword}",
        font=("Helvetica", 16, "bold"),
        fg="#ffffff",
        bg="#313131",
        wraplength=500,
        justify="center",
    )
    passwordLabel.place(relx=0.5, y=150, anchor="center")

    # Create and display the entropy and strength label
    entropyLabel = tk.Label(
        window,
        text=f"Entropy Score: {entropy:.2f}\nPassword Strength: {strength}",
        font=("Helvetica", 14),
        fg="#ffffff",
        bg="#313131",
        justify="center",
    )
    entropyLabel.place(relx=0.5, y=250, anchor="center")

    # Add a "Save Password" button
    saveButton = tk.Button(
        window,
        text="Save Password",
        font=("Helvetica", 14),
        bg="#414141",
        fg="#ffffff",
        highlightthickness=0,
        command=lambda: savePassword(GeneratedPassword, entropy, strength)
    )
    saveButton.place(relx=0.5, y=350, anchor="center", width=150, height=40)


    # Add a "Back to Menu" button
    backButton = tk.Button(
        window,
        text="Back to Menu",
        font=("Helvetica", 14),
        bg="#414141",
        fg="#ffffff",
        highlightthickness=0,
        command=drawPasswordMenu,
    )
    backButton.place(relx=0.5, y=470, anchor="center", width=150, height=40)



drawMainMenu()

window.mainloop()