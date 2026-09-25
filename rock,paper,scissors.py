import random
while True:
    user_choice = input("Enter a choice (rock, paper, scissors):")
    possible_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choices)
    print(f"User choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")
    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")