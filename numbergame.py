import random
import time

number = random.randint(1, 100)

def intro():
    print("Put your name here: ")
    global name
    name = input()
    print("Hello " + name + "! Welcome to the Number Guessing Game!")
    if(number % 2 == 0):
        print("The number is even.")
    else:
        print("The number is odd.")
  
    time.sleep(.5)
    print("Go ahead and guess a number between 1 and 100.")

def guess():
    guessestaken = 0

    while guessestaken < 10:
        time.sleep(.25)
        enter = input("Enter your guess: ")

        try:
            guess = int(enter)

            if guess <= 100 and guess >= 1:
                guessestaken = guessestaken+1
                if guessestaken < 6:
                    if guess < number:
                        print("Your guess is too low.")
                    elif guess > number:
                        print("Your guess is too high.")

                    elif guess != number:
                        time.sleep(.5)
                        print("Try again")

                    elif guess == number:
                        break


            elif guess > 100 or guess < 1:
                print("Please enter a number between 1 and 100.")
                continue

        except ValueError:
            print("Please enter a number between 1 and 100.")
            continue

    if guess == number:
        guessestaken = str(guessestaken)
        print("Good job, " + name + "! You guessed my number in " + guessestaken + " guesses!")

    if guess != number:
        print("Nope. The number I was thinking of was " + str(number))

playagain = "yes"
while playagain == "yes" or playagain == "y":
    intro()
    guess()
    print("Would you like to play again? (yes or no)")
    playagain = input().lower()

        

        
        
