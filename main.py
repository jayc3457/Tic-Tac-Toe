from game import Game
from display_engine import DisplayEngine


def get_input():
    player_move = input("Where would you like to make your move?: ")
    return player_move


game = Game(get_input)
de = DisplayEngine(game)

while game.winner is None:
    de.render()
    if game.turn is game.PLAYER:
        game.player_turn()
    else:
        game.computer_turn()
    game.check_for_win()

de.render()
if game.winner == game.PLAYER:
    print("Hurray, you won!")
elif game.winner == game.COMPUTER:
    print("Sorry but you lost...")
else:
    print("The game was a tie, better luck next time.")
