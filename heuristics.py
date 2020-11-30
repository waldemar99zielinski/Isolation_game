import constants
from helpers import get_value
def heuristic(board, max_player):

    if max_player == constants.PLAYER_1:
        return get_value(board,constants.PLAYER_1) -  get_value(board,constants.PLAYER_2)
    else:
        return get_value(board,constants.PLAYER_2) -  get_value(board,constants.PLAYER_1)
    