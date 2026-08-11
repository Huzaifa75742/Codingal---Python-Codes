temperature = float(input("Enter the temperature in Celsius: "))
if temperature >= 39:
    print("Its summer.")
if temperature <= 19:
    print("Its winter.")
if temperature >= 20 and temperature <= 30:
    print("Its spring.")
if temperature <= 38 and temperature >= 30:
    print("Its fall.")
else: 
    print("Invalid temperature.")  
