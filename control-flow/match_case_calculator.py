#deifninig the variables
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
#defining mathematical operations
#defining the match case block
match operation:
    case "+" :
        result = num1 + num2
        print(f"the result is {result}")
    case "-" :
        result = num1 - num2
        print(f"the result is {result}")
    case "*" :
        result = num1 * num2
        print(f"the result is {result}")
    case "/" :
        result = num1 / num2
        if num2 != 0:
            print(f"the result is {result}")
        else:
            print("cannot divide by zero")
    case _ :
        print("that is an invalid operation")