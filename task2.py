def simple_calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero is undefined."
        else:
            return num1 / num2
    else:
        return "Invalid operation."

def calculator():
    while True:
        try:
            # Taking user input
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter an operation (+, -, *, /), or type 'exit' to quit: ")

            # Check if the user wants to exit
            if operation.lower() == 'exit':
                print("Calculator exiting. Goodbye!")
                break

            # Perform the calculation
            result = simple_calculator(num1, num2, operation)
            print(f"Result: {result}\n")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")

# Call the calculator function to start the program
calculator()
