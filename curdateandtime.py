from datetime import date, time, datetime

today = date.today()
now = datetime.now()
print("Current date:", today)
print("Current time:", now.strftime("%H:%M:%S"))

print("Current date and time:", now)