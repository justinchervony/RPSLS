import time

class RunGame:
    def __init__(self):
        pass
    def GameStart():
        print("Welcome to Rock Paper Scissors Lizard Spock")
        print("")

    def GameRules():
        print("Here are the rules:")
        print("Each match will be a 'best-of-three' series.")
        print("Use the number keys indicated to enter your gesture selection!")
        print("")
        print("Scissors cut Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard")
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")
        print("Rock crushes Scissors")
        print("")

    def GameParticipants():
        print("How many human players are there? Type 1 or 2 (Type 3 for an AI only match). ")
        print("")

    def GameRound():
        print("Type 0 for Rock")
        print("Type 1 for Paper")
        print("Type 2 for Scissors")
        print("Type 3 for Lizard")
        print("Type 4 for Spock")
        print("Enter you gesture choice: ")
        print("")
    
    def GameResults():
        print("Player 1 uses x!")
        print("Player 2 uses y!")
        print("x is before y")
        print("Player 1 wins!")
        print("")
