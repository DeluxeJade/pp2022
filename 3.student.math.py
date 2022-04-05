import math
import pandas as pd
import curses
from curses import wrapper
import numpy as np

studentList = []
coursesList = [
    { "name": "Object Orinated Programming", "credit": 4,"id": 1},
    { "name": "Digital System", "credit": 3,"id": 2},
    { "name": "France", "credit" : 8,"id": 3},
    { "name": "Software Engineering", "credit": 3,"id": 4},
    { "name": "Advanced Python", "credit": 4,"id": 5},
]
class Student:
    def initialize(stdscr, self,):
        stdscr.addstr("Name student: ")
        self.name = stdscr.getstr()
        stdscr.addstr("Student's ID: ")
        self.id_constant = stdscr.getstr()
        self.dob = self.StudentDateOfBirth(stdscr)
        self.courses = self.inputCourse(stdscr)
    
    def Name(self):
        return self.name
    def Id(self):
        return self.id_constant
    def DateOfBirth(self):
        return self.dob
    def Courses(self):
        return self.courses

    def StudentDateOfBirth(stdscr, self,): 
        dayFlag = True
        while(dayFlag): 
            stdscr.addstr("Student DateOfBirth: ")
            dayInput = stdscr.getstr().decode()
            if(isinstance(int(dayInput), int)):
                if(int(dayInput)<32 and int(dayInput)>0):
                    dayFlag = False
                else:
                    stdscr.addstr("Invalid. Try again.")
            else:
                stdscr.addstr("Invalid. Try again.")
        monthFlag = True
        while(monthFlag):
            stdscr.addstr("Student MonthOfBirth: ")
            monthInput = stdscr.getstr().decode()
            if(isinstance(int(monthInput), int)):
                if(int(monthInput) == 2 and int(dayInput)>29):
                    print("Invalid. Try again")
                    stdscr.addstr("Invalid. Ttry again")
                elif(int(monthInput)<13 and int(monthInput)>0):
                    monthFlag = False
                else:
                    print("Invalid. Try again")
                    stdscr.addstr("Invalid. Try again")
        stdscr.addstr("Student's YearOfBirth: ")
        yearInput = int(stdscr.getstr().decode())
        returnedValue = str(dayInput)+"/"+str(monthInput)+"/"+str(yearInput)
        return returnedValue

    def Grade(self,stdscr):
        studentName = Utils.cursesInput(stdscr,"Name Student: ")
        studentId = Utils.cursesInput(stdscr, "ID Student: ")
        for i in range(0, len(studentList)):
            if(studentName == studentList[i]["name"] and studentId == studentList[i]["ID"]):
                chosenCourse = input("Grade of Course?: ")
                print("Course: " + chosenCourse + " Grade: " + str(studentList[i]["courses"][Utils.find(studentList[i]["courses"],"courseName",chosenCourse)]["grade"]))
                stdscr.addstr("Course: " + chosenCourse + " Grade: " + str(studentList[i]["courses"][Utils.find(studentList[i]["courses"],"courseName",chosenCourse)]["grade"]))
            else:
                print("Student doesn't exist")
                stdscr.addstr("Student doesn't exist")
        
    def CourseEnroll(self,stdscr):
        tempList = []
        returnedList = []
        index = 0
        numOfCourses = (Utils.cursesInput(stdscr,"Enroll Course for Student"))

        inputFlag = True
        while(inputFlag):
            if(numOfCourses==0 or int(numOfCourses)>len(coursesList)):
                print("Invalid. Try again")
                stdscr.addstr("Invalid. Try again")
            else:
                inputFlag = False
        courses = Course.listCourse(coursesList)
        print("\n")
        while index < int(numOfCourses):
            inputCourse = Utils.cursesInput("Student's course no." + str(index+1) + ": ")
            if (inputCourse in tempList):
                stdscr.addstr("This Course " + inputCourse + "Already added. Try again.")
            elif (inputCourse in courses):
                addedCourse = {
                    "Grade": "",
                    "Name": inputCourse,
                }
                tempList.append(inputCourse)
                returnedList.append(addedCourse)
                index = index + 1
                print("This Course "+inputCourse + " has been added")
                stdscr.addstr("This Course" + inputCourse + " has been added")
            else:
                print("Course doesn't exist")
                stdscr.addstr("Course doesn't exist.")

        return returnedList

        
class Course:
    def initialize(self, stdscr) ->None:
        self.courseName = Utils.cursesInput(stdscr, "Name: ")
        self.courseId = Utils.cursesInput(stdscr, "ID: ")
        self.courseCredits = Utils.cursesInput(stdscr, "Credits: ")
    def Courselist(stdscr): 
        Courselist = []
        for i in range(0, len(coursesList)):
            Courselist.append(coursesList[i]["name"])
        stdscr.addstr("Available courses")
        for i in range(0, len(coursesList)):
            stdscr.addstr(coursesList[i]["name"]+ ", ")
        return Courselist

