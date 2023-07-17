import random

while True:
    user_choice = input ("Choose between Rock, Paper, Scissors: ")
    possible_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choices)
    print(f"n\You chose {user_choice}, Computer chose {computer_choice}.\n")

    if user_choice.lower() == computer_choice:
        print(f"Both players selected {user_choice.lower()}. It's a tie!")
    elif user_choice.lower() == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You Dominated!")
        else:
            print("Paper covers rock! You Were Defeated!?")
    elif user_choice.lower() == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You Dominated!")
        else:
            print("Scissors cuts paper! You Were Defeated!?")
    elif user_choice.lower() == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You Dominated!")
        else:
            print("Rock smashes scissors! You Were Defeated!?")
    play_again = input("Play Again? yes/no: ")
    if play_again.lower() != "yes":
        break