def total_calc(bill_amount, tip_percentage):

    total_tip = bill_amount*(1 + 0.01*tip_percentage)
    total = round(total_tip, 2)
    print(f"The total amount to be paid is: ${total}")

total_calc (150, 20)