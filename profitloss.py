actual_cost = float(input("Enter the actual cost of the item: "))
selling_price = float(input("Enter the selling price of the item: "))

if (selling_price > actual_cost):
    profit = selling_price - actual_cost
    print(f"Total Profit: {profit}".format(profit))
else:
    print("No profit is made.")