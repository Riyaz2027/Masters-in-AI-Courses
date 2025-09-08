course_info = {
    "CSC101": {
        "Room Number": "3004",
        "Instructor": "Haynes",
        "Meeting Time": "8:00 a.m."
    },
    "CSC102": {
        "Room Number": "4501",
        "Instructor": "Alvarado",
        "Meeting Time": "9:00 a.m."
    },
    "CSC103": {
        "Room Number": "6755",
        "Instructor": "Rich",
        "Meeting Time": "10:00 a.m."
    },
    "NET110": {
        "Room Number": "1244",
        "Instructor": "Burke",
        "Meeting Time": "11:00 a.m."
    },
    "COM241": {
        "Room Number": "1411",
        "Instructor": "Lee",
        "Meeting Time": "1:00 p.m."
    }
}

course_input = input("Enter the course number: ")
if course_input in course_info:
    print(f"Course Number: {course_input}")
    print(f"Room Number: {course_info[course_input]['Room Number']}")
    print(f"Instructor: {course_info[course_input]['Instructor']}")
    print(f"Meeting Time: {course_info[course_input]['Meeting Time']}")
else:
    print("Course not found.")


