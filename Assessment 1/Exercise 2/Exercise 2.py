"""
Exercise 2 - Alexa tell me a Joke

[Your solution must be no more than 100 lines of code]

The randomJokes.txt file in the resources folder contains a dataset of random jokes. 
Each joke is on a new line and consists of a setup and punchline separated by a question mark.
"""

from tkinter import *
import random
import tkinter.font as tkFont

list = [0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72,75,78,81,84,87,90,93,96,99,102,105,108] 
l1 = ''
l2 = ''
randNum = 0
check = False

def clearRoot():
    """ This function is used to erase all of the items within
    the root window. """

    for item in root.winfo_children():                          # The for loop is used to select every item inside the window/root.
        item.destroy()                                          # The ".destory" deletes the item from the window.

def start():
    """ This function is used to introduce the user to the
    machine, everytime they ask if they can get a question.
    lines will appear in empty space in the middle. """

    bigText = tkFont.Font(size=13)
    smallText = tkFont.Font(size=9)

    clearRoot()
    
    global l1, l2
    
    Label(root, text="Hey. Welcome to the joke machine.", font=bigText).place(relx=0.5, rely=0.15, anchor=CENTER)
    Label(root, text="To start, please write 'Alexa, please tell me a joke' in the text box", font=bigText).place(relx=0.5, rely=0.23, anchor=CENTER)
    Label(root, text="Press any key to get the punchline", font=smallText).place(relx=0.5, rely=0.30, anchor=CENTER)
    entry = Entry(root, width = 40)
    entry.place(relx=0.5, rely=0.4, anchor=CENTER)
    Label(root, text=(l1), font=(11)).place(relx=0.5, rely=0.52, anchor=CENTER)
    Label(root, text=(l2), font=(11)).place(relx=0.5, rely=0.65, anchor=CENTER)
    Button(root, text="Submit", command=lambda: jokeTeller(entry)).place(relx=0.5, rely=0.8, anchor=CENTER)
    Button(root, text="Quit", command=root.destroy).place(relx=0.5, rely=0.9, anchor=CENTER)

def jokeTeller(entry):
    """ This function is used to get a random joke from the
    text file given to students. """

    global list, l1, l2, randNum, check
    
    check = False
    userAnswer = entry.get()
    if(userAnswer == "Alexa, please tell me a joke" and check == False):        # The If condition checks if the useranswer is the same as the given prompt.
        randNum = random.choice(list)                                           # random.choice picks a random choice in a list given to it.
        file = open("randomJokes.txt", "r")                                     # open the text file used.
        content = file.readlines()                                              # ".readlines()" reads every line inside the text file.
        l1 = str(content[randNum])                                              # content[randNum] reads a specific line from the text file.
        l2 = ""
        file.close()                                                            # closes the text file used.
        check = True
        start()
    else:
        l1 = ""
        l2 = "Sorry, Alexa didn't recognize your input, please try again."
        start()

def punchline(event=None):
    global randNum, l2, check
    
    if check == True:
        file = open("randomJokes.txt", "r")
        content = file.readlines()
        l2 = str(content[randNum+1])  
        file.close()
        start()
        check = False

root = Tk()
root.title('Joke Machine') 
root.geometry("500x400")
root.bind('<Key>',punchline)                                    # This binds the 'r' key to the root, so when it is pressed it will execute the punchline function.

start()

root.mainloop()