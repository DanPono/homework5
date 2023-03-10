# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate(self, lecturer, course, grade):
        if grade < 0 or grade > 10:
            return 'Ошибка: оценка должна быть в пределах 0-10!'
        if isinstance(lecturer, Lecturer) and \
                course in self.courses_in_progress and \
                course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def getAvg(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_count if total_count != 0 else 0

    def __str__(self):
        average_grade = self.getAvg()
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {average_grade:.1f}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        return self.getAvg() < other.getAvg()

    def __eq__(self, other):
        return self.getAvg() == other.getAvg()


class Mentor:
    def __init__(self, name='No name', surname='No surname'):
        self.name = name
        self.surname = surname
        # список закрепленных курсов
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def getAvg(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_count if total_count != 0 else 0

    def __str__(self):
        average_grade = self.getAvg()
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {average_grade:.1f}'

    def __lt__(self, other):
        return self.getAvg() < other.getAvg()

    def __eq__(self, other):
        return self.getAvg() == other.getAvg()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and \
                course in self.courses_attached and \
                course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def example1():
    best_student = Student('Ruoy', 'Eman', 'your_gender')
    best_student.courses_in_progress += ['Python']
    best_student.courses_in_progress += ['C#']
    best_student.finished_courses += ['Введение в программирование']
    cool_mentor = Reviewer('Some', 'Buddy')
    print(cool_mentor)
    cool_mentor.courses_attached += ['Python']
    cool_mentor.rate_hw(best_student, 'Python', 4)
    cool_mentor.rate_hw(best_student, 'Python', 5)
    cool_mentor.rate_hw(best_student, 'Python', 6)
    print(best_student)
    print(best_student.grades)


def example2():
    best_student = Student('Ruoy', 'Eman', 'your_gender')
    best_student.courses_in_progress += ['Python']
    cool_mentor = Lecturer('Some', 'Buddy')
    cool_mentor.courses_attached += ['Python']
    best_student.rate(cool_mentor, 'Python', 1)
    best_student.rate(cool_mentor, 'Python', 2)
    best_student.rate(cool_mentor, 'Python', 3)
    print(cool_mentor)
    print(cool_mentor.grades)


def example3():
    # list of first names to randomly generate student and lecturer names
    first_names = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy']

    # list of last names to randomly generate student and lecturer names
    last_names = ['Smith', 'Johnson', 'Brown', 'Lee', 'Garcia', 'Davis', 'Williams', 'Jones', 'Miller', 'Wilson']

    # create 10 random students with random names and grades
    students = []
    for i in range(10):
        name = random.choice(first_names)
        surname = random.choice(last_names)
        gender = random.choice(['male', 'female'])
        student = Student(name, surname, gender)
        student.courses_in_progress = [f'Course{i + 1}' for i in range(3)]
        student.finished_courses = [f'Course{i + 4}' for i in range(2)]
        student.grades = {f'Course{i + 1}': [random.randint(1, 10) for j in range(5)] for i in range(3)}
        students.append(student)

    # create 10 random lecturers with random names and grades
    lecturers = []
    for i in range(10):
        name = random.choice(first_names)
        surname = random.choice(last_names)
        lecturer = Lecturer(name, surname)
        lecturer.courses_attached = [f'Course{i + 1}' for i in range(3)]
        lecturer.grades = {f'Course{i + 1}': [random.randint(1, 10) for j in range(5)] for i in range(3)}
        lecturers.append(lecturer)

    # sort the students and lecturers based on their average grades
    students_sorted = sorted(students, key=lambda x: sum(sum(grades) for grades in x.grades.values()) / sum(
        len(grades) for grades in x.grades.values()), reverse=True)
    lecturers_sorted = sorted(lecturers, key=lambda x: sum(sum(grades) for grades in x.grades.values()) / sum(
        len(grades) for grades in x.grades.values()), reverse=True)

    # print the sorted students and lecturers
    print('Sorted students by average grade:')
    for student in students_sorted:
        print(student)
        print()

    print('Sorted lecturers by average grade:')
    for lecturer in lecturers_sorted:
        print(lecturer)
        print()


if __name__ == '__main__':
    # example1()
    # example2()
    example3()
