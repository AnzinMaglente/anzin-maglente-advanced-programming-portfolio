"""
Exercise 1 - Maths Quiz

[Your solution should not be more than 250 lines]

The student is tasked with developing a program that presents the user
with a quiz of arithmetric problems.
"""

from tkinter import *
from tkinter import ttk
import random

difficulty = "none"
progress = 0
score = 0
answer = 0
value1 = 0
value2 = 0
arithOperation = 0
answer_text = ""
mistakeCount = 0
totalMistakes = 0

def clearRoot():
    """ This function is used to erase all of the items within
    the root window. """

    for item in root.winfo_children():                          # The for loop is used to select every item inside the window/root.
        item.destroy()                                          # The ".destory" deletes the item from the window.

def displayMenu():
    """ This function is used to display the difficulty levels of the
    game, that being: Easy, Medium, and Hard. """

    global score, progress, mistakeCount, answer_text, totalMistakes
    # The global tag allows for global variables to be affected in the function.

    score = 0
    progress = 0
    mistakeCount = 0
    answer_text = ""
    totalMistakes = 0
    # The aforementioned variables are used to reset the said variables for future playthroughs.
    
    clearRoot()

    ttk.Label(root,                                             # Labels are used to print out text inside the window.
              text="Arithm Quiz",                               # Text is used to store the text to be seen from the user.
              font=("Lato", 45, 'bold')                         # This parameter changes how the text's font, size, and style.
              ).place(relx=0.5, rely=0.2, anchor=CENTER)        # ".place" is used for precise positioning.
                                                                # relx and rely is used to position the variable properly using window as a reference.
                                                                # anchor aligns the text to a certain position.

    ttk.Label(root, 
              text="Hello, welcome to Arithm Quiz. Where you will be answering some"
              ).place(relx=0.5, rely=0.375, anchor=CENTER)
    
    ttk.Label(root, 
              text="arithmetic questions. If you want to start, pick a difficulty."
              ).place(relx=0.5, rely=0.4375, anchor=CENTER)
    
    # Buttons are interactable objects in which allows the user to select several options.
    # In this program, they are used to allow the user to choose their difficulty.
    ttk.Button(root, 
               text="Easy", 
               command=lambda: randomInt(difficulty = "easy")   # Command is used to activate a certain function when the button is pressed.
               ).place(relx=0.3, rely=0.55, anchor=CENTER)
    
    ttk.Button(root, 
               text="Moderate", 
               command=lambda: randomInt(difficulty = "moderate")
               ).place(relx=0.5, rely=0.55, anchor=CENTER)
    
    ttk.Button(root, 
               text="Advanced", 
               command=lambda: randomInt(difficulty = "advanced")
               ).place(relx=0.7, rely=0.55, anchor=CENTER)
    
    ttk.Button(root, 
               text="Quit", 
               command=root.destroy                             # This completely closes the window/root.
               ).place(relx=0.5, rely=0.7, anchor=CENTER)

def randomInt(difficulty):
    """ This function is used to determine the values used in each question
    It should be based on the difficulty level. """

    if (difficulty == "easy"):
        value1 = random.randint(0, 9)                           # randint gets a certain number between the minimum and maximum values.
        value2 = random.randint(0, 9)
        decideOperation(value1, value2, difficulty)
    elif (difficulty == "moderate"):
        value1 = random.randint(0, 99)
        value2 = random.randint(0, 99)
        decideOperation(value1, value2, difficulty)
    elif (difficulty == "advanced"):
        value1 = random.randint(0, 999)
        value2 = random.randint(0, 999)
        decideOperation(value1, value2, difficulty)

def decideOperation(value1, value2, difficulty):
    """ This function is used to decide if the current problem should
    involve addition or subtraction. """

    arithOperation = random.randint(0, 1)
    if arithOperation == 0:
        answer = value1 + value2
        displayProblem(value1, value2, answer, arithOperation, difficulty)
    elif arithOperation == 1:
        answer = value1 - value2
        displayProblem(value1, value2, answer, arithOperation, difficulty)

