string = input("Enter a string: ")
character = input("Enter a character to count: ")
count = 0
i = 0
while i < len(string):
    if string[i] == character:
        count = count + 1
    i = i + 1
    print(f"The character '{character}' occurs {count} times in the string.")
