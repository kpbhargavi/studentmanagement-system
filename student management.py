# Student Management System using OOPs and Functions
class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
    def display(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
class StudentManagement:
    def __init__(self):
        self.students = []
    def add_student(self, student_id, name, age, grade):
        new_student = Student(student_id, name, age, grade)
        self.students.append(new_student)
        print("Student added successfully!")
    def view_students(self):
        if not self.students:
            print("No students found.")
            return
        for student in self.students:
            print(student.display())
    def update_student(self, student_id, name, age, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.name = name
                student.age = age
                student.grade = grade
                print("Student details updated successfully!")
                return
        print("Student not found.")
    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student deleted successfully!")
                return
        print("Student not found.")
sms = StudentManagement()
sms.add_student(1, "John Doe", 20, "A")
sms.add_student(2, "Jane Smith", 22, "B")
sms.view_students()
sms.update_student(1, "John Doe", 21, "A+")
sms.view_students()
sms.delete_student(2)
sms.view_students()