class Class:
    def initialize(self) -> None:
        self.studentList = []
        self.courseList = coursesList
    def StudentInfo(self, stdscr):
        studentsNum = Utils.cursesInput(stdscr, "Number of student:" )
        for i in range(0, int(studentsNum)):
            tempDict = {
                "Student's name": "", "Student's ID": "","Student DateOfBirth":"","Student's course": "","Student's GPA": 0,}
            tempStudent = Student(stdscr)
            tempDict["name"] = tempStudent.Name()
            tempDict["ID_CONSTANT"] = tempStudent.Id()
            tempDict["courses"] = tempStudent.Courses()
            tempDict["dob"] = tempStudent.DateOfBirth()
            studentList.append(tempDict)   
        return tempDict

    def CourseInfomation(self, stdscr):
        coursesNum = Utils.cursesInput(stdscr, "Enter the number of added courses:")
        for i in range(0, int(coursesNum)):
            tempDict = {
                "name":"",
                "id":"",
                "credits": "",
            }
            tempCourse = Course()

            tempDict["name"] = tempCourse.courseName
            tempDict["id"] = tempCourse.courseId
            tempDict["credits"] = tempCourse.courseCredits
            coursesList.append(tempDict)
        


    def Studentslist(self, stdscr): 
        def listStudentCourse(studentCourseList):
            returnedCourseList = []
            for i in range(0, len(studentCourseList)):
                returnedCourseList.append(studentCourseList[i]["courseName"])
            return returnedCourseList
        
        for i in range(0,len(studentList)):
            stdscr.addstr("Student: "+ str(studentList[i]["name"]) + " ID: " + str(studentList[i]["ID_CONSTANT"]) + "Enrolled in courses: " + str(listStudentCourse(studentList[i]["courses"])))
            print("Student: "+ str(studentList[i]["name"]) + " ID: " + str(studentList[i]["ID_CONSTANT"]) + "Enrolled in courses: " + str(listStudentCourse(studentList[i]["courses"])))

    def Gradesmdf(self, stdscr):
        checkList = []
        courses = Course.listCourse(coursesList)        
        if(not studentList):
            print("Student list is incomplete.")
            stdscr.addstr("Student list is incomplete.")
        else:
            studentName = Utils.cursesInput(stdscr, "Enter student's name to modify gradeS: ")
            studentID = Utils.cursesInput(stdscr, "Enter student's ID to modify grades: ")
            if(Utils.find(studentList,"ID_CONSTANT",studentID)!=-1):            
                currentStudent = studentList[Utils.find(studentList,"ID_CONSTANT",studentID)]
                print("Student: " + currentStudent["name"], "- ID: "+ currentStudent["ID_CONSTANT"] + "is enrolled in: ", end=" ")
                for i in range(0,len(currentStudent["courses"])):
                    print(currentStudent["courses"][i]["courseName"], end=" ")
                    checkList.append(currentStudent["courses"][i]["courseName"])
                courseInput = input("\nEnter student's course to modify grades: ")
                if(courseInput in checkList):
                    studentGrade = self.roundDownGrades(input("Enter the modified grade: "))
                    while((not isinstance(studentGrade,int)) or (not isinstance(studentGrade,float)) or isinstance>20 or isinstance<0):
                        print("Invalid input. Please try again")
                    (studentList[Utils.find(studentList,"ID_CONSTANT",studentID)]["courses"][Utils.find(studentList[Utils.find(studentList,"ID_CONSTANT",studentID)]["courses"],"courseName",courseInput)]).update({"grade":studentGrade})                 
                else:
                    print("The course does not exist")
            else:
                print("The student does not exist.")   

    def AverageGrades(self, stdscr):
        studentName = Utils.cursesInput(stdscr, "Enter student's name to see their average grades: ")
        studentID = Utils.cursesInput(stdscr, "Enter student's ID to see their average grades: ")
        gradeArray = np.array([])
        studentIndex = Utils.find(studentList,"ID_CONSTANT",studentID)
        if(studentIndex!=-1): 
            for i in range(0,len(studentList[studentIndex])):
                if((not isinstance(studentList[studentIndex]["courses"][i]["grade"],float)) or (not isinstance(studentList[studentIndex]["courses"][i]["grade"],int))):
                    gradeArray = np.append(0)
                else:
                    gradeArray = np.append(gradeArray, float(studentList[studentIndex]["courses"][i]["grade"]))
            averageGrade = np.average(gradeArray)
            (studentList[studentIndex]).update({"GPA":averageGrade})
            print(studentName+" - " + "ID: " +studentID + " - GPA: "+averageGrade)
            stdscr.addstr(studentName+" - " + "ID: " +studentID + " - GPA: "+averageGrade)
        else:
            print("The student does not exist")
            stdscr.addstr("The student does not exist")

    def sortStudentList(self):
        sortedStudentList = sorted(studentList.copy(), key= lambda d: d['GPA']) 
        return sortedStudentList
    
class Utils:
    def find(lst, key, value):
        for i, dic in enumerate(lst):
            if dic[key] == value:
                return i
        return -1  
    def cursesInput(stdscr,string):
        curses.echo()
        stdscr.addstr(string)
        input = stdscr.getstr()
        return input.decode()

def main(stdscr): 
    stdscr.clear()
    stdscr.refresh()
    curses.echo()
    classroom = Class()
    while(True):
        print("1.Information (Name, ID, DateOfBirth, Course)") 
        stdscr.addstr("1. Enter students information (Name, ID, DateOfBirth, Course)")
        print("2. Show students' grades") 
        stdscr.addstr("2. Show students' grades")
        print("3. List all available students")
        stdscr.addstr("3. List all available students")
        print("4. List all available courses")
        stdscr.addstr("4. List all available courses")
        print("5. Add a course")
        stdscr.addstr("5. Add a course")
        print("6. Modify students' grades")
        stdscr.addstr("6. Modify students' grades")
        print("7. Exit the program")
        stdscr.addstr("7. Exit the program")
        option = Utils.cursesInput(stdscr, "Option: ")
        if int(option) ==1:
            classroom.StudentInfo(stdscr)
        elif int(option) ==2:
            Student.Grade(stdscr)
        elif int(option) ==3:
            classroom.Studentslist(stdscr)
        elif int(option) ==4:
            Course.Courselist(stdscr)
        elif int(option) ==5:
            classroom.CourseInfomation(stdscr)
        elif int(option) ==6:
            classroom.Gradesmdf(stdscr)
        elif int(option) ==7:
            print("END")
            break
wrapper(main)
