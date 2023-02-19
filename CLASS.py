class Person:
    def __init__(self):
        self.grades = None
        self.courses = None
        self.__id = None

    def student(self):
        self.__id = []
        self.courses = []
        self.grades = {}

    def enroll(self, course):
        self.courses.append(course)

    def enter_grades(self, urok, percentage):
        self.grades.append()
