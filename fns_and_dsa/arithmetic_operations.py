def perform_operation():
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    operation=input("Enter the operation (add, subtract, multiply, divide)")
    match operation:
        case 'add':
            print("Result: ", num1 +num2)
        case 'subtract':
            print("Result: ", num1 - num2)
        case 'multiply':
            print("Result: ", num1 * num2)
        case 'divide':
            print("Result: ", num1 / num2)
    
perform_operation(num1,num2, operation)
