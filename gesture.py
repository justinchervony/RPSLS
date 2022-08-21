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
        else:
            self.gesture_name = "Spock"