class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  
  return sorted_students



students = [
    Student("Albert Einstein", "A101", 9.9),
    Student("Charles Darwin", "A102", 9.1),
    Student("Galileo Galilei", "A103", 8.9),
    Student("Isaac Newton", "A104", 9.8),
]

sorted_students = sort_students(students)


for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,student.roll_number,student.cgpa))