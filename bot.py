import random


class Bot:
    def __init__(self):
        self.range = list(range(1, 10))


    def bot_turn(self):
        random_number = random.choice(self.range)
        self.range.remove(random_number)
        return random_number


    def remove_move(self, number):
        self.range.remove(number)


    def reset_range(self):
        self.range = list(range(1, 10))
