from helpers import get_all_possibilities
from heuristics import heuristic
import constants
import copy



def minmax(board, depth, player):
    value = None
    move = None
    possible_moves = get_all_possibilities(board, player)
    if len(possible_moves) > 0:
        if depth > 0:
            if player == constants.max_player:

                value = float('-inf')
                #move = None
                for p in possible_moves:
                    new_value, new_move = minmax(p, depth-1, constants.min_player)
                    if new_value > value:
                        value = new_value
                        move = copy.deepcopy(p)
                    #print("player",player, "value", value, "depth", depth, "player", player)
                    #print(move.printArray())
            else: #minimalize
                value = float('inf')
                #move = None
                for p in possible_moves:
                    new_value, new_move = minmax(p, depth-1, constants.max_player)
                    if new_value < value:
                        value = new_value
                        move = copy.deepcopy(p)

                    #print("player",player,"value", value,"depth", depth,"player", player)
                    #print(move.printArray())
        else:
            #board.printArray()
            value = heuristic(board)
            move = copy.deepcopy(board)

        #print("player",player,"value", value,"depth", depth,"player", player)
        #print(move.printArray())

        return value, move
    else:
        #leafs
        if player == constants.max_player:
            # value = float('-inf')
            value = -10000
            move = copy.deepcopy(board)
            return value,move
        else:
            # value = float('inf')
            value = 10000
            move = copy.deepcopy(board)
            return value, move


def alphabeta(board, depth, player, alpha, beta):
    value = None
    move = None
    a = alpha
    b = beta

    possible_moves = get_all_possibilities(board, player)


    if len(possible_moves) > 0:


        if depth > 0:


            if player == constants.max_player:



                value = float('-inf')
                # move = None

                for p in possible_moves:

                    new_value, new_move = alphabeta(p, depth-1, constants.min_player, a, b)


                    if new_value > value:

                        value = new_value
                        move = copy.deepcopy(p)


                    if new_value >=b:

                        break


                    if new_value>a:

                        a=new_value
                    #print("player",player, "value", value, "depth", depth, "player", player)
                    #print(move.printArray())

            else: #minimalize

                value = float('inf')
                # move = None

                for p in possible_moves:

                    new_value, new_move = alphabeta(p, depth-1, constants.max_player, a, b)


                    if new_value < value:

                        value = new_value
                        move = copy.deepcopy(p)


                    if new_value <=a:

                        break


                    if new_value < b:

                        b = new_value

        else:

            #board.printArray()
            value = heuristic(board)
            move = copy.deepcopy(board)



    else:
        #end of the game
        if player == constants.max_player:
            value = -10000
            move = copy.deepcopy(board)

        else:
            value = 10000
            move = copy.deepcopy(board)


    return value, move
