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
        res = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.__avrg_grade()}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}
Оценки за курсы: {self.grades}
'''
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not student!')
            return
        return self.__avrg_grade() < other.__avrg_grade()

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
        res = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.__avrg_grade()}
Оценки за лекции: {self.grades}
'''
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not Lector!')
            return
        return self.__avrg_grade() < other.__avrg_grade()

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
        res = f'''Имя: {self.name}
Фамилия: {self.surname}
'''
        return res

def avrg_mark_all_students (studs, course):
    sum_mark_all = 0
    count_mark_all = 0
    for stud in studs:
        for mark in stud.grades.get(course):
            sum_mark_all += mark
            count_mark_all += 1
    return print(f'Средняя оценка за домашние задания всех студентов по курсу {course}: {round(sum_mark_all / count_mark_all, 2)} \n')

def avrg_mark_all_lectors (lects, course):
    sum_mark_all = 0
    count_mark_all = 0
    for lect in lects:
        for mark in lect.grades.get(course):
            sum_mark_all += mark
            count_mark_all += 1
    return print(f'Средняя оценка за лекции всех лекторов в рамках курса {course}: {round(sum_mark_all / count_mark_all, 2)} \n')

student_1 = Student('Gordon', 'Freemen', 'm')
student_2 = Student('Alex', 'Vance', 'w')
lectur_1 = Lecturer('Artur', 'Clark')
lectur_2 = Lecturer('Ayzek ', 'Asimov')
reviever_1 = Reviewer('Jackie', 'Chan')
reviever_2 = Reviewer('Bruce', 'Lee')

student_1.courses_in_progress += ['Java']
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['VB']
student_2.courses_in_progress += ['C++']
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Go']
lectur_1.courses_attached += ['Java']
lectur_1.courses_attached += ['Python']
lectur_2.courses_attached += ['C++']
lectur_2.courses_attached += ['Python']
reviever_1.courses_attached += ['Java']
reviever_1.courses_attached += ['Python']
reviever_2.courses_attached += ['C++']
reviever_2.courses_attached += ['Python']
reviever_1.rate_hw(student_1, 'Python', 9)
reviever_1.rate_hw(student_1, 'Java', 6)
reviever_2.rate_hw(student_2, 'Python', 9)
reviever_2.rate_hw(student_2, 'Python', 7)
reviever_2.rate_hw(student_2, 'C++', 8)
student_1.rate_hw(lectur_1, 'Java', 7)
student_1.rate_hw(lectur_1, 'Python', 6)
student_1.rate_hw(lectur_1, 'Python', 10)
student_2.rate_hw(lectur_2, 'C++', 9)
student_2.rate_hw(lectur_2, 'Python', 8)

all_stud = [student_1, student_2]
all_lect = [lectur_1, lectur_2]

print(student_1)
print(student_2)
print(f'Средняя оценка {student_1.name} {student_1.surname} выше чем, у {student_2.name} {student_2.surname} - {student_1 > student_2}')
print(f'Средняя оценка {student_1.name} {student_1.surname} ниже чем, у {student_2.name} {student_2.surname} - {student_1 < student_2} \n')
avrg_mark_all_students(all_stud, 'Python')
print(reviever_1)
print(reviever_2)
print(lectur_1)
print(lectur_2)
avrg_mark_all_lectors(all_lect, 'Python')
