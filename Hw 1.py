class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married
    def introduce_myself(self):
        print(f"Меня зовут {self.full_name}, мне {self.age} лет. Женат/Замужем: {self.is_married}")
class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks
    def calculate_average_mark(self):
        if not self.marks:
            return
        return sum(self.marks.values()) / len(self.marks)
class Teacher(Person):
    base_salary = 1000 #
    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience
    def calculate_salary(self):
        bonus = 0
        if self.experience > 3:
            bonus = (self.experience - 3) * 0.05 * self.base_salary
        return self.base_salary + bonus
def create_students():
    students = []
    students.append(Student("Aleksander Germanovich ", 16, False, {"Математика": 5, "Физика": 4, "Химия": 5}))
    students.append(Student("Alfia Vitalevna", 17, False, {"Математика": 4, "Литература": 5, "История": 4}))
    students.append(Student("Anastofia Kox", 15, False, {"Математика": 3, "Биология": 5, "География": 4}))
    return students
teacher = Teacher("Azamat Kenzebekov", 45, True, 10)
teacher.introduce_myself()
print(f"Опыт работы: {teacher.experience} лет")
salary = teacher.calculate_salary()
print(f"Зарплата: {salary}")
students = create_students()
for student in students:
    student.introduce_myself()
    print("Оценки:", student.marks) 
    average_mark = student.calculate_average_mark()
    print(f"Средний балл: {average_mark:.2f}")
    print("-" * 20)
