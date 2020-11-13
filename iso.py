import random
import copy

BOARDWIDTH = 7
BOARDHEIGHT = 7

PLAYER_1 = 1
PLAYER_2 = 2
VOID = 0
AVAILABLE = 7


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

    def is_move_legal(self, px, py):
        if px < 0 or px >= BOARDWIDTH:
            return False
        if py < 0 or py >= BOARDHEIGHT:
            return False
        if board.get_position(px, py) == AVAILABLE:
            return True

        return False
    
    


# def forecast_move(board, px, py):
#     new_board = copy.deepcopy(board)
#     index = new_board.get_index(PLAYER_1)  
#     y = index * BOARDHEIGHT
    # new_board.set_position(index, y, AVAILABLE)
    # new_board.set_position(px, py, PLAYER_1)

def get_all_possibilities(board, player):
    # board.indexof()
    px,py = board.get_index(player)
   
    print(px, py)
   
    moves = []
    
    for x in range(-1,2):
        print("x: ",x)
        for y in range(-1,2):
            print("y: ",y)
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

def min_value(board, player):
    v = float('inf')
    for move in get_all_possibilities(board, player):
        

    return v

def max_value(board, player):
    v = float('-inf')
    for move in get_all_possibilities(board, player):


    return v; 



board = Board(7,7)
board.set_position(0, 0, PLAYER_1)
board.set_position(6, 6, PLAYER_2)
board.printArray()
forecast_move(board, 2, 2)


def gameLoop():

    #setup board
    while 1:
        

"""


      []
     / \
   []   []    []   []    []   []    []   []    []   []    []   []    []   []    []   []    []   [] 8
/ \ / \ / \ / \
[4] [2] [6] [8]


                        []
              
              []  []  []  []   []  []



7 - 12 - 22


value = p1moves-p2moves

def alpha_beta_search(board):

# ocenia wartosc kroku dla nowej tablicy
def minimax(board, depth, isMax):
        

#zwraca najlepszy krok gracza
def bestmove(board):





"""



    



#print(wow)


