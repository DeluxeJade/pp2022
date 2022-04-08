import math
import numpy as np
import curses
from curses import wrapper
import domains
import out 
studentList = []
coursesList = [
    { "name": "Object Orinated Programming", "credit": 4,"id": 1},
    { "name": "Digital System", "credit": 3,"id": 2},
    { "name": "France", "credit" : 8,"id": 3},
    { "name": "Software Engineering", "credit": 3,"id": 4},
    { "name": "Advanced Python", "credit": 4,"id": 5},
]
def main(stdscr): 
    stdscr.clear()
    stdscr.refresh()
    curses.echo()

    while(True):
        stdscr.addstr("1. Students information  ")
        stdscr.addstr("2. Students' grades ")
        stdscr.addstr("3. List all available students ")
        stdscr.addstr("4. List all available courses ")
        stdscr.addstr("5. Add newC ourse ")
        stdscr.addstr("6. Grade modify ")
        stdscr.addstr("7. Exit ")
        option = domains.Utils.cursesInput(stdscr, "Option: ")

        if int(option) == 1:
         domains.Student.StudentInfo(stdscr, studentList)
        if int(option) == 2:
         domains.Student.Grade(stdscr, studentList)
        if int(option) == 3:
         domains.Class.Studentslist(stdscr, studentList)
        if int(option) == 4:
            domains.Courselist(stdscr, coursesList)
        if int(option) == 5:
            domains.CourseInfomation(stdscr, coursesList)
        if int(option) == 6:
            domains.Gradesmdf(stdscr, studentList)
        if int(option) == 7:
            print("Session ended.")
            break

wrapper(main)