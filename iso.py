import random
import copy
import time

import constants

f = open('alphabeta_different_depth.txt', 'a')


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
                    if new_value > value:
                        value = new_value
                        move = copy.deepcopy(p)
                    #print("player",player, "value", value, "depth", depth, "player", player)
                    #print(move.printArray())
            else: #minimalize
                value = float('inf')
                move = None
                for p in possible_moves:
                    new_value, new_move = minmax(p, depth-1, max_player)
                    if new_value < value:
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
            value = -10000
            move = copy.deepcopy(board)

        else:
            value = 10000
            move = copy.deepcopy(board)


    return value, move

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



def user_turn(board, player):

    #read user move
    legal_moves = set('wasd')
    while True:

        move = input('Move with WASD: ')[0]
        if set(move.lower()) <= legal_moves:
            
            x, y = get_move_coords(move.lower())
            px, py = board.get_index(player)
            # print('move coords: ', x, y)
            # print('p coords: ', px , py)
            # print('new pos: ', px + x, px + y)

            if board.is_move_legal(px + x, py + y):
                board.set_position(px, py, constants.AVAILABLE)
                board.set_position(px + x, py + y, player)
                break
            else: 
                print('Incorrect move, try again.')
        else:
            print('Incorrect move, try again.')
    
    
    #erase a cell on the board
    while True:
        print('input x, y coords to erase from the board')
        vx, vy = map( int, input().split() )
        
        
        if not board.is_move_legal(vx, vy):
            print('incorrect coords')
        else:
            board.set_position(vx, vy, constants.VOID)
            break

    


    return board



def game(init_board, first_player, depth):

    #computer begins
    if first_player == 'c':
        max_player = constants.PLAYER_1
        min_player = constants.PLAYER_2

    #user begins
    elif first_player == 'u': 
        max_player = constants.PLAYER_2
        min_player = constants.PLAYER_1

    else:
        print('Incorrect player')
        return '0'


    turn = 0
    players = [constants.PLAYER_1, constants.PLAYER_2]
    board = copy.deepcopy(init_board)


    
    if first_player == 'u':
        #check moves before user turn
        playerMoves = get_value(board, players[turn % 2])
        if playerMoves == 0:
            print('user lost')
            return 'u'

        print('Player: ', constants.PLAYER_1)
        user_turn(board, constants.PLAYER_1)
        board.printArray()

        #check moves at the end of the turn
        playerMoves = get_value(board, players[turn % 2])
        if playerMoves == 0:
            print('user lost')
            return 'u'

        turn += 1


    
    #proper gameloop
    while True:


        if get_value(board, players[turn % 2]) == 0:
            print('ai lost')
            return 'c'

        
        print("(AI) Player: ", players[turn % 2])
        t1 = time.perf_counter()

        if constants.ALPHABETA:
            value, move = alphabeta(board, depth, players[turn%2], float('-inf'), float('inf'))
        else:
            value, move = minmax(board, depth, players[turn%2])
        t2 = time.perf_counter()

        print("value: ",value)
        print("time:", t2-t1)

        board = move
        board.printArray()


        if get_value(board, players[turn % 2]) == 0:
            print('ai lost')
            return 'c'

        #user turn
        turn += 1


        if get_value(board, players[turn % 2]) == 0:
            print('user lost')
            return 'u'


        print('Player: ', players[turn % 2])
        
        move = user_turn(board, players[turn % 2])
        board = move
        board.printArray()


        if get_value(board, players[turn % 2]) == 0:
            print('user lost')
            return 'u'

        turn += 1


def end_ai(board, depth, ai, time):

    print('AI ', ai, ' lost.')

    if constants.DEBUG:
        x, y = board.get_size()
        log = str(x) + 'x' + str(y) + ' ' + str(depth) + ' ' + str(time) + '\n'
        f.write(log)

    return 'c'


def gameAI(init_board, first_player, depth):
    
    board = copy.deepcopy(init_board)
    turn = 0

    if first_player == constants.PLAYER_1:
        players = [constants.PLAYER_1, constants.PLAYER_2]
        max_player = constants.PLAYER_1
        min_player = constants.PLAYER_2
    else:
        players = [constants.PLAYER_2, constants.PLAYER_1]
        max_player = constants.PLAYER_2
        min_player = constants.PLAYER_1
    

    t1 = time.perf_counter()

    while True:

        #no moves left for ai before move
        if get_value(board, players[turn % 2]) == 0:
            board.printArray()
            t2 = time.perf_counter()
            return end_ai(board, depth, players[turn % 2], t2 - t1)

        if constants.ALPHABETA:
            value, move = alphabeta(board, depth, players[turn % 2], float('-inf'), float('inf'))
        else:
            value, move = minmax(board, depth, players[turn % 2])

        board = move


        #no moves left for ai after move
        if get_value(board, players[turn % 2]) == 0:
            board.printArray()
            t2 = time.perf_counter()
            return end_ai(board, depth, players[turn % 2], t2 - t1)

        #swap max, min for next ai XDDDDDDD no pls god no
        # max_player, min_player = min_player, max_player

        #next ai's turn
        turn += 1

