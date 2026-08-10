print   ("Enter marks obtained in 4 objects")
maths = int(input("Enter marks obtained in maths: "))
science = int(input("Enter marks obtained in science: "))  
english = int(input("Enter marks obtained in english: "))
history = int(input("Enter marks obtained in history: "))

sum = maths + science + english + history
print("The sum of the marks is:", sum)

percentage = (sum / 400) * 100
print(end="The percentage of the marks is: ")
print(percentage)