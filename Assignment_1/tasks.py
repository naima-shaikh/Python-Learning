
#Master list for the student record
students = []

#Take name, age, class, subject list, marks
# Store each record as a dictionary
# Append to a master list

def add_student():
    name = input("Enter a student name: ")
    age = input("Enter the age of student: ")
    student_class = input("Enter a  class: ")
    subjects = input("Enter the subjects : ").split(',')
    marks = float(input("Enter total marks: "))

    
    
    student = {
        "name": name,
        "age": age,
        "class": student_class,
        "subjects": [s.strip() for s in subjects],
         "marks": marks
    }
    students.append(student)
    print(f" {name}  student added successfully!\n")

## now we want to view the student record for which  we can Loop through all records and display. 

def view_students():
    if not students:
        print(" No students found.\n")
        return
    print("\n Student List:")
    for id, s in enumerate(students, 1):
        print(f"{id}. Name: {s['name']}, Age: {s['age']}, Class: {s['class']}")
    print()

def update_student():
    view_students()
    try:
        id = int(input("Enter student number to update: ")) - 1
        if 0 <= id < len(students):
            students[id]['name'] = input("New name: ")
            students[id]['age'] = input("New age: ")
            students[id]['class'] = input("New class: ")
            print(" Student updated successfully.\n")
        else:
            print(" Invalid student number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

def delete_student():
    view_students()
    try:
        idx = int(input("Enter student number to delete: ")) - 1
        if 0 <= idx < len(students):
            deleted = students.pop(idx)
            print(f" {deleted['name']} has been removed.\n")
        else:
            print(" Invalid student number.\n")
    except ValueError:
        print(" Please enter a valid number.\n")

def analyze_grades():
    if not students:
        print('No student to analyze grades')
        return
    
def main():
    while True:
        print("Welcome to The console-based School Portal")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student Info")
        print("4. Delete Student")
        print("5. Exit")
        print("6. Analyze Grades")
        
        choice = input("Select an option (1-6): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("👋 Exiting School Portal. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")


print(main)