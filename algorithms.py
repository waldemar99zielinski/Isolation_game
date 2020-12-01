from helpers import get_all_possibilities
from heuristics import heuristic
import constants
import copy



def minmax(board, depth, player):
    value = None
    move = None
    possible_moves = get_all_possibilities(board, player)
    #check whether game has ended, player out of moves
    if len(possible_moves) > 0:
        #check whether given depth is achieved
        if depth > 0:
            #maximizing player
            if player == constants.MAX_PLAYER:
                # assign worst value for max
                value = float('-inf')
                #recursion for possible moves
                for p in possible_moves:
                    new_value, new_move = minmax(p, depth-1, constants.MIN_PLAYER)
                    #assign better outcome
                    if new_value > value:
                        value = new_value
                        move = copy.deepcopy(p)

            else: #minimizing player
                #assign worst value for min
                value = float('inf')
                #  #recursion for possible moves
                for p in possible_moves:
                    new_value, new_move = minmax(p, depth-1, constants.MAX_PLAYER)
                    #assign better outcome
                    if new_value < value:
                        value = new_value
                        move = copy.deepcopy(p)

        else:
            # leaves, assign value based on heuristic
            value = heuristic(board)
            move = copy.deepcopy(board)

    else:
        #end of the game player is out of moves,
        if player == constants.MAX_PLAYER:
            value = -10000
            move = copy.deepcopy(board)

        else:
            value = 10000
            move = copy.deepcopy(board)

    return value, move

def alphabeta(board, depth, player, alpha, beta):
    value = None
    move = None
    #best possible value for max player
    a = alpha
    #best possible value for min player
    b = beta

    possible_moves = get_all_possibilities(board, player)

    # check whether game has ended, player out of moves
    if len(possible_moves) > 0:

        # check whether given depth is achieved
        if depth > 0:
            # maximizing player
            if player == constants.MAX_PLAYER:
                # assign worst value for max
                value = float('-inf')

                # recursion for possible moves
                for p in possible_moves:

                    new_value, new_move = alphabeta(p, depth-1, constants.MIN_PLAYER, a, b)

                    #if better move found assign it
                    if new_value > value:

                        value = new_value
                        move = copy.deepcopy(p)

                    # max player found greater value than beta
                    # min player will not choose it anyway
                    # stop searching - break loop
                    if new_value >=b:

                        break

                    # assign better alfa for next interations
                    if new_value>a:

                        a=new_value

            else: #minimizing player
                #assign worst value for min
                value = float('inf')

                # recursion for possible moves
                for p in possible_moves:

                    new_value, new_move = alphabeta(p, depth-1, constants.MAX_PLAYER, a, b)

                    #if better move found assign it
                    if new_value < value:

                        value = new_value
                        move = copy.deepcopy(p)

                    # min player found smaller value than alfa
                    # max player will not choose it anyway
                    # stop searching - break loop
                    if new_value <=a:

                        break

                    #assign better beta for next interations
                    if new_value < b:

                        b = new_value

        else:

            # leaves, assign value based on heuristic
            value = heuristic(board)
            move = copy.deepcopy(board)



    else:
        #end of the game
        if player == constants.MAX_PLAYER:
            value = -10000
            move = copy.deepcopy(board)

        else:
            value = 10000
            move = copy.deepcopy(board)


    return value, move
