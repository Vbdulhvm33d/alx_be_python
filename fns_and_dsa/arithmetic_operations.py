#defining arithmetic functions
def perform_operation(num1, num2, operation):
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    operation = input("Enter the operation (add, subtract, multiply, divide)").strip().lower()
    #individual operation definition
    if operation == add:
        add = num1 + num2
        print(f"result: {add}")
    elif operation == subtract:
        subtract = num1 - num2
        print(f"result: {subtract}")
    elif operation == multiply:
        multiply = num1 * num2
        print(f"result: {multiply}")
    elif operation == divide:
        divide = num1 / num2
        if num2 == 0:
            print("error: cannot divide by zero")
        else:
            print(f"result: {divide}")

   