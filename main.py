from scores import Score
from game import Game
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

game = Game()
score = Score()
bot = Bot()

while True:
    if choose == "F":
        print(game.tablero.fill_board())
        while True:
            p1 = game.valid_turn(1, False)
            clean_console()
            if p1[0] == "X" or p1[0] == "I":
                if p1[0] == "I":
                    print(p1)
                    break
                score.increase_point(1)
                print(f"The winner is the player 1")
                break
            print(p1)
            p2 = game.valid_turn(2, False)
            clean_console()
            if p2 == "O":
                score.increase_point(2)
                break
            print(p2)
    else:
        print(game.tablero.fill_board())
        while True:
            p1 = game.valid_turn(1, True)
            clean_console()
            if p1[0] == "X" or p1[0] == "I":
                if p1[0] == "I":
                    print(p1)
                    break
                score.increase_point(1)
                print(f"The winner is the player 1")
                break
            print(p1)
            bot = game.valid_turn(3, True)
            clean_console()
            if bot == "O":
                score.increase_point(2)
                break
            print(bot)

    score_text = score.scores()
    print(score_text[0])
    print(score_text[1])
    finish = input("Do you want to challenge the bot again? Y(Yes) or N(No)\n")
    finish = finish.upper()
    while finish != "N" and finish != "Y":
        finish = input("Option no accepted, do you want to play again? Y(Yes) or N(No)\n")
        finish = finish.upper()
    if finish == "N":
        break
    elif finish == "Y":
        clean_console()
        game.bot.reset_range()
        game.tablero.clean_board()


print("Game finished")
time.sleep(2)
