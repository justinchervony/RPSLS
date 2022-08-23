from player import Player

class GestureResults:
    def __init__(self, player1_gesture, player2_gesture):
        self.player1_gesture = player1_gesture
        self.player2_gesture = player2_gesture
        self.player_holder = Player("")
    
    def GestureResults(self):
        if self.player1_gesture == self.player2_gesture:
            return "Tie"

        elif self.player1_gesture == self.player_holder.gestures[0] :
            if self.player2_gesture == self.player_holder.gestures[2] or self.player2_gesture == self.player_holder.gestures[3]:
                return "Player 1"
            else :
                return "Player 2"

        elif self.player1_gesture == self.player_holder.gestures[1]:
            if self.player2_gesture == self.player_holder.gestures[0] or self.player2_gesture == self.player_holder.gestures[4]:
                return "Player 1"
            else :
                return "Player 2"

        elif self.player1_gesture == self.player_holder.gestures[2]:
            if self.player2_gesture == self.player_holder.gestures[1] or self.player2_gesture == self.player_holder.gestures[3]:
                return "Player 1"
            else :
                return "Player 2"

        elif self.player1_gesture == self.player_holder.gestures[3]:
            if self.player2_gesture == self.player_holder.gestures[1] or self.player2_gesture == self.player_holder.gestures[4]:
                return "Player 1"
            else :
                return "Player 2"

        elif self.player1_gesture == self.player_holder.gestures[4]:
            if self.player2_gesture == self.player_holder.gestures[0] or self.player2_gesture == self.player_holder.gestures[2]:
                return "Player 1"
            else :
                return "Player 2"
    