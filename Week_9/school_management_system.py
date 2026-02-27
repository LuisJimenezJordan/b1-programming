class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello! My name is {self.name}, and I'm {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"Hi, my name is {self.name}. My student ID is {self.student_id} and I'm {self.age} years old.")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        print(f"Hi, my name is {self.name}. I teach {self.subject} and I'm {self.age} years old.")


# Create instances
student1 = Student("Alice", 16, "S001")
teacher1 = Teacher("Mr Smith", 35, "Mathematics")

# Test the system
print("=== School Management System ===\n")
student1.introduce()
teacher1.introduce()