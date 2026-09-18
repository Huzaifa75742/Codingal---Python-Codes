def calculate_due(billamount, cusamount):
    if cusamount < billamount:
        due = billamount - cusamount
        return due

billamount = float(input("Enter the bill amount: "))
cusamount = float(input("Enter the customer amount: "))

due = calculate_due(billamount, cusamount)
print("The due amount is:", due)