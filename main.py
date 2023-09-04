from scores import Score
from tablero import Tablero
from bot import Bot
from logo import logo
import time
import os


def clean_console():
    os.system('cls')


print(logo)

choose = input("Welcome are you gonna play with a friend or wanna challenge a bot?F(friend) or B(bot)\n")
choose = choose.upper()

while choose != "F" and choose != "B":
    choose = input("It's not a valid option, try again F(friend) or B(bot)\n")
    choose = choose.upper()

tablero = Tablero()
score = Score()
bot = Bot()

while True:
    if choose == "F":
        while True:
            clean_console()
            print(tablero.fill_board())

            move = tablero.complete_board(1)

            if move == "X":
                print("The player 1 won")
                score.increase_point(1)
                break

            if tablero.is_all_occupied():
                print("It's a draw")
                break

            move2 = tablero.complete_board(2)

            if move2 == "O":
                print("The player 2 won")
                score.increase_point(2)
                break

        score.print_scores()
        choose = input("Do you want to play again? Y(Yes) or N(No)\n")
        choose = choose.upper()

        if choose == "N":
            break
        elif choose == "Y":
            print("")
            tablero.clean_board()
            choose = "F"
        else:
            print("Option no accepted, finishing the game")
            break
    else:
        print("this is where you play against a bot(on development)")
        break

print("Game finished")
time.sleep(2)
