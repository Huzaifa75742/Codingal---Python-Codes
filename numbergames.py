import random
number = str(random.randint(1,9))

print("I will generate a random number between 1 and 9. Try to guess it!")
print("You have 3 attempts to guess the number.")
while True:
    guess = input("Enter your guess: ")
    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Incorrect guess. Try again.")