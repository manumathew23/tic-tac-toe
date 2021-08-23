from package.constants import *
from package.utilities import *

"""
Players are denoted as 0 (1st player), 1 (second player)
Slot markers are denoted as - 'x' and 'o'
"""


player = 1
game_over = False
board = [False] * 10
players = get_player_marker_choice()

while not game_over:
    position = get_slot_choice(board)

    # Get the marker for the player
    marker = players[swtich_player.get(player)]

    # Place the marker against the current user
    place_marker(board, marker, position)

    # display the board
    display_board(board)

    if check_if_won(board, marker):
        game_over = True
        msg = " You've won" if player == 1 else "You've lost"
        print(msg)
        break

    player = swtich_player.get(player)

    # Check if game over
    if is_game_over(board):
        game_over = True
        print(" It's a draw")