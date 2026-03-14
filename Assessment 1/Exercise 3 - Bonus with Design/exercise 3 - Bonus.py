from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

students = []
studentNames = ['Select an option']
lowestScore = 100
highestScore = 0

def clearRoot():
    """ This function is used to erase all of the items within
    the root window. """

    for item in root.winfo_children():                          # The for loop is used to select every item inside the window/root.
        item.destroy()                                          # The ".destory" deletes the item from the window.

def getAllInfo():
    """ This function is used to gather the required info
    inside the text file. """

    students.clear()
    
    count = 1
    with open('studentMarks.txt', 'r') as file: 
        lines = file.readlines()[1:]
        for line in lines:
            studentData = {
                "number":0,
                "studentID":"",
                "name":"",
                "totalCourseWork":"",
                "examMark":"",
                "overallPercentage":""
            }
            x = line.split(',')                                 # ".split" splits each word whenever it meets a comma / ",".
            studentData["number"] = count
            studentData["studentID"] = x[0]
            studentData["name"] = x[1]
            studentData["totalCourseWork"] = str(int(x[2]) + int(x[3]) + int(x[4]))
            studentData["examMark"] = x[5]
            studentData["overallPercentage"] = str((int(studentData["totalCourseWork"]) + int(x[5])) / 160)
            count += 1
            students.append(studentData)

def getStudentValues():
    """ This function gets all necessary values for future actions. """

    global highestScore, lowestScore                            # global is used to indicate that the varible can be used outside of the function.
    studentNames.clear()                                        # ".clear" deletes the content of a list.

    # This is used to get every student's name for the dropdown.
    for studentData in students:
        studentNames.append(studentData["name"])
    
    # This is used to get the highest grade.
    for studentData in students:
        if(float(studentData["overallPercentage"]) > float(highestScore)):
            highestScore = studentData["overallPercentage"]

    # This is used to get the lowest grade.
    for studentData in students:
        if (float(studentData["overallPercentage"]) < float(lowestScore)):
            lowestScore = studentData["overallPercentage"]
    
def gradecalculator(markPercentage):
    """ This function is used to get the student's grade by using if conditions. """

    if markPercentage >= 70:
        grade = "A"
        return grade
    elif markPercentage >= 60:
        grade = "B"
        return grade
    elif markPercentage >= 50:
        grade = "C"
        return grade
    elif markPercentage >= 40:
        grade = "D"
        return grade
    else:
        grade = "F"
        return grade

def totalAverageCalculator():
    """ This function finds the lowest scoring student. """
    
    totalScore = 0
    for i in range(len(students)):
        totalScore += float(students[i]["overallPercentage"])*100
    totalAverage = totalScore/len(students)
    return(totalAverage)

def printHighestScorer(Lb1):
    """ This function finds the highest scoring student. """

    global highestScore
    Lb1.delete(0, END)                                          # ".delete" clears out the content of the listbox.
    currentLine = 0
    for i in range(len(students)):
        markPercentage = float(students[i]["overallPercentage"])*100
        if students[i]["overallPercentage"] == highestScore:
            # ".insert" places the line of text inside the listbox according to the first parameter.
            Lb1.insert(currentLine, "Student ID: " + students[i]["studentID"])
            currentLine += 1
            Lb1.insert(currentLine, "Name: " + students[i]["name"])
            currentLine += 1
            Lb1.insert(currentLine, "Total Course Work: " + students[i]["totalCourseWork"])
            currentLine += 1
            Lb1.insert(currentLine, "Exam Mark: " + students[i]["examMark"])
            currentLine += 1
            Lb1.insert(currentLine, "Overall Percentage: " + str(markPercentage) + "%")
            currentLine += 1
            grade = gradecalculator(markPercentage)
            Lb1.insert(currentLine, "Grade: " + grade)

def printLowestScorer(Lb1):
    """ This function finds the lowest scoring student. """

    global lowestScore
    Lb1.delete(0, END)
    currentLine = 0
    for i in range(len(students)):
        markPercentage = float(students[i]["overallPercentage"])*100
        if students[i]["overallPercentage"] == lowestScore:
            Lb1.insert(currentLine, "Student ID: " + students[i]["studentID"])
            currentLine += 1
            Lb1.insert(currentLine, "Name: " + students[i]["name"])
            currentLine += 1
            Lb1.insert(currentLine, "Total Course Work: " + students[i]["totalCourseWork"])
            currentLine += 1
            Lb1.insert(currentLine, "Exam Mark: " + students[i]["examMark"])
            currentLine += 1
            Lb1.insert(currentLine, "Overall Percentage: " + str(markPercentage) + "%")
            currentLine += 1
            grade = gradecalculator(markPercentage)
            Lb1.insert(currentLine, "Grade: " + grade)

