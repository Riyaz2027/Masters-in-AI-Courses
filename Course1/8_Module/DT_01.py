class Classroom:
    def __init__(self, name, courses):
        self.name = name          
        self.courses = courses    
        self._secret_code = "CSC101" # Private attribute
    def show_courses(self):
        print(f"The secret code is {self._secret_code}") # Accessing private attribute within the class
        print(f"Classroom {self.name} offers these courses:")
        for course in self.courses:
            print(f"- {course}")

classroom1 = Classroom("Room A", ["Math", "Science", "History"])
classroom2 = Classroom("Room B", ["English", "Art", "Music"])
classroom1.show_courses()
classroom2.show_courses()