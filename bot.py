import random


class Bot:
    def __init__(self):
        self.range = list(range(1, 10))


    def easy(self, player_number):
        self.range.remove(player_number)
        random_number = random.choice(self.range)
        self.range.remove(random_number)
        return random_number


    def medium(self):
        pass


    def hard(self):
        pass
