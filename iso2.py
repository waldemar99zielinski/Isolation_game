import random
import copy

BOARDWIDTH = 4
BOARDHEIGHT = 4

PLAYER_1 = 1
PLAYER_2 = 2
VOID = 4
AVAILABLE = 0
DEPTH = 1

max_player = 1


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = [AVAILABLE for x in range(BOARDWIDTH*BOARDHEIGHT)] 

    def get_position(self, x, y):
        return self.array[y*BOARDWIDTH+x]

    def printArray(self):
        for j in range(0, BOARDHEIGHT):
            for i in range (0, BOARDWIDTH):
               print(self.array[j*BOARDWIDTH+i], end=" ")
            print('') 

    def set_position(self, x, y, value):
        self.array[y*( BOARDWIDTH )+x] = value

    def get_index(self, value):
        index = self.array.index(value)
        return index%BOARDWIDTH, int(index/BOARDHEIGHT)

    def is_move_legal(self, px, py):
       
        if px < 0 or px >= BOARDWIDTH:
            return False
        if py < 0 or py >= BOARDHEIGHT:
            return False
        if board.get_position(px, py) == AVAILABLE:
            return True

        return False

    def updateBoard(self, new_board):
        # print('new board:')
        # new_board.printArray()
        self.array = new_board.array
        # print(self.array)


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
                # print("value++: ",player,px+x, py+y)
                value +=1
    return value

def get_all_moves(board, player):

    px,py = board.get_index(player)
   
    moves = []
    
    for x in range(-1,2):

        for y in range(-1,2):

            if x == 0 and y == 0:
                continue

            if board.is_move_legal(px + x, py + y):

                new_move = copy.deepcopy(board)
                new_move.set_position(px, py, AVAILABLE)
                new_move.set_position(px+x, py+y, player)
                moves.append(new_move)


    return moves

def get_all_removals(board):
    removals = []

    for y in range(0, board.height):

        for x in range(0, board.width):

            if board.get_position(x,y) == AVAILABLE:

                new_removal = copy.deepcopy(board)
                new_removal.set_position(x,y,VOID)
                removals.append(new_removal)
    
    return removals

def get_all_possibilities(board, player):

    possibilities = []

    player_moves = get_all_moves(board,player)


    for move in player_moves:
        possibilities+=get_all_removals(move)

    return possibilities



def gameLoop(board):

    turn = 0
    players = [PLAYER_1, PLAYER_2]
    move_possible = True

    while move_possible:
        print('current player ', players[ turn % 2])
        move_possible = players_move( board, players[turn % 2] )
        turn += 1
        max_player = (turn % 2) + 1
        # board.printArray()

def heuristic_new(board, player):

    if player == max_player:
        return get_value(board,PLAYER_1) -  get_value(board,PLAYER_2)
    else:
        return get_value(board,PLAYER_2) -  get_value(board,PLAYER_1)

def players_move(board, player):
    temp_board = copy.deepcopy(board)
    value, best_move = minimax(temp_board, player, DEPTH)

    if value == 'inf' or value == '-inf':
        return False
    
    # print('Reached end eval: ', value)
    # best_move.printArray()
    # board = copy.deepcopy(best_move)
    # board.updateBoard(best_move)
    board.updateBoard(best_move)
    # board = best_move
    board.printArray()
    # board.move(player, best_move.coords, best_move.void)
    # return True
    return True

def minimax(board, player, depth):


    possible_moves = get_all_possibilities(board, player)
    value = None
    move = None

    #moves available
    if len(possible_moves) > 0:

        #max depth for a move not reached yet
        if depth > 0:

            #if current player reqs maxing
            if player == max_player:
                
                #worst case - no moves possible
                value = float('-inf')

                #iterate through all moves
                for p in possible_moves:
                    
                    #recursively call minimax alg. to find best values
                    new_value, new_move = minimax(p, player, depth - 1)

                    #xd
                    if new_value > value:
                        value = new_value
                        move = new_move

                        # print('found better move: ', player, value)
                        # move.printArray()
            
            
            #current player reqs minimizing
            else:

                value = float('inf')

                for p in possible_moves:

                    new_value, new_move = minimax(p, player, depth - 1)

                    #xd
                    if new_value < value:
                        value = new_value
                        move = new_move

                        # print('found better move: ', player, value)
                        # move.printArray()
        
        #reached depth == 0
        else:
            #count values for players based on final dest.
            # print('reached depth.', board.printArray())
            value = heuristic_new(board, player)
            # print('value: ', value)
            move = copy.deepcopy(board)
            # move = board

        return value, move

board = Board(BOARDWIDTH,BOARDWIDTH)
board.set_position(0, 0, PLAYER_1)
board.set_position(3, 3, PLAYER_2)
gameLoop(board)