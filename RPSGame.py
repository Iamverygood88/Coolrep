from random import randint

player_lives = 3
computer_lives = 3

# available weapons => store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

# make the computer pick one item at random

computer = choices[randint(0, 2)]

# show the computer choice in the terminal_window
print("Computer chooses: ", computer)
print("Computer wins", computer_lives)
print("Player wins", player_lives)

while player is False:

    player = input("Rock, Paper or Scissors?\n")
    print("Player chooses:", player)

    if player == "computer":
        print("Tie! Live to shoot another day")

    elif player == "Rock":
        if computer == "Paper":
            print("You lose", computer, "covers", player)
            player_lives -=1
            print("Evgeniia lives left", player_lives)
        else:
            print("You win!", player, "smashes", computer)
            computer_lives -=1
            print("Computer lives left", computer_lives)

    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
            player_lives -=1
            print("Evgeniia lives left", player_lives)

        else:
            print("You win!", player, "covers", computer)
            computer_lives -=1
            print("Computer lives left", computer_lives)

    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
            player_lives -=1
            print("Evgeniia lives left", player_lives)
        else:
            print("You win!", player, "cuts", computer)
            computer_lives -=1
            print("Computer lives left", computer_lives)

    if player_lives == 0:
        print("Computer won the game.")
        restart = input("Would you like to play again looser? (Yes/No)")
        if restart == "Yes":
            continue
        if restart == "No":
            exit()

    if computer_lives == 0:
        print("EVGENIIA WON!")
        restart = input("Would you like to play again looser? (Yes/No)")
        if restart == "Yes":
            continue
        if restart == "No":
            exit()

    player = False
    computer = choices[randint(0, 2)]