def printSpecify(Lb1, value_inside):
    """ This function finds and inserts a specific student's information 
    inside the list box. """

    Lb1.delete(0, END)
    currentLine = 0
    currentQry = value_inside.get()
    for i in range(len(students)):
        markPercentage = float(students[i]["overallPercentage"])*100
        if students[i]["name"] == currentQry:
            Lb1.insert(currentLine, "Student ID: " + students[i]["studentID"])
            currentLine += 1
            Lb1.insert(currentLine, "Name: " + students[i]["name"])
            currentLine += 1
            Lb1.insert(currentLine, "Total Course Work: " + students[i]["totalCourseWork"])
            currentLine += 1
            Lb1.insert(currentLine, "Exam Mark: " + students[i]["examMark"])
            currentLine += 1
            Lb1.insert(currentLine, "Overall Percentage: " + str(markPercentage) + "%")
            currentLine += 1
            grade = gradecalculator(markPercentage)
            Lb1.insert(currentLine, "Grade: " + grade)
            
def printAllInfo(Lb1):
    """ This function inserts all of the students information inside the listbox. """

    Lb1.delete(0, END)
    totalAverage = totalAverageCalculator()
    currentLine = 0

    Lb1.insert(currentLine, "There are a total of " + str(len(students)) + " students inside the class.")
    currentLine += 1
    Lb1.insert(currentLine, "The class' total average is " + str(totalAverage) + "%")
    currentLine += 1
    Lb1.insert(currentLine, "")
    currentLine += 1

    for i in students:
        markPercentage = float(i["overallPercentage"])*100

        Lb1.insert(currentLine, "Student ID: " + i["studentID"])
        currentLine += 1
        Lb1.insert(currentLine, "Name: " + i["name"])
        currentLine += 1
        Lb1.insert(currentLine, "Total Course Work: " + i["totalCourseWork"])
        currentLine += 1
        Lb1.insert(currentLine, "Exam Mark: " + i["examMark"])
        currentLine += 1
        Lb1.insert(currentLine, "Overall Percentage: " + str(markPercentage) + "%")
        currentLine += 1

        grade = gradecalculator(markPercentage)
        Lb1.insert(currentLine, "Grade: " + grade)
        currentLine += 1
        Lb1.insert(currentLine, "")
        currentLine += 1

def printAllInfoReverse(Lb1):
    """ This function inserts all of the students information inside the listbox
    in reverse order. """
    
    students.reverse()
    Lb1.delete(0, END)
    totalAverage = totalAverageCalculator()
    currentLine = 0

    Lb1.insert(currentLine, "There are a total of " + str(len(students)) + " students inside the class.")
    currentLine += 1
    Lb1.insert(currentLine, "The class' total average is " + str(totalAverage) + "%")
    currentLine += 1
    Lb1.insert(currentLine, "")
    currentLine += 1

    for i in students:
        markPercentage = float(i["overallPercentage"])*100
        
        Lb1.insert(currentLine, "Student ID: " + i["studentID"])
        currentLine += 1
        Lb1.insert(currentLine, "Name: " + i["name"])
        currentLine += 1
        Lb1.insert(currentLine, "Total Course Work: " + i["totalCourseWork"])
        currentLine += 1
        Lb1.insert(currentLine, "Exam Mark: " + i["examMark"])
        currentLine += 1
        Lb1.insert(currentLine, "Overall Percentage: " + str(markPercentage) + "%")
        currentLine += 1

        grade = gradecalculator(markPercentage)
        Lb1.insert(currentLine, "Grade: " + grade)
        currentLine += 1
        Lb1.insert(currentLine, "")
        currentLine += 1

def addInfo(newName, newID, mark1, mark2, mark3, newExamMark):
    """ This function is used to add information. """

    ID = newID.get()
    name = newName.get()
    m1 = mark1.get()
    m2 = mark2.get()
    m3 = mark3.get()
    ExamMark = newExamMark.get()
    f = open("studentMarks.txt", "a")
    f.write("\n" + ID + "," + name  + "," + m1 + "," + m2 + "," + m3 + "," + ExamMark)
    f.close()
    menuScreen()

def getSpecify(value1, newName, newID, newMark1, newMark2, newMark3, newExamMark):
    """ This function gets the specific student and inserts them inside the queries
    the user may want to change. """

    getAllInfo()
    getStudentValues()
    currentQry = value1.get()

    for i in range(len(students)):
        if students[i]["name"] == currentQry:
            lineQry = students[i]["number"]
    ptr = 1

    with open("studentMarks.txt", "r") as f:
        lines = f.readlines()[1:]
        for line in lines:
            if ptr == lineQry:
                x = line.split(',')
                Id = x[0]
                name = x[1]
                mark1 = x[2]
                mark2 = x[3]
                mark3 = x[4]
                examMark = x[5]

                newName.delete(0, END)
                newID.delete(0, END)
                newMark1.delete(0, END)
                newMark2.delete(0, END)
                newMark3.delete(0, END)
                newExamMark.delete(0, END)

                newName.insert(0, name)
                newID.insert(0, Id)
                newMark1.insert(0, mark1)
                newMark2.insert(0, mark2)
                newMark3.insert(0, mark3)
                newExamMark.insert(0, examMark)
            ptr += 1

