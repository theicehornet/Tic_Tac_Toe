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
            p1 = game.player_turn(1)
            clean_console()
            if p1[0] == "X" or p1[0] == "I":
                if p1[0] == "I":
                    print(p1)
                    break
                score.increase_point(1)
                print(f"The winner is the player 1")
                break
            print(p1)
            p2 = game.player_turn(2)
            clean_console()
            if p2[0] == "O":
                score.increase_point(2)
                break
            print(p2)

        score_text = score.scores()
        print(score_text[0])
        print(score_text[1])
        finish = input("Do you want to play again? Y(Yes) or N(No)\n")
        finish = finish.upper()

        if finish == "N":
            break
        elif finish == "Y":
            clean_console()
            game.tablero.clean_board()
        else:
            print("Option no accepted, finishing the game")
            break
    else:
        print("this is where you play against a bot(on development)")
        break

print("Game finished")
time.sleep(2)
