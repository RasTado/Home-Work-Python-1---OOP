class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw_s(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in lectur.courses_attached and course in self.courses_in_progress:
            if course in lectur.grades:
                lectur.grades[course] += [grade]
            else:
                lectur.grades[course] = [grade]
        else:
            return 'Error'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'


student_1 = Student('Ivan', 'Ivanov', 'm')
lectur_1 = Lecturer('Jacky', 'Chan')

student_1.courses_in_progress += ['Java']

lectur_1.courses_attached += ['Java']

student_1.rate_hw_s(lectur_1, 'Java', 10)
student_1.rate_hw_s(lectur_1, 'Python', 10)


print(student_1.name)
print(student_1.surname)
print(student_1.gender)
print(student_1.finished_courses)
print(student_1.courses_in_progress)
print(student_1.grades)
print(lectur_1.name)
print(lectur_1.surname)
print(lectur_1.courses_attached)
print(lectur_1.grades)
