def add(P,Q):
    return P + Q

def subtract(P,Q):
    return P - Q

def multiply(P,Q):
    return P * Q

def divide(P,Q):
    return P / Q

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice(1/2/3/4): ")

if choice == '1':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", add(num1, num2))
elif choice == '2':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", subtract(num1, num2))
elif choice == '3':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", multiply(num1, num2))
elif choice == '4':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", divide(num1, num2))
else:
    print("Invalid input")