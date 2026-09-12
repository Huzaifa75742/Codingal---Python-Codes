def shutdown(name, time):
    print(f"Hello {name}, the system will shutdown in {time} minutes.")

name = input("Enter your name: ")
time = int(input("Enter the time in minutes: "))
shutdown(name, time)