from player import Player
from random import choice

class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        pass

    def ChooseGesture(self):
        self.chosen_gesture = choice(self.gestures)