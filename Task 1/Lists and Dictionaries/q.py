def display_menu():
    print("\nMenu:")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

def add_student(students):
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grades = list(map(float, input("Enter student's grades (comma-separated X,X,X ): ").split(',')))
    students[name] = {'age': age, 'grades': grades}
    print(f"Student {name} added successfully!")

def view_students(students):
    if not students:
        print("No students found.")
        return

    print("\nStudent Data:")
    for name, info in students.items():
        print(f"Name: {name}, Age: {info['age']}, Grades: {info['grades']}")

def update_student(students):
    name = input("Enter the name of the student to update: ")
    if name not in students:
        print(f"Student {name} not found.")
        return

    print("What would you like to update?")
    print("1. Age")
    print("2. Grades")
    choice = input("Enter your choice: ")

    if choice == '1':
        new_age = int(input("Enter new age: "))
        students[name]['age'] = new_age
        print(f"Age of {name} updated successfully!")
    elif choice == '2':
        new_grades = list(map(float, input("Enter new grades (comma-separated): ").split(',')))
        students[name]['grades'] = new_grades
        print(f"Grades of {name} updated successfully!")
    else:
        print("Invalid choice.")

def delete_student(students):
    name = input("Enter the name of the student to delete: ")
    if name in students:
        del students[name]
        print(f"Student {name} deleted successfully!")
    else:
        print(f"Student {name} not found.")

def main():
    students = {}

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            update_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
