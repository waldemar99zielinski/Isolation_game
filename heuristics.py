import constants
from helpers import get_value
def heuristic(board):
    #simple heuristics based on number of moves each player has
    return get_value(board, constants.PLAYER_1) - get_value(board, constants.PLAYER_2)
    