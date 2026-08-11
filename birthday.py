birthdays = {
    "Alice": "1995-04-12",
    "Bob": "2000-08-25",
    "Charlie": "1992-11-03",
    "Diana": "1998-01-19",
    "Evan": "2005-06-30",
}


chosen_name = input("Enter a name to find their birthday: ")



birthday = birthdays.get(chosen_name.title())


if birthday:
    print(f"{chosen_name.title()}'s birthday is {birthday}.")
else:
    print("That name is not in the system.")