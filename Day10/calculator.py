def calculator():
    num1 = float(input('Enter the first number: '))
    should_continue = True

    while should_continue:
        operator = input('Enter the operator (+, -, *, /): ')
        num2 = float(input('Enter the next number: '))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print('Error: Division by zero is not allowed.')
                return
        else:
            print('Error: Invalid operator.')
            return

        print(f"Result: {num1} {operator} {num2} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation: ").lower() == 'y':
            num1 = result
        else:
            should_continue = False
            calculator() # Recursively call the function to start over

calculator()
