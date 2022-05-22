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

    def rate_hw(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in lectur.courses_attached and course in self.courses_in_progress:
            if course in lectur.grades:
                lectur.grades[course] += [grade]
            else:
                lectur.grades[course] = [grade]
        else:
            return 'Error'

    def __avrg_grade(self):
        sum_mar_course = 0
        count_mar_course = 0
        for marks in self.grades.values():
            sum_mar = 0
            count_mar = 0
            for mark in marks:
                sum_mar += mark
                count_mar += 1
            sum_mar_course += sum_mar
            count_mar_course += count_mar
        if count_mar_course > 0:
            avrg_gr = round((sum_mar_course / count_mar_course), 1)
            return avrg_gr
        else:
            return('-')

    def __str__(self):
        res = f'''
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.__avrg_grade()}
'''
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __avrg_grade(self):
        sum_mar_course = 0
        count_mar_course = 0
        for marks in self.grades.values():
            sum_mar = 0
            count_mar = 0
            for mark in marks:
                sum_mar += mark
                count_mar += 1
            sum_mar_course += sum_mar
            count_mar_course += count_mar
        if count_mar_course > 0:
            avrg_gr = round((sum_mar_course / count_mar_course), 1)
            return avrg_gr
        else:
            return('-')

    def __str__(self):
        res = f'''
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.__avrg_grade()}
'''
        return res
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'

    def __str__(self):
        res = f'''
Имя: {self.name}
Фамилия: {self.surname}
'''
        return res


student_1 = Student('Ivan', 'Ivajov', 'm')
lectur_1 = Lecturer('Jacky', 'Chan')
reviever_1 = Reviewer('Brus', 'Li')

student_1.courses_in_progress += ['Java']
student_1.courses_in_progress += ['Python']
lectur_1.courses_attached += ['Java']
lectur_1.courses_attached += ['Python']
reviever_1.courses_attached += ['Java']
reviever_1.courses_attached += ['Python']
reviever_1.rate_hw(student_1, 'Python', 10)
reviever_1.rate_hw(student_1, 'Java', 3)
student_1.rate_hw(lectur_1, 'Java', 10)
student_1.rate_hw(lectur_1, 'Python', 5)

print(student_1)

print(reviever_1)

print(lectur_1)
