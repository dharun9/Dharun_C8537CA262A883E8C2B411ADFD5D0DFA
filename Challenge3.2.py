class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __repr__(self):
        return f"Student(name='{self.name}', roll_number='{self.roll_number}', cgpa={self.cgpa})"

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Test the function with a list of student objects
students = [
    Student("Alice", "S001", 3.8),
    Student("Bob", "S002", 3.5),
    Student("Charlie", "S003", 4.0),
    Student("David", "S004", 3.9),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(student)
