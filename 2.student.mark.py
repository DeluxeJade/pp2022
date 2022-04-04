studentList = []

coursesList = [
    { "name": "Object Orinated Programming",
      "id": 1},
    { "name": "Digital System",
      "id": 2},
    { "name": "France",
      "id": 3},
    { "name": "Software Engineering",
      "id": 4},
    { "name": "Advanced Pytho",
      "id": 5},
]

class Student:
    def __init__(self):
        self.name = input("Name student: ")
        self.id_constant = input("Student' ID: ")
        self.dob = self.StudentDateOfBirth()
        self.courses = self.inputCourse()
    
    def Name(self):
        return self.name
    def Id(self):
        return self.id_constant
    def DateOfBirth(self):
        return self.dob
    def Courses(self):
        return self.courses

    def StudentDateOfBirth(self): 
        dayFlag = True
        while(dayFlag): 
            dayInput = int(input("Student DateOfBirth: "))
            if(isinstance(dayInput, int)):
                if(dayInput<32 and dayInput>0):
                    dayFlag = False
                else:
                    print("Invalid. Please try again.")
            else:
                print("Invalid. Please try again.")
        monthFlag = True
        while(monthFlag):
            monthInput = int(input("Student MonthOfBirth: "))
            if(isinstance(monthInput, int)):
                if(monthInput == 2 and dayInput>29):
                    print("Invalid. Please try again")
                elif(monthInput<13 and monthInput>0):
                    monthFlag = False
                else:
                    print("Invalid. Please try again")
        yearInput = int(input("Student's YearOfBirth: "))

        returnedValue = str(dayInput)+"/"+str(monthInput)+"/"+str(yearInput)
        return returnedValue

    def Grade(self):
        print("Student's grades")
        studentName = input("Name Student: ")
        studentId = input("Student ID: ")
        for i in range(0, len(studentList)):
            if(studentName == studentList[i]["name"] and studentId == studentList[i]["ID_CONSTANT"]):
                chosenCourse = input("Grade of Course?: ")
                print("Course: " + chosenCourse + "Grade: " + str(studentList[i]["courses"][Utils.find(studentList[i]["courses"],"course Name",chosenCourse)]["grade"]))
                return
            else:
                print("Student does not exist")
        
    def inputCourse(self):
        print("Student Course Information")
        tempList = []
        returnedList = []
        index = 0

        numOfCourses = int(input("New Student"+ " Course number: "))

        inputFlag = True
        while(inputFlag):
            if(numOfCourses==0 or int(numOfCourses)>len(coursesList)):
                print("Invalid. Please try again")
            else:
                inputFlag = False
        courses = Course.listCourse(coursesList)
        print("\n")
        while index < int(numOfCourses):
            inputCourse = input("Enter student's course no." + str(index+1) +": ")
            if (inputCourse in tempList):
                print("Course " + inputCourse + " has already been added. Please try again.")
            elif (inputCourse in courses):
                addedCourse = {
                    "grade": "",
                    "courseName": inputCourse,
                }
                tempList.append(inputCourse)
                returnedList.append(addedCourse)
                index = index + 1
                print("Course "+inputCourse + " has been added")
            else:
                print("This course does not exist? Try again.")

        return returnedList

        
class Course:
    def __init__(self) -> None:
        self.courseName = input("Enter course name: ")
        self.courseId = input("Enter course ID: ")

    def listCourse(): 
        print("Listing courses")
        listOfCourse = []
        for i in range(0, len(coursesList)):
            listOfCourse.append(coursesList[i]["name"])

        print("Available courses:")
        for i in range(0, len(coursesList)):
            print(coursesList[i]["name"], end=" ")
        print("\n")
        return listOfCourse



class Class:
    def __init__(self) -> None:
        self.studentList = []
        self.courseList = coursesList

    def inputStudentInfo(self):
        studentsNum = int(input("Enter the number of students: "))
        for i in range(0, studentsNum):
            tempDict = {
                "name": "",
                "ID_CONSTANT": "",
                "dob":"",
                "courses": "",
            }
            tempStudent = Student()

            tempDict["name"] = tempStudent.getName()
            tempDict["ID_CONSTANT"] = tempStudent.getId()
            tempDict["courses"] = tempStudent.getCourses()
            tempDict["dob"] = tempStudent.getDob()
            studentList.append(tempDict)
        
        return tempDict

    def inputCourseInfo(self):
        print("=== Course input information ===")
        coursesNum = int(input("Enter the number of added courses: "))
        for i in range(0, coursesNum):
            tempDict = {
                "name":"",
                "id":"",
            }
            tempCourse = Course()

            tempDict["name"] = tempCourse.courseName
            tempDict["id"] = tempCourse.courseId
            coursesList.append(tempDict)
        


    def listStudents(self): 
        print("=== Listing students ===")
        def listStudentCourse(studentCourseList):
            returnedCourseList = []
            for i in range(0, len(studentCourseList)):
                returnedCourseList.append(studentCourseList[i]["courseName"])
            return returnedCourseList
        
        for i in range(0,len(studentList)):
            print("Student: "+ str(studentList[i]["name"]) + " ID: " + str(studentList[i]["ID_CONSTANT"]) + "- Enrolled in courses: " + str(listStudentCourse(studentList[i]["courses"])))

    def chooseCourse(self):
        print("=== Modify course grade ===")
        flag = True
        checkList = []
        courses = Course.listCourse(coursesList)        
        if(not studentList):
            print("Student list is incomplete.")
        else:
            studentName = input("\nEnter student's name to modify grades: ")
            studentID = input("Enter student's ID to modify grades: ")
            if(Utils.find(studentList,"ID_CONSTANT",studentID)!=-1):            
                currentStudent = studentList[Utils.find(studentList,"ID_CONSTANT",studentID)]
                print("Student: " + currentStudent["name"], "- ID: "+ currentStudent["ID_CONSTANT"] + "is enrolled in: ", end=" ")
                for i in range(0,len(currentStudent["courses"])):
                    print(currentStudent["courses"][i]["courseName"], end=" ")
                    checkList.append(currentStudent["courses"][i]["courseName"])
                courseInput = input("\nEnter student's course to modify grades: ")
                if(courseInput in checkList):
                    studentGrade = input("Enter the modified grade: ")
                    (studentList[Utils.find(studentList,"ID_CONSTANT",studentID)]["courses"][Utils.find(studentList[Utils.find(studentList,"ID_CONSTANT",studentID)]["courses"],"courseName",courseInput)]).update({"grade":studentGrade})                 
                else:
                    print("The course does not exist")
            else:
                print("The student does not exist.")    

class Utils:
    def find(lst, key, value):
        for i, dic in enumerate(lst):
            if dic[key] == value:
                return i
        return -1

def main(): 
    classroom = Class()
    while(True):
        print("#1. Enter students information (Name, ID, Date of birth, Enrolled courses)")
        print("#2. Show students' grades")
        print("#3. List all available students")
        print("#4. List all available courses")
        print("#5. Add a course")
        print("#6. Modify students' grades")
        print("#0. Exit the program")

        option = int(input("Enter the option: "))
        if option ==1:
            classroom.inputStudentInfo()
        elif option ==2:
            Student.showGrade()
        elif option ==3:
            classroom.listStudents()
        elif option ==4:
            Course.listCourse()
        elif option ==5:
            classroom.inputCourseInfo()
        elif option ==6:
            classroom.chooseCourse()
        elif option ==0:
            print("Session ended.")
            break

main()
