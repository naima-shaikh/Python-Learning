#Master list for the student record
student_records=[]

#Take name, age, class, subject list, marks
# Store each record as a dictionary
# Append to a master list

def add_student():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    student_class = input("Enter student's class: ")
    subjects = input("Enter the subjects : ").split(',')
    marks = float(input("Enter total marks: "))

student = {
"name": name,
"age": age,
"class": student_class,
"subjects": [s.strip() for s in subjects],
 "marks": marks
    }

