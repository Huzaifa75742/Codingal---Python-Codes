age_input = input("Enter your age: ")

try:
    
    age = int(age_input.strip())
    
  
    if age % 2 == 0:
        print(f"The age {age} is EVEN.")
    else:
        print(f"The age {age} is ODD.")
except ValueError:
    print("Please enter a valid whole number for age.")