import random
from .constants import *

def get_player_marker_choice():
    """ Fetches the choice of market for first player ('x' or 'o')

    Returns player1 choice, player2 choice
    """

    while True:
        player1_input = input("Please pick a symbol 'x' or 'o'")
        if player1_input.lower() in ('x', 'o'):
            player2_input = player1_player2_input_map.get(player1_input)
            print(
                "You are player1 and has chosen %s and player2 will be %s"
                % (player1_input.upper(), player2_input.upper())
            )
            return player1_input.lower(), player2_input


def generate_computer_choice(board):
    """ Auto-generate a slot choice for computer player
    """

    # return random index in board which is unoccupied
    return random.choice(
        [index for index, item in enumerate(board) if not item]
    )



def get_slot_choice(board, computer=False):
    """ Allows user to choose the next slot for his marker

    Accepts: the updated list of markers (available + used)
        : optionally accepts if the player is computer

    Returns the choice of the user

    """
    if computer:
        return generate_computer_choice(board)

    choice = False
    msg = "Please choose a slot between 1 - 9"
    while not choice:
        try:
            choice = int(input(msg))
            if not choice in range(1, 10):
                msg = "Invalid choice, please try again"
            elif not board[position]:
                msg = "Slot not free. Please choose another slot (1 - 9: "
            else:
                break
        except:
            msg = "Invalid choice, please try again"

    return choice


def display_board(board):
    """ For displaying the current state of board

    Accepts the updated list of markers (available + used)

    Returns the the the grid updated with the markers

    """
    blank_board = empty_grid

    for index in range(1, 10):
        if (board[index] in ('o', 'x')):
            blank_board = blank_board.replace(str(index), board[index].upper())
        else:
            blank_board = blank_board.replace(str(index), ' ')
    print(blank_board)



def place_marker(board, mark, position):
    """ Marks the current user mark in a given position in the board

    Accepts board, current user mark and desired location for placement

    Returns the updated board
    """
    board[position] = mark
    return board


def is_game_over(board):
    """ Check if the game is over as draw
    """
    return board.count(False) == 1

def check_if_won(board, mark):
    """ Checks if the user with current mark has won

    Accepts the board and the last mark

    Returns True / False
    """

    for indexes in game_tuple_indexes:
        if [board[index] for index in indexes].count(mark) == 3:
            return True
    return False


def play_agiainst_computer():
    """ Get user choice whether to play against computer
    """
    res = ''
    while res not in ('y', 'n'):
        res = input("Play against computer - 'y' or 'n' ").lower()

    return True if res == 'y' else False




