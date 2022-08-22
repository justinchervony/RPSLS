import time
from computer import ComputerPlayer
from gesture import Gesture
from human import HumanPlayer

class RunGame:
    def __init__(self):
        self.player1 = None
        self.player2 = None
        pass

    def GameStart(self):
        print("Welcome to Rock Paper Scissors Lizard Spock")
        print("")
        # time.sleep(1)
        self.GameRules()
        self.GameParticipants()
        self.GameRound()
        self.GameResults()

    def GameRules(self):
        print("Here are the rules:")
        # time.sleep(1)
        print("Each match will be a 'best-of-three' series.")
        # time.sleep(1)
        print("Use the number keys indicated to enter your gesture selection!")
        # time.sleep(1)
        print("")
        print("Scissors cut Paper")
        # time.sleep(1)
        print("Paper covers Rock")
        # time.sleep(1)
        print("Rock crushes Lizard")
        # time.sleep(1)
        print("Lizard poisons Spock")
        # time.sleep(1)
        print("Spock smashes Scissors")
        # time.sleep(1)
        print("Scissors decapitates Lizard")
        # time.sleep(1)
        print("Lizard eats Paper")
        # time.sleep(1)
        print("Paper disproves Spock")
        # time.sleep(1)
        print("Spock vaporizes Rock")
        # time.sleep(1)
        print("Rock crushes Scissors")
        # time.sleep(2)
        print("")
        pass

    def GameParticipants(self):
        valid_response = False
        while valid_response == False:
            user_input = input("How many human players are there? Type 1 or 2 (Type 3 for an AI only match). ")
            if user_input == "1":
                self.player1 = HumanPlayer("Player 1 ")
                self.player2 = ComputerPlayer("Player 2 ")
                valid_response = True
            elif user_input == "2":
                self.player1 = HumanPlayer("Player 1 ")
                self.player2 = HumanPlayer("Player 2 ")
                valid_response = True
            elif user_input == "3":
                self.player1 = ComputerPlayer("Player 1 ")
                self.player2 = ComputerPlayer("Player 2 ")
                valid_response = True
            else:
                print("Please enter 1, 2, or 3.")
        print("")
        pass

    def GameRound(self):
        valid_response = False
        print("Type 0 for Rock")
        # time.sleep(1)
        print("Type 1 for Paper")
        # time.sleep(1)
        print("Type 2 for Scissors")
        # time.sleep(1)
        print("Type 3 for Lizard")
        # time.sleep(1)
        print("Type 4 for Spock")
        # time.sleep(1)
        print("")
        
        while valid_response == False:
            user_input = input("Enter your gesture choice: ")
            if user_input == "0" or user_input == "1" or user_input == "2" or user_input == "3" or user_input == "4":
                valid_response = True
                self.user_gesture_choice = int(user_input)
                
            else:
                print("Please enter a valid gesture number.")
            print("")
        pass
    
    def GameResults(self):
        print("Player 1 uses {self.player_choice}!")
        # time.sleep(1)
        print("Player 2 uses {self.player2_choice}!")
        # time.sleep(1)
        print("x beats y")
        # time.sleep(1)
        print("Player 1 wins!")
        # time.sleep(1)
        print("")
