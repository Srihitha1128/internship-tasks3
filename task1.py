# Simple Calculator - Task 1

def calculator():
    print("=== Simple Calculator ===")
    print("Operations: +  -  *  /")

    try:
        # Take user input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operator (+, -, *, /): ")

        # Perform operation
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            # Handle division by zero
            result = num1 / num2
        else:
            print("Invalid operator!")
            return

        print(f"Result: {num1} {op} {num2} = {result}")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except ValueError:
        print("Error: Please enter valid numbers!")

calculator()
