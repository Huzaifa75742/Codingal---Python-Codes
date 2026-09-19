try:
    num1, num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1 / num2
    print("The result of division is:", result)

except ZeroDivisionError as ex:
    print("Error: Division by zero is not allowed.")

except ValueError as ex:
    print("Invalid input. Please enter valid numbers.")
    print("Error details:", ex)

finally:
    print("Execution completed.")