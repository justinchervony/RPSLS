class Gesture:
    def __init__(self, gesture_selection):
        self.gesture_selection = gesture_selection
        self.gesture_name = ""
    
    def Gesture_Naming(self):
        if self.gesture_selection == 0:
            self.gesture_name = "Rock"
        elif self.gesture_selection == 1:
            self.gesture_name = "Paper"
        elif self.gesture_selection == 2:
            self.gesture_name = "Scissors"
        elif self.gesture_selection == 3:
            self.gesture_name = "Lizard"
        elif self.gesture_selection == 4: #I know I could use else here but logically this isn't a "catch-all" so I'm thinking an elif would be more appopriate.
            self.gesture_name = "Spock"