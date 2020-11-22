import random
import copy
import time

import constants


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

    if max_player == constants.PLAYER_1:
        return get_value(board,constants.PLAYER_1) -  get_value(board,constants.PLAYER_2)
    else:
        return get_value(board,constants.PLAYER_2) -  get_value(board,constants.PLAYER_1)
    
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




max_player = constants.PLAYER_1
min_player = constants.PLAYER_2
counter = 0
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
            value = heuristic(board, constants.PLAYER_1)
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


def alphabeta(board, depth, player, alpha, beta):
    value = None
    move = None
    a = alpha
    b = beta

    possible_moves = get_all_possibilities(board, player)


    if len(possible_moves) > 0:


        if depth > 0:


            if player == max_player:



                value = float('-inf')
                # move = None

                for p in possible_moves:

                    new_value, new_move = alphabeta(p, depth-1, min_player, a, b)


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

                    new_value, new_move = alphabeta(p, depth-1, max_player, a, b)


                    if new_value < value:

                        value = new_value
                        move = copy.deepcopy(p)


                    if new_value <=a:

                        break


                    if new_value < b:

                        b = new_value
                    #print("player",player,"value", value,"depth", depth,"player", player)
                    #print(move.printArray())
        else:

            #board.printArray()
            value = heuristic(board, constants.PLAYER_1)
            move = copy.deepcopy(board)



    else:
        #end of the game
        if player == max_player:
            value = float('-inf')
            move = copy.deepcopy(board)

        else:
            value = float('inf')
            move = copy.deepcopy(board)


    return value, move

def get_move_coords(move):
    
    if move == 'w':
        px = 0
        py = 1
    elif move == 'a':
        px = -1
        py = 0
    elif move == 's':
        px = 0
        py = -1
    else:
        px = 1
        py = 0
    return px, py



def user_turn(board, player):

    #read user move
    print('aaaaa')
    legal_moves = set('wasd')
    while True:
        move = input('Move with WASD: ')[0]
        if set(move.lower()) <= legal_moves:
            break
        else:
            print('Incorrect move, try again.')
    
    #get position, and dx, dy
    x, y = get_move_coords(move.lower())
    px, py = board.get_index(player)

    #move user
    if board.is_move_legal(px + x, py + y):

        board.set_position(px, py, constants.AVAILABLE)
        board.set_position(px + x, py + y, player)

    #erase a cell on the board
    while True:
        print('input x, y coords to erase from the board')
        vx, vy = map( int, input().split() )
        
        
        if not board.is_move_legal(vx, vy):
            print('incorrect coords')
        else:
            break

    board.set_position(vx, vy, constants.VOID)


    return board

def game(init_board, first_player):

    #computer begins
    if first_player == 'c':
        max_player = constants.PLAYER_1
        min_player = constants.PLAYER_2

    #user begins
    else: 
        max_player = constants.PLAYER_2
        min_player = constants.PLAYER_1


    turn = 0
    players = [constants.PLAYER_1, constants.PLAYER_2]
    board = copy.deepcopy(init_board)


    #check if beginning player is able to move
    playerMoves = get_value(board, constants.PLAYER_1)

    #make a first move
    if first_player == 'u' and playerMoves > 0:
        print('Player: ', constants.PLAYER_1)
        user_turn(board, constants.PLAYER_1)
        turn += 1

    #get moves for next player
    playerMoves = get_value(board, players[turn % 2])

    #proper gameloop
    while playerMoves > 0:

        print("Player: ", players[turn % 2])

        t1 = time.perf_counter()
        #value, move = alphabeta(board,2, players[turn%2], float('-inf'), float('inf'))
        value, move = minmax(board,2, players[turn%2])
        t2 = time.perf_counter()
        print("value: ",value)
        print("time:", t2-t1)
        board = move
        playerMoves = get_value(board, players[turn % 2])
        board.printArray()
        if playerMoves == 0:
            # endgame(winner)
            print('ai loses')
            break
        
        #user turn
        turn += 1
        print('Player: ', players[turn % 2])
        move = user_turn(board, players[turn % 2])
        board = move
        playerMoves = get_value(board, players[turn % 2])
        if playerMoves == 0:
            # endgame(user)
            print('user loses')
            break