def editInfo(value1, newName, newID, newMark1, newMark2, newMark3, newExamMark):
    """ This function changes the value of a particular information. """

    currentQry = value1.get()
    name = newName.get()
    Id = newID.get()
    m1 = newMark1.get()
    m2 = newMark2.get()
    m3 = newMark3.get()
    examMark = newExamMark.get()
    ptr = 0

    for i in range(len(students)):
        if students[i]["name"] == currentQry:
            lineQry = students[i]["number"]
    with open("studentMarks.txt", "r") as f:
        lines = f.readlines()
    with open("studentMarks.txt", "w") as f:
        for line in lines:
            try:
                if ptr != lineQry:
                    f.write(line)
                else:
                    f.write(Id + "," + name  + "," + m1 + "," + m2 + "," + m3 + "," + examMark)
            except:
                f.write(line)
            ptr += 1
    f.close()
    menuScreen()

def deleteInfo(value_inside):
    """ This function deletes a line inside the text document. """

    currentQry = value_inside.get()
    for i in range(len(students)):
        if students[i]["name"] == currentQry:
            lineQry = students[i]["number"]
    ptr = 0
    with open("studentMarks.txt", "r") as f:
        lines = f.readlines()
    with open("studentMarks.txt", "w") as f:
        for line in lines:
            try:
                if ptr != lineQry:
                    f.write(line)
                ptr += 1
            except:
                f.write(line)
    f.close()
    menuScreen()

def menuScreen():
    """ This function acts as the screen the user will use and prints out all 
    of the necessary information. """

    clearRoot()
    getAllInfo()
    getStudentValues()

    global picture1, bg1
    value_inside = StringVar()

    pic1 = Label(root,image=picture1, bg=bg1).place(relx=0.5, rely=0.1, anchor=CENTER)

    Label(root, 
          text="Student Manager",                               # Text is used to store the text to be seen from the user.
          font=("Georgia", 18),                                 # This parameter changes how the text's font, size, and style.
          bg=bg1,
          ).place(relx=0.5, rely=0.2, anchor=CENTER)
    
    Label(root, 
          text="Student Records:",
          font=("Georgia", 14),
          bg=bg1,
          ).place(relx=0.2, rely=0.28, anchor=CENTER)
    
    entry = ttk.Combobox(root, width = 40, textvariable = value_inside)
    entry['values'] = studentNames
    entry.place(relx=0.31, rely=0.263)

    Button(root, text="View Record", command=lambda:printSpecify(Lb1, value_inside)).place(relx=0.70, rely=0.28, anchor=CENTER)
    Button(root, text="Delete Record", command=lambda:deleteInfo(value_inside)).place(relx=0.82, rely=0.28, anchor=CENTER)
    
    Button(root, text="View All\nStudent Records", width=12, justify=CENTER, command=lambda:printAllInfo(Lb1)).place(relx=0.17, rely=0.39, anchor=CENTER)
    Button(root, text="View Highest\nOverall mark", width=12, justify=CENTER, command=lambda:printHighestScorer(Lb1)).place(relx=0.17, rely=0.49, anchor=CENTER)
    Button(root, text="View Lowest\nOverall mark", width=12, justify=CENTER, command=lambda:printLowestScorer(Lb1)).place(relx=0.17, rely=0.59, anchor=CENTER)
    Button(root, text='Reverse\nOrder', width=12, command=lambda:printAllInfoReverse(Lb1)).place(relx=0.17, rely=0.67, anchor=CENTER)

    Lb1 = Listbox(root, width=80, height=15)
    Lb1.place(relx=0.57, rely=0.52, anchor=CENTER)
    
    Button(root, text='Add Student', command=lambda:addInfoMenu()).place(relx=0.70, rely=0.77, anchor=CENTER)
    Button(root, text='Edit Student', command=lambda:editInfoMenu()).place(relx=0.82, rely=0.77, anchor=CENTER)

