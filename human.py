from player import Player

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        pass

    def ChooseGesture(self):
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
                user_input = int(user_input)
                self.chosen_gesture = self.gestures[user_input]
            else:
                print("Please enter a valid gesture number.")
            print("")
