class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_finished_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_val_hw(self):
        sum_ = 0
        quantity = 0
        for course in self.grades:
            quantity += len(self.grades[course])
            val = self.grades[course]
            for namb in val:
                sum_ += namb
        return sum_ / quantity

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average_val_hw()} \n" \
               f"Курсы в процессе изучения: {self.courses_in_progress[0]},{self.courses_in_progress[1]} \nЗавершенные курсы: {self.finished_courses[0]}"

    def __lt__(self, other):
        if isinstance(other, Student):
            if self.average_val_hw() > other.average_val_hw():
                return f"{self.name} {self.surname} учится лучше чем {other.name} {other.surname}"
            elif self.average_val_hw() < other.average_val_hw():
                return f"{self.name} {self.surname} учится хуже чем {other.name} {other.surname}"
            elif self.average_val_hw() == other.average_val_hw():
                return f"{self.name} {self.surname} и {other.name} {other.surname} в среднем учатся одинаково"
        else:
            return 'Не студент'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def average_val_hw(self):
        sum_ = 0
        quantity = 0
        for course in self.grades:
            quantity += len(self.grades[course])
            val = self.grades[course]
            for namb in val:
                sum_ += namb
        result = sum_ / quantity
        return result

    def average_val_lectures(self):
        sum_ = 0
        quantity = 0
        for course in self.grades:
            quantity += len(self.grades[course])
            val = self.grades[course]
            for namb in val:
                sum_ += namb
        return sum_ / quantity

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_val_lectures()}"

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            if self.average_val_lectures() > other.average_val_lectures():
                return f"{self.name} {self.surname} преподает лучше чем {other.name} {other.surname} по мнению студентов"
            elif self.average_val_lectures() < other.average_val_lectures():
                return f"{self.name} {self.surname} преподает хуже чем {other.name} {other.surname} по мнению студентов"
            elif self.average_val_lectures() == other.average_val_lectures():
                return f"{self.name} {self.surname} и {other.name} {other.surname} в среднем преподают одинаково по мнению студентов"
        else:
            return 'Не лектор'



class Reviewer(Mentor):
    def __inin__ (self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        super().rate_hw(student,course,grade)

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"


def GPA_hw(students, course):
    sum_GPA = 0
    for student in students:
        if course in student.courses_in_progress:
            sum_GPA += student.average_val_hw()
    return sum_GPA / len(students)

def GPA_lectures(lecturers, course):
    sum_GPA = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            sum_GPA += lecturer.average_val_lectures()
    return sum_GPA / len(lecturers)






student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Vadim', 'Burov', 'your_gender')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Введение в программирование']

students_list =[student_1, student_2]

# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']

some_reviewer = Reviewer('Dmitry', 'Novikov')
some_reviewer.courses_attached += ['Python']

lecturer_1 = Lecturer('Alexander', 'Sokolov')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Timofey', 'Fadeev')
lecturer_2.courses_attached += ['Python']

lecturers_list = [lecturer_1, lecturer_2]

# cool_mentor.rate_hw(student_1, 'Python', 10)
# cool_mentor.rate_hw(student_1, 'Python', 10)
# cool_mentor.rate_hw(student_1, 'Python', 10)

some_reviewer.rate_hw(student_1, 'Python', 9)
some_reviewer.rate_hw(student_1, 'Python', 8)
some_reviewer.rate_hw(student_1, 'Python', 8)
some_reviewer.rate_hw(student_1, 'Python', 10)

some_reviewer.rate_hw(student_2, 'Python', 7)
some_reviewer.rate_hw(student_2, 'Python', 9)
some_reviewer.rate_hw(student_2, 'Python', 8)
some_reviewer.rate_hw(student_2, 'Python', 8)

student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Python', 7)
student_2.rate_lecture(lecturer_1, 'Python', 10)
student_2.rate_lecture(lecturer_1, 'Python', 8)

student_1.rate_lecture(lecturer_2, 'Python', 10)
student_1.rate_lecture(lecturer_2, 'Python', 9)
student_2.rate_lecture(lecturer_2, 'Python', 10)
student_2.rate_lecture(lecturer_2, 'Python', 9)




#print(best_student.grades)
print(some_reviewer)
print()
print(lecturer_1)
print()
print(student_1)
print()
print(student_1.__lt__(student_2))
print()
print(lecturer_1.__lt__(lecturer_2))
print()
print(GPA_hw(students_list, 'Python'))
print()
print(GPA_lectures(lecturers_list, 'Python'))



