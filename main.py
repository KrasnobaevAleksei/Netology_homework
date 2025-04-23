class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {} 

    # Функция считает среднюю оценку студента за домашнее задание 
    def average_grade(self):
        summa = 0
        count = 0 
        for i in self.grades:         
            summa += (sum(self.grades[i]))
            count += len(self.grades[i])
        res = summa/count
        return res

    # выставление оценок лекторам
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades and 1 <= grade <= 10 :
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"
        
    # Перегрузка метода __str__ для студента  
    def __str__(self):
        
        return f" Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за лекции: {self.average_grade()} \n Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n Завершенные курсы :{", ".join(self.finished_courses)}"
    # Перегрузка оператора РАВЕНСТВО для студента
    def __eq__(self, other):
        return self.average_grade() == other.average_grade()   
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {} 

class Lecturer(Mentor):
    # Функция считает среднюю оценку лектора за лекции
    def average_grade(self):
        summa = 0
        count = 0 
        for i in self.grades:         
            summa += (sum(self.grades[i]))
            count += len(self.grades[i])
        res = summa/count
        return res
    # Перегрузка метода __str__ для лектора
    def __str__(self):
        return f" Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за лекции: {self.average_grade()}"
    # Перегрузка оператора РАВЕНСТВО для лектора
    def __eq__(self, other):
        return self.average_grade() == other.average_grade()
    
class Reviewer(Mentor):
    # выставление оценок студентам
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f" Имя: {self.name} \n Фамилия: {self.surname}"
    

reviewer_1 = Reviewer("Bill", "Geits")
reviewer_2 = Reviewer("Philip", "Moris")

lecture_1 = Lecturer("Boby", "Tarantino")
lecture_2 = Lecturer("Jacky", "Chan")

student_1 = Student("Stiv", "Djobs", "man")
student_2 = Student("Maria", "Gonsales", "woman")

reviewer_1.courses_attached.append("Python")   
lecture_1.courses_attached.append("Python")
student_1.courses_in_progress.append("Python")
student_1.finished_courses.append("Git")
student_1.finished_courses.append("Word")

student_1.rate_lecturer(lecture_1, "Python", 5)
reviewer_1.rate_hw(student_1,"Python", 5) 
reviewer_1.rate_hw(student_1,"Python", 8) 

# подсчет средней оценки по всем студентам  врамках одного курса
def total_student_avg_for_course(student_list, course_name):
    for i in student_list:
        summa = 0
        number_grades = 0
        if course_name in i.grades:
            summa += sum(i.grades[course_name])
            number_grades += len(i.grades[course_name])
    return summa/number_grades

# подсчет средней оценки по всем лекторам в рамках одного курса

def total_lecturer_avg_for_course(lector_list, course_name):
    for i in lector_list:
        summa = 0
        number_grades = 0
        if course_name in i.grades:
            summa += sum(i.grades[course_name])
            number_grades += len(i.grades[course_name])
    return summa/number_grades


print(lecture_1)
print(student_1)


