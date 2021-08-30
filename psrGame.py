import random

# Playable options
options = {1: "Paper", 2: "Scissor", 3: "Rock"}
# Winning combinations for the player
combinations = {"Scissor": "Paper", "Rock": "Scissor", "Paper": "Rock"}


def game():
    playerWon = False   # Initially, player has not yet won

    while not playerWon:
        # Computer is random
        computer = random.choice(list(options.values()))

        player = input("Paper, Scissor, Rock ?  ")
        # Verify player's choice
        if player == options.get(1) or player == options.get(2) or player == options.get(3):
            valid = "Valid"
        else:
            valid = options.get(player, "Invalid option")

        while valid == "Invalid option":
            print("Invalid option. Chose again...")
            player = input("Paper, Scissor, Rock ?  ")
            # Verify player's choice
            if player == options.get(1) or player == options.get(2) or player == options.get(3):
                valid = "Valid"
            else:
                valid = options.get(player, "Invalid option")

        if player == computer:  # Same choice => draw
            print("Draw!!!")
            print("Computer chosen " + computer)
        else:
            for key in combinations:    # Check winning combinations
                if combinations[key] == computer and key == player:
                    playerWon = True
                    print("You won!!!")
                    print("Computer chosen " + computer)
            if not playerWon:   # Player has not a winning combination
                print("You lost!")
                print("Computer chosen " + computer)

        play = input("\nDo you want to play more? (Y/N)...  ")
        if play == "n" or play == "N":
            print ("See you!!")
            break
        elif play == "y" or play == "Y":
            playerWon = False   # Force to continue in the while loop
        else:   # Anything else
            while play != "y" and play != "Y" and play != "n" and play != "N":
                play = input("\nDo you want to play more? (Y/N)...  ")
                if play == "n" or play == "N":
                    print("See you!!")
                    break
                elif play == "y" or play == "Y":
                    playerWon = False  # Force to continue in the while loop
            if play == "n" or play == "N":
                break
