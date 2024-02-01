class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        return "Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

class Teacher(Person):
    def __init__(self, name, age, gender, subject, experience):
        super().__init__(name, age, gender)
        self.subject = subject
        self.experience = experience

    def display_info(self):
        return f"{super().display_info()}, Subject: {self.subject}, Experience: {self.experience} years"

class Student(Person):
    def __init__(self, name, age, gender, grade, average_mark):
        super().__init__(name, age, gender)
        self.grade = grade
        self.average_mark = average_mark
    def display_info(self):
        return f"{super().display_info()}, Grade: {self.grade}, Average Mark: {self.average_mark}"

# Creating instances and displaying information
teacher_instance = Teacher("Mr. Smith", 35, "Male", "Mathematics", 10)
student_instance = Student("Alice", 15, "Female", 10, 85)

print(teacher_instance.display_info())
print(student_instance.display_info())

