try:
    num1, num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1 / num2
    print("The result of division is:", result)

except ZeroDivisionError as ex:
    print("Error: Division by zero is not allowed.")

except ValueError as ex:
    print("Invalid input. Please enter valid numbers.")
    print("Error details:", ex)

except SyntaxError as ex:
    print("Syntax Error: Please enter the numbers in the correct format.")
    print("Error details:", ex)

else:
    print("No exceptions occurred. The division was successful.")

finally:
    print("Execution completed.")