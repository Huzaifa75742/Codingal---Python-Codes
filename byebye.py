valid = False
while not valid:
    try:
        number = int(input("Enter a number: "))
        print("You entered:", number)
        valid = True  

    except ValueError as ex:
        print("Invalid input. Please enter a valid integer.")
        print("Error details:", ex)
