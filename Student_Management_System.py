students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    students[roll] = {
        "Name": name,
        "Age": age,
        "Course": course
    }

    print("Student Added Successfully!\n")

def view_students():
    if not students:
        print("No Student Records Found.\n")
        return

    for roll, details in students.items():
        print(f"\nRoll No : {roll}")
        print(f"Name    : {details['Name']}")
        print(f"Age     : {details['Age']}")
        print(f"Course  : {details['Course']}")

def search_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print(students[roll])
    else:
        print("Student Not Found.")

def delete_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        del students[roll]
        print("Student Deleted Successfully.")
    else:
        print("Student Not Found.")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")