def addInfoMenu():
    """ This function is the menu for adding a certain line. """

    clearRoot()

    global bg1

    Label(root, 
          text="Add a Student?",
          font=("New Times Roman", 16, "bold"),
          bg=bg1,
          ).place(relx=0.5, rely=0.1, anchor=CENTER)
    
    Label(root, 
          text="Name:",
          font=("New Times Roman", 14),
          bg=bg1,
          ).place(relx=0.18, rely=0.195)
    
    newName = Entry(root,
                  font=('Century 12'), 
                  width=24)
    newName.place(relx=0.38, rely=0.2)

    Label(root, 
          text="Student ID:",
          font=("New Times Roman", 14),
          bg=bg1,
          ).place(relx=0.18, rely=0.295)
    
    newID = Entry(root,
                  font=('Century 12'), 
                  width=24)
    newID.place(relx=0.38, rely=0.3)
    
    Label(root, 
          text="Marks(20):",
          font=("New Times Roman", 14),
          bg=bg1,
          ).place(relx=0.18, rely=0.395)
    
    mark1 = Entry(root,
                  font=('Century 12'), 
                  width=5)
    mark1.place(relx=0.38, rely=0.4)

    mark2 = Entry(root,
                  font=('Century 12'), 
                  width=5)
    mark2.place(relx=0.48, rely=0.4)

    mark3 = Entry(root,
                  font=('Century 12'), 
                  width=5)
    mark3.place(relx=0.58, rely=0.4)

    Label(root, 
          text="Exam Mark(100):",
          font=("New Times Roman", 14),
          bg=bg1,
          ).place(relx=0.18, rely=0.495)
    
    newExamMark = Entry(root,
                  font=('Century 12'), 
                  width=5)
    newExamMark.place(relx=0.38, rely=0.5)
    
    Button(root, text="Submit", command=lambda:addInfo(newName, newID, mark1, mark2, mark3, newExamMark)).place(relx=0.35, rely=0.7, anchor=CENTER)
    Button(root, text="Back", command=lambda:menuScreen()).place(relx=0.65, rely=0.7, anchor=CENTER)
    
def editInfoMenu():
    """ This function is the menu for editing a certain line. """
    
    clearRoot()
    getAllInfo()
    getStudentValues()
    value1 = StringVar()

    global bg1

    Label(root, 
          text="Edit a Student's Profile",
          font=("New Times Roman", 16, "bold"),
          bg=bg1,
          ).place(relx=0.5, rely=0.1, anchor=CENTER)
    
    Label(root, 
          text="Whose information do you want to edit?",
          font=("New Times Roman", 12),
          bg=bg1,
          ).place(relx=0.5, rely=0.18, anchor=CENTER)

    profile = ttk.Combobox(root, width = 22, textvariable = value1)
    profile['values'] = studentNames
    profile.place(relx=0.5, rely=0.25, anchor=CENTER)

    Button(root, text="Search", command=lambda:getSpecify(value1, newName, newID, newMark1, newMark2, newMark3, newExamMark)).place(relx=0.5, rely=0.35, anchor=CENTER)

    Label(root, 
          text="Name:",
          font=("New Times Roman", 12),
          bg=bg1,
          ).place(relx=0.1, rely=0.42)
    
    newName = Entry(root,
                  font=('Century 12'), 
                  width=18)
    newName.place(relx=0.18, rely=0.42)

    Label(root, 
          text="ID:",
          font=("New Times Roman", 12),
          bg=bg1,
          ).place(relx=0.55, rely=0.42)
    
    newID = Entry(root,
                  font=('Century 12'), 
                  width=10)
    newID.place(relx=0.59, rely=0.42)

    Label(root, 
          text="Marks(20):",
          font=("New Times Roman", 12),
          bg=bg1,
          ).place(relx=0.1, rely=0.52)
    
    newMark1 = Entry(root,
                  font=('Century 12'), 
                  width=4)
    newMark1.place(relx=0.21, rely=0.52)
    
    newMark2 = Entry(root,
                  font=('Century 12'), 
                  width=4)
    newMark2.place(relx=0.30, rely=0.52)

    newMark3 = Entry(root,
                  font=('Century 12'), 
                  width=4)
    newMark3.place(relx=0.39, rely=0.52)

    Label(root, 
          text="Exam Mark(100):",
          font=("New Times Roman", 12),
          bg=bg1,
          ).place(relx=0.55, rely=0.52)
    
    newExamMark = Entry(root,
                  font=('Century 12'), 
                  width=5)
    newExamMark.place(relx=0.71, rely=0.52)

    Button(root, text="Submit", command=lambda:editInfo(value1, newName, newID, newMark1, newMark2, newMark3, newExamMark)).place(relx=0.35, rely=0.7, anchor=CENTER)
    Button(root, text="Back", command=lambda:menuScreen()).place(relx=0.65, rely=0.7, anchor=CENTER)

# This is the start of the code.
root = Tk()

img = Image.open(".\\media\\file icon.png")
resizedPhoto = img.resize((100,100))
picture1 = ImageTk.PhotoImage(resizedPhoto)

bg1 = "#e1f8fa"

# This creates the geometry.
root.geometry("800x600")
root.resizable(0,0)

root.title('Student Manager') 
root.configure(bg=bg1)
root.iconbitmap(".\\media\\file icon.ico")

menuScreen()

root.mainloop()
