class Student:
    def __init__(self, name, age, grades):
        """Initialize the Student object with name, age, and grades."""
        self.name = name
        self.age = age
        self.grades = grades

    def display_details(self):
        """Display the details of the student."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def calculate_average_grade(self):
        """Calculate and return the average of the grades."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


if __name__ == "__main__":
    # Create a student object (Example) 
    student = Student(name="Alice", age=21, grades=[88, 92, 79, 85])

    # Display student details
    student.display_details()

    # Calculate and display the average grade
    average_grade = student.calculate_average_grade()
    print(f"Average Grade: {average_grade:.2f}")
