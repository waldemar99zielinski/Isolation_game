import random
import copy


BOARDWIDTH = 3
BOARDHEIGHT = 3

PLAYER_1 = 1
PLAYER_2 = 2
VOID = 4
AVAILABLE = 0


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = [AVAILABLE for x in range(BOARDWIDTH*BOARDHEIGHT)] 

    def get_position(self, x, y):
        return self.array[y*BOARDWIDTH+x]

    def printArray(self):
        for j in range(0,BOARDHEIGHT):
            for i in range (0, BOARDWIDTH):
               print(self.array[j*BOARDWIDTH+i], end=" ")
            print() 
    def set_position(self, x, y, value):
        self.array[y*( BOARDWIDTH )+x] = value
    def get_index(self, value):
        index = self.array.index(value)
        return index%BOARDWIDTH, int(index/BOARDHEIGHT)
    def set_board(self, board):
        self.array = board;
    def is_move_legal(self, px, py):
       
        if px < 0 or px >= BOARDWIDTH:
            return False
        if py < 0 or py >= BOARDHEIGHT:
            return False
        if self.get_position(px, py) == AVAILABLE:
            return True

        return False

    


# def forecast_move(board, px, py):
#     new_board = copy.deepcopy(board)
#     index = new_board.get_index(PLAYER_1)  
#     y = index * BOARDHEIGHT
    # new_board.set_position(index, y, AVAILABLE)
    # new_board.set_position(px, py, PLAYER_1)
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

def heuristic(board, max_player):
    #print('heuristic')
    #board.printArray()
    #print('player1v: ', get_value(board,PLAYER_1))
    #print('player1v: ', get_value(board,PLAYER_2))
    if max_player == PLAYER_1:
        return get_value(board,PLAYER_1) -  get_value(board,PLAYER_2)
    else:
        return get_value(board,PLAYER_2) -  get_value(board,PLAYER_1)
    
def get_all_moves(board, player):
    # board.indexof()
    px,py = board.get_index(player)
   
    #print(px, py)
   
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
                new_move.set_position(px, py, AVAILABLE)
                new_move.set_position(px+x, py+y, player)
                #print("newmove: \n",new_move.printArray())
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
"""
def min_value(board, player):
    v = float('inf')
    moves(board, player):
        

    return v

def max_value(board, player):
    v = float('-inf')
    for move in get_all_possibilities(board, player):


    return v; 
"""


"""
#board.set_board([4, 0, 0, 1, 0, 0, 4, 2, 0])
#board.printArray()
possibilities = get_all_possibilities(board, PLAYER_2)
for b in possibilities:
    b.printArray();
    print()
#removals = get_all_removals(moves[0])


#print(get_value(board, PLAYER_1))
"""

max_player = PLAYER_1
min_player = PLAYER_2
def minmax(board, depth, player):
    value = None
    move = None
    possible_moves = get_all_possibilities(board, player)
    if len(possible_moves) > 0:
        if depth > 0:
            if player == max_player:

                value = float('-inf')
                move = None
                for p in possible_moves:
                    new_value, new_move = minmax(p, depth-1, min_player)
                    if new_value >= value:
                        value = new_value
                        move = copy.deepcopy(p)
                    #print("player",player, "value", value, "depth", depth, "player", player)
                    #print(move.printArray())
            else: #minimalize
                value = float('inf')
                move = None
                for p in possible_moves:
                    new_value, new_move = minmax(p, depth-1, max_player)
                    if new_value <= value:
                        value = new_value
                        move = copy.deepcopy(p)

                    #print("player",player,"value", value,"depth", depth,"player", player)
                    #print(move.printArray())
        else:
            #board.printArray()
            value = heuristic(board, PLAYER_1)
            move = copy.deepcopy(board)

        #print("player",player,"value", value,"depth", depth,"player", player)
        #print(move.printArray())

        return value, move
    else:
        #leafs
        if player == max_player:
            value = float('-inf')
            move = copy.deepcopy(board)
            return value,move
        else:
            value = float('inf')
            move = copy.deepcopy(board)
            return value, move


board = Board(BOARDWIDTH,BOARDWIDTH)

board.set_position(1, 0, PLAYER_1)
board.set_position(2, 2, PLAYER_2)
#board.printArray()
board.set_position(1,1,VOID)
board.set_position(2,1,VOID)

#print(minmax(board, 2, True))
board.printArray()
"""
a, b = minmax(board, 2, PLAYER_1)
print("wynik\n")
print(a)
b.printArray()
board.printArray()
# get_value(board, player):
"""
def game(init_board):

    turn = 0
    players = [PLAYER_1, PLAYER_2]
    max_player = PLAYER_1
    min_player = PLAYER_2
    board = copy.deepcopy(init_board)
    playerMoves = get_value(board, players[turn%2])
    while playerMoves > 0:
        print("Player: ", players[turn%2])
        value, move = minmax(board,2, players[turn%2])
        print("value: ",value)
        board=move
        playerMoves = get_value(board, players[turn % 2])
        board.printArray()
        turn +=1

game(board)


