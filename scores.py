class Score:
    def __init__(self):
        self.player1 = 0
        self.player2 = 0

    def increase_point(self, player):
        if player == 1:
            self.player1 += 1
        else:
            self.player2 += 1

    def scores(self):
        return [f"The score of the player 1 is: {self.player1}", f"The score of the player 2 is: {self.player2}"]