def displayProblem(value1, value2, answer, arithOperation, difficulty):
    """ This function is used to display the current problem and accept
    any answer from the user. """

    global score, progress, answer_text
    clearRoot()

    progressbar = ttk.Progressbar()                             # The progressbar is added to allow users to know where they are at in the quiz.
    progressbar.step(progress)                                  # ".step" increases the bar to a certain degree.
    progressbar.place(relx=0.5, rely=0.12, width=350, anchor=CENTER)

    ttk.Label(root, 
              text="Your problem is...", 
              font=("Lato", 25, 'bold')
              ).place(relx=0.5, rely=0.25, anchor=CENTER)

    if (arithOperation == 0):
        ttk.Label(root,
                  text=(str(value1) + " + " + str(value2)), 
                  font=("Lato", 15)
                  ).place(relx=0.5, rely=0.4, anchor=CENTER)
    
    elif (arithOperation == 1):
        ttk.Label(root, 
                  text=(str(value1) + " - " + str(value2)), 
                  font=("Lato", 15)
                  ).place(relx=0.5, rely=0.4, anchor=CENTER)
    
    ttk.Label(root, 
              text="Your Answer", 
              font=("Lato", 15)
              ).place(relx=0.5, rely=0.54, anchor=CENTER)
    
    entry = Entry(root,                                          # Entry is used to get a string variable from the user.
                  font=('Century 12'), 
                  width=20)
    entry.place(relx=0.5, rely=0.64, anchor=CENTER)
    
    ttk.Button(root, 
               text="Submit", 
               command=lambda: isCorrect(value1, value2, entry, answer, arithOperation, difficulty, progressbar)
               ).place(relx=0.5, rely=0.80, anchor=CENTER)
    
    ttk.Label(root, 
              text=(answer_text), 
              font=("Lato", 10)
              ).place(relx=0.5, rely=0.9, anchor=CENTER)

def isCorrect(value1, value2, entry, answer, arithOperation, difficulty, progressbar):
    """ This function is used to check if the user's answer is correct
    and displays an appropriate message. """

    global score, progress, mistakeCount, answer_text, totalMistakes

    try:
        userAnswer = int(entry.get())                               # ".get" gathers the value from a certain variable.

        if (userAnswer == answer):                                  # This checks if the userAnswer is equal to the correct answer.
            progress += 10                                          # This increases the progress of the progressbar.
            progressbar.step(progress)
            if (mistakeCount == 1):                                 # This checks if the user got a mistake or not. Which changes the amount of points they will get.
                answer_text = "Correct, good job! You almost got the hang of this."
                # answer text changes based on the outcome the user got.
                score += 5
                mistakeCount = 0
                if (progress == 100):
                    displayResults()
                else:
                    randomInt(difficulty)

            else:
                answer_text = "Correct, Perfect! Keep it up."
                score += 10
                if (progress == 100):
                    displayResults()
                else:
                    randomInt(difficulty)
        else:                                                       # This is when the user answer is not equal to the correct answer.
            mistakeCount += 1
            totalMistakes += 1
            if (mistakeCount == 2):
                answer_text = "Incorrect, let us move on to the next question"
                progress += 10
                mistakeCount = 0
                if (progress == 100):
                    displayResults()
                else:
                    randomInt(difficulty)

            else:
                answer_text = "You have one more try before you move on to the next question."
                displayProblem(value1, value2, answer, arithOperation, difficulty)
    except ValueError:
        answer_text = "Please insert a number."
        displayProblem(value1, value2, answer, arithOperation, difficulty)

def displayResults():
    """ This function is used to display the final result of the user
    out of 100 based on how well they did in the quiz. """

    global score, progress, totalMistakes
    clearRoot()
    ttk.Label(root, text="Your total score is...", font=("Lato", 25, 'bold')).place(relx=0.5, rely=0.25, anchor=CENTER)
    ttk.Label(root, text=(str(score)), font=("Lato", 15)).place(relx=0.5, rely=0.4, anchor=CENTER)
    ttk.Label(root, text="Your grade is...", font=("Lato", 15)).place(relx=0.5, rely=0.54, anchor=CENTER)
    if (score >= 50 and score <= 59):                           # This if condition checks which grade the user got depending on their total score. 
        ttk.Label(root, 
                  text=("E"), 
                  font=("Lato", 15)
                  ).place(relx=0.5, rely=0.64, anchor=CENTER)

    elif (score >= 60 and score <= 69):
        ttk.Label(root, 
                  text=("D"), 
                  font=("Lato", 15)
                  ).place(relx=0.5, rely=0.64, anchor=CENTER)
    
    elif (score >= 70 and score <= 79):
        ttk.Label(root, 
                  text=("C"), 
                  font=("Lato", 15)
                  ).place(relx=0.5, rely=0.64, anchor=CENTER)

    elif (score >= 80 and score <= 89):
        ttk.Label(root, 
                  text=("B"), 
                  font=("Lato", 15)
                  ).place(relx=0.5, rely=0.64, anchor=CENTER)
    
    elif (score >= 90):
        ttk.Label(root, 
                  text=("A"), 
                  font=("Lato", 15)
                  ).place(relx=0.5, rely=0.64, anchor=CENTER)
    
    ttk.Button(root, 
               text="Want to play again?", 
               command=lambda: displayMenu()
               ).place(relx=0.4, rely=0.80, anchor=CENTER)

    ttk.Button(root, 
               text="Quit game", 
               command=root.destroy
               ).place(relx=0.6, rely=0.80, anchor=CENTER)

# This is the start of the program.
root = Tk()
root.title('Arithmetic Quiz') 
root.geometry("500x400")
displayMenu()
root.mainloop()