from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display_details(self):
        pass
    
class TypeCheckMixin:
    @staticmethod
    def check_instance( obj,cls):
        if not isinstance(obj, cls):
            raise TypeError(f"Object must be an instance of {cls.__name__}")

    
class Student(Person):
    def __init__(self, student_id, name):
        super().__init__(name)
        self._student_id = student_id
        self._grades = {}
        
    @property
    def student_id(self):
        return self._student_id

    @property
    def grades(self):
        return self._grades
    
    def add_grade(self, subject, grade):
        if not isinstance(grade, (int, float)):
            raise TypeError("Grade must be a number")
        if 0 <= grade <= 100:
            self._grades[subject] = grade
        else:
            raise ValueError("Grade must be between 0 and 100")
    
    def average_grade(self):
        if not self._grades:
            return 0.0
        return sum(self._grades.values()) / len(self._grades)

    def display_details(self):
        avg_grade = self.average_grade()
        print(f"Student ID: {self.student_id}, Name: {self.name}, Average Grade: {avg_grade}")
        
class StudentManagementSystem:
    def __init__(self):
        self.students = {}
    @staticmethod
    def check_instance(obj, cls):
        if not isinstance(obj, cls):
            raise TypeError(f"Object must be an instance of {cls.__name__}")

        
    def add_student(self, student):
        TypeCheckMixin.check_instance(student, Student)
        if student.student_id in self.students:
            raise ValueError("A student with this ID already exists")
        self.students[student.student_id] = student
        
    def show_student_details(self, student_id):
        TypeCheckMixin.check_instance(student_id, int)
        student = self.students.get(student_id)
        if student:
            student.display_details()
        else:
            print(f"No student found with ID {student_id}")
            
    def show_student_average_grade(self, student_id):
        TypeCheckMixin.check_instance(student_id, int)
        student = self.students.get(student_id)
        if student:
            print(f"Average Grade for {student.name} (ID: {student_id}): {student.average_grade():.2f}")
        else:
            print(f"No student found with ID {student_id}")



