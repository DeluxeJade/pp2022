tudentList = [
]

coursesList = [
    {
        "name": "Object Orinated Programming",
        "id": 0
    },
    {
        "name": "Digital System",
        "id": 1
    },
    {
        "name": "France",
        "id": 2
    },
    {
        "name": "Software Engineering",
        "id": 3
    },
    {
        "name": "Advanced Python",
        "id": 4
    },
]

def find(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1


def chooseCourse(courseList, studentList):
    print("Here course grade")
    flag = True
    studentCourseList = []
    courses = listCourse(courseList)
    courseInput = input("Course name: ")
    while flag:
        if(courseInput in courses):
            for i in range(0, len(studentList)):
                for t in range (0, len((studentList[i]["courses"]))):
                    if(studentList[i]["courses"][t]["courseName"] == courseInput):
                        studentCourseList.append(studentList[i])
            flag = False
        else:
            print("Your course does not exist.")
    
    if(not studentList):
        print("Student list is incomplete.")
    else:
        studentName = input("Enter student's name : ")
        studentID = input("Enter student's ID : ")
        for i in range(0, len(studentCourseList)):
            if((studentName == studentCourseList[i]["name"]) and (studentID == studentCourseList[i]["ID_CONSTANT"])):
                studentGrade = input("Enter student "+ studentName + ", ID: "+ studentID + " new grade: ")
                (studentList[find(studentList,"ID_CONSTANT",studentID)]["courses"][find(studentList[find(studentList,"ID_CONSTANT",studentID)]["courses"],"courseName",courseInput)]).update({"grade":studentGrade})                 


def inputCourseInfo(studentNo, courseList):
    print("Course information")
    tempList = []
    returnedList = []
    index = 0

    numOfCourses = input("Enter student's no. " +str(studentNo) + " number of enrolled courses: ")
    courses = listCourse(courseList)
    while index < int(numOfCourses):
        inputCourse = input("Enter course name no. " + str(index) +" for student no. " + str(studentNo) + ": ")
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
            print("The entered course does not exist. Please try again.")

    return returnedList


def inputStudentInfo(studentList):
    studentsNum = int(input("Enter the number of students: "))

    for i in range(0, studentsNum):
        tempDict = {
            "name": "",
            "ID_CONSTANT": "",
            "courses": "",
        }
        print(" Student infomation")
        tempName = input("Enter the name for student no." + str(i) + ": ")
        tempId = input("Enter the ID for student no." + str(i) + ": ")
        courseList = inputCourseInfo(i, coursesList)

        tempDict["name"] = tempName
        tempDict["ID_CONSTANT"] = tempId
        tempDict["courses"] = courseList
        studentList.append(tempDict)
    return studentList

def listCourse(courseList): 
    print(" Listing courses")
    listOfCourse = []
    for i in range(0, len(courseList)):
        listOfCourse.append(courseList[i]["name"])

    print("Here are the available courses: \n")
    for i in range(0, len(courseList)):
        print(courseList[i]["name"], end=" ")
    print("\n")

    return listOfCourse



def listStudents(studentData): 
    print("Listing students ")
    def listStudentCourse(studentCourseList):
        returnedCourseList = []
        for i in range(0, len(studentCourseList)):
            returnedCourseList.append(studentCourseList[i]["courseName"])
        return returnedCourseList
     
    for i in range(0,len(studentData)):
        print("Student "+ studentData[i]["name"] + " ID: " + studentData[i]["ID_CONSTANT"] + ". Enrolled in courses: " + str(listStudentCourse(studentData[i]["courses"])))

def showGrade(studentData):
    print("Student's grades")
    studentName = input("Enter name of the student: ")
    studentId = input("Enter ID of the student: ")
    for i in range(0, len(studentData)):
        if(studentName == studentData[i]["name"] and studentId == studentData[i]["ID_CONSTANT"]):
            chosenCourse = input("Choose which course you want to see the grade of: ")
            print("Course: " + chosenCourse + " - Grade: " + str(studentData[i]["courses"][find(studentData[i]["courses"],"courseName",chosenCourse)]["grade"]))
            return
    print("The student does not exist")
            

def initiateClass():
    inputStudentInfo(studentList)
    chooseCourse(coursesList,studentList)
    listStudents(studentList)
    showGrade(studentList)

initiateClass()