def perform_operation(num1, num2, operation):
    
    match operation:
        case 'add':
            print("Result: ", num1 +num2)
        case 'subtract':
            print("Result: ", num1 - num2)
        case 'multiply':
            print("Result: ", num1 * num2)
        case 'divide':

            print("Result: ", num1 / num2)
            if num2 == 0:
                print ("Result: ", 0)


