age = int(input("Enter your age: "))
if age <= 4:
    print("You are a baby.")
elif age <= 12:
    print("You are a child.")
elif age <= 19:
    print("You are a teenager.")
elif age <= 59:
    print("You are an adult.")
elif age >= 60:
    print("You are a grandadult.")
else:
    print("Invalid age entered.")