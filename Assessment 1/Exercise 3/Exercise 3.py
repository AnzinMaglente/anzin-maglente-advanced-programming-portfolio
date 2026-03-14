from tkinter import *
from tkinter import ttk

students = []
studentNames = ['Select an option']
lowestScore = 100
highestScore = 0

def getAllInfo():
    """ This function is used to gather the required info
    inside the text file. """

    students.clear()
    with open('studentMarks.txt', 'r') as file: 
        lines = file.readlines()[1:]
        for line in lines:
            studentData = {
                "studentID":"",
                "name":"",
                "totalCourseWork":"",
                "examMark":"",
                "overallPercentage":"",
            }
            x = line.split(',')                                 # ".split" splits each word whenever it meets a comma / ",".
            studentData["studentID"] = x[0]
            studentData["name"] = x[1]
            studentData["totalCourseWork"] = str(int(x[2]) + int(x[3]) + int(x[4]))
            studentData["examMark"] = x[5]
            studentData["overallPercentage"] = str((int(studentData["totalCourseWork"]) + int(x[5])) / 160)
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
    """ This calculates the total average of the class. """
    
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

def menuScreen():
    """ This function acts as the screen the user will use and prints out all 
    of the necessary information. """

    getAllInfo()
    getStudentValues()

    value_inside = StringVar() 

    ttk.Label(root, 
          text="Student Manager",                               # Text is used to store the text to be seen from the user.
          font=("New Times Roman", 16, "bold"),                 # This parameter changes how the text's font, size, and style.
          ).place(relx=0.5, rely=0.1, anchor=CENTER)
    ttk.Button(root, text="View All Student Records", command=lambda:printAllInfo(Lb1)).place(relx=0.25, rely=0.25, anchor=CENTER)
    ttk.Button(root, text="View Highest Overall mark", command=lambda:printHighestScorer(Lb1)).place(relx=0.5, rely=0.25, anchor=CENTER)
    ttk.Button(root, text="View Lowest Overall mark", command=lambda:printLowestScorer(Lb1)).place(relx=0.75, rely=0.25, anchor=CENTER)

    ttk.Label(root, 
          text="View Student Record:",
          font=("New Times Roman", 14, "bold"),
          ).place(relx=0.25, rely=0.38, anchor=CENTER)
    
    entry = ttk.Combobox(root, width = 27, textvariable = value_inside)
    entry['values'] = studentNames
    entry.place(relx=0.42, rely=0.355)
    ttk.Button(root, text="View Record", command=lambda:printSpecify(Lb1, value_inside)).place(relx=0.75, rely=0.38, anchor=CENTER)

    Lb1 = Listbox(root, width=80, height=10)
    Lb1.place(relx=0.5, rely=0.7, anchor=CENTER)


# This is the start of the code.
root = Tk()

# This creates the geometry
root.geometry("700x400")

root.title('Student Manager') 
menuScreen()
root.mainloop()
