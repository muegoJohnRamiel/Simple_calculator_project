# Simple Calculator
# Function 1
def get_numbers():
    """Asks to enter two numbers and returns them as float values."""
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2

# Function 2
def get_operation():
    """Asks to select a math operation and returns the chosen operator."""
    print("\nAvailable operations:")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")
    operation = input("\nEnter the operation you want to perform: ")
    return operation

# Function 3
def calculate(num1, num2, operation):
    """Performs the calculation and returns the result or error message."""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Cannot divide by zero."
    else:
        return "Error! Invalid operation selected."

# Function 4
def show_result(result):
    """Shows the final result to the user."""
    print("\nResult:", result)

# Main Function
def main():
    """Main function that runs the entire calculator program."""
    print("＊*✩*˚📍Simple Calculator📍˚*✩*˚＊")
    
    # Step 1: Get numbers 
    number1, number2 = get_numbers()
    
    # Step 2: Get operation 
    operation = get_operation()
    
    # Step 3: calculate
    result = calculate(number1, number2, operation)
    
    # Step 4: Show the result
    show_result(result)

if __name__ == "__main__":
    main()
    
