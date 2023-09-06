from tablero import Tablero
from bot import Bot

def is_valid_number(number):
    try:
        return 0 < number < 10
    except TypeError:
        return None


def try_parse_int(text):
    try:
        return int(text)
    except ValueError:
        return None


class Game:
    def __init__(self):
        self.tablero = Tablero()
        self.bot = Bot()


    def valid_turn(self, player, is_bot_playing):
        if player == 1:
            player_move = input("Player 1 turn(X):\n")
            is_number = try_parse_int(player_move)
        elif player == 2:
            player_move = input("Player 2 turn(O):\n")
            is_number = try_parse_int(player_move)
        else:
            bot_move = self.bot.bot_turn()
            is_number = try_parse_int(bot_move)
        while is_number is None or is_valid_number(is_number) is False:
            player_move = input("This position doesn't exist, choose another!\n")
            is_number = try_parse_int(player_move)
        if self.tablero.positions[is_number] != "":
            print("this place it's already taken!!")
            if is_bot_playing:
                return self.valid_turn(player, True)
            return self.valid_turn(player, False)
        if is_bot_playing:
            return self.gameplay_w_bot(player, is_number)
        return self.gameplay_w_players(player, is_number)


    def gameplay_w_players(self, player_turn, player_move):
        if player_turn == 1:
            self.tablero.positions[player_move] = "X"
        else:
            self.tablero.positions[player_move] = "O"
        result = self.tablero.is_end_game()
        if result[0]:
            return result[1]
        return self.tablero.fill_board()

    def gameplay_w_bot(self, player_turn, player_move):
        if player_turn == 1:
            self.tablero.positions[player_move] = "X"
            self.bot.remove_move(player_move)
        else:
            self.tablero.positions[player_move] = "O"
        result = self.tablero.is_end_game()
        if result[0]:
            return result[1]
        return self.tablero.fill_board()
