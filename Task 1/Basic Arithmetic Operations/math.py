# Program to perform basic arithmetic operations
def main():
    # Taking input from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Performing operations
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2
        division = num1 / num2 if num2 != 0 else "undefined (division by zero)"

        # Displaying results
        print(f"Addition: {num1} + {num2} = {addition}")
        print(f"Subtraction: {num1} - {num2} = {subtraction}")
        print(f"Multiplication: {num1} * {num2} = {multiplication}")
        print(f"Division: {num1} / {num2} = {division}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the program
if __name__ == "__main__":
    main()
