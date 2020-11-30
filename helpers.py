import random
import copy
import time
import constants

# f = open('alphabeta_different_depth.txt', 'a')


def get_value(board, player):
    px,py = board.get_index(player)
    value = 0
    
    for x in range(-1,2):
        #print("x: ",x)
        for y in range(-1,2):
            #print("y: ",y)
            if x == 0 and y == 0:
                continue

            elif board.is_move_legal(px + x, py + y):
                #print("value++: ",player,px+x, py+y)
                value +=1
    return value


def get_all_moves(board, player):

    px,py = board.get_index(player)
   

   
    moves = []
    
    for x in range(-1,2):
        #print("x: ",x)
        for y in range(-1,2):
            #print("y: ",y)
            if x == 0 and y == 0:
                continue
            #moze
           
            
            #print("board:\n ",new_move.printArray())


            if board.is_move_legal(px + x, py + y):
                new_move = copy.deepcopy(board)
                new_move.set_position(px, py, constants.AVAILABLE)
                new_move.set_position(px+x, py+y, player)
                #print("newmove: \n",new_move.printArray())
                moves.append(new_move)


  

    return moves

def get_all_removals(board):
    removals = []
    for y in range(0, board.height):
        for x in range(0, board.width):
            if board.get_position(x,y) == constants.AVAILABLE:
                new_removal = copy.deepcopy(board)
                new_removal.set_position(x,y,constants.VOID)
                removals.append(new_removal)
    
    return removals


def get_all_possibilities(board, player):
    possibilities = []
    player_moves = get_all_moves(board,player)
    for move in player_moves:
        possibilities+=get_all_removals(move)

    return possibilities


def get_move_coords(move):
    
    if move == 'w':
        px = 0
        py = -1
    elif move == 'a':
        px = -1
        py = 0
    elif move == 's':
        px = 0
        py = 1
    else:
        px = 1
        py = 0
    return px, py
