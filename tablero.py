class Tablero:
    def __init__(self):
        self.positions = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}

    def fill_board(self):
        table = ""
        for pos in self.positions:
            if pos % 3 == 0:
                table += f"  {self.positions[pos]}  |\n ----------------\n"
            else:
                table += f"  {self.positions[pos]}  |"
        return table


    def is_position_occupied(self, position):
        return self.positions[position] != ""


    def is_all_occupied(self):
        answer = None
        for value in self.positions.values():
            if value != "":
                answer = True
            else:
                return False
        return answer


    def clean_board(self):
        for pos in self.positions:
            self.positions[pos] = ""


    def is_end_game(self):
        if self.positions[1] == self.positions[2] and self.positions[1] == self.positions[3]:
            return [self.is_position_occupied(1), self.positions[1]]
        elif self.positions[4] == self.positions[5] and self.positions[5] == self.positions[6]:
            return [self.is_position_occupied(4), self.positions[4]]
        elif self.positions[7] == self.positions[8] and self.positions[8] == self.positions[9]:
            return [self.is_position_occupied(9), self.positions[9]]
        elif self.positions[1] == self.positions[4] and self.positions[4] == self.positions[7]:
            return [self.is_position_occupied(4), self.positions[4]]
        elif self.positions[2] == self.positions[5] and self.positions[5] == self.positions[8]:
            return [self.is_position_occupied(2), self.positions[2]]
        elif self.positions[4] == self.positions[5] and self.positions[5] == self.positions[6]:
            return [self.is_position_occupied(4), self.positions[4]]
        elif self.positions[3] == self.positions[6] and self.positions[6] == self.positions[9]:
            return [self.is_position_occupied(9), self.positions[9]]
        elif self.positions[1] == self.positions[5] and self.positions[5] == self.positions[9]:
            return [self.is_position_occupied(1), self.positions[1]]
        elif self.positions[3] == self.positions[5] and self.positions[5] == self.positions[7]:
            return [self.is_position_occupied(5), self.positions[5]]
        elif self.is_all_occupied():
            return [True, "It's a draw"]
        return [False, None]
