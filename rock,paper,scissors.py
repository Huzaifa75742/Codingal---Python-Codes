import random
while True:
    user_choice = input("Enter a choice (rock, paper, scissors):")
    possible_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choices)
    print(f"User choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")