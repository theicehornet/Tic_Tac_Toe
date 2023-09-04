

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

    def complete_board(self, player):
        while True:
            result = self.is_end_game()
            if result[0]:
                return result[1]
            if player == 1:
                pos = int(input("Player 1 turn(X)\n"))
            else:
                pos = int(input("Player 2 turn(O)\n"))
            try:
                if self.positions[pos] != "":
                    pos = int(input("This place has already been taken, choose another place\n"))
                else:
                    if player == 1:
                        self.positions[pos] = "X"
                    else:
                        self.positions[pos] = "O"
                    return self.fill_board()
            except KeyError:
                pos = int(input("This position does not exist, choose another place\n"))
            except ValueError:
                pos = int(input("This position does not exist, choose another place\n"))

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
        if self.is_all_occupied():
            return [True, "It's a draw"]
        elif self.positions[1] == self.positions[2] and self.positions[1] == self.positions[3]:
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
        return [False, None]
