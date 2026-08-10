amount = int(input("Enter the amount: "))

notes_1 = amount // 100
notes_2 = (amount % 100) // 50
notes_3 = (amount % 100 % 50) // 10

print("Number of 100 notes:", notes_1)
print("Number of 50 notes:", notes_2)
print("Number of 10 notes:", notes_3)