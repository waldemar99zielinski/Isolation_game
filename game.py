from helpers import get_move_coords, get_value
from minmax import minmax, alphabeta
import constants
import copy
import time

def end_ai(board, depth, ai, time):

    print('AI ', ai, ' lost.')

    if constants.DEBUG:
        x, y = board.get_size()
        log = str(x) + 'x' + str(y) + ' ' + str(depth) + ' ' + str(time) + '\n'
        f.write(log)

    return 'c'


def end_game(board, player):

    board.printArray()

    #if lost player == ai
    if player is constants.max_player:

        print('AI Won')
        return 'u'
    else:

        print('User won')
        return 'c'



def user_turn(board, player):

    
    legal_moves = set('wasd')

    while True:

        #first letter input
        move = input('Move with WASD: ')[0]

        #if the letter is in our legal set
        if set(move.lower()) <= legal_moves:
            
            #get coords of the player and dx, dy
            x, y = get_move_coords(move.lower())
            px, py = board.get_index(player)

            #check if move is possible
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

        #read cell's coords to be erased
        print('input x, y coords to erase from the board')
        vx, vy = map( int, input().split() )
        
        #try erasing cell
        if board.is_move_legal(vx, vy):
            board.set_position(vx, vy, constants.VOID)
            break
            
        else:
            print('incorrect coords')
    


    return board



def game(init_board, first_player, depth):

    #computer begins
    if first_player == 'c':
        constants.max_player = constants.PLAYER_1
        constants.min_player = constants.PLAYER_2

    #user begins
    elif first_player == 'u': 
        constants.max_player = constants.PLAYER_2
        constants.min_player = constants.PLAYER_1

    else:
        print('Incorrect player')
        return '0'

    print('maxpl: ', constants.max_player)
    #variable setup
    turn = 0
    players = [constants.PLAYER_1, constants.PLAYER_2]
    board = copy.deepcopy(init_board)


    #game loop
    while True:


        #check if current player lost before this round
        if get_value(board, players[turn % 2]) == 0:
            return end_game(board, players[turn % 2])


        #its not ai's turn
        if players[turn % 2] is not constants.max_player:

            #make a move 
            move = user_turn(board, players[turn % 2])


        #it's ai's turn
        else:

            #timer
            t1 = time.perf_counter()

            #if alpha-beta pruning is enabled
            if constants.ALPHABETA:
                value, move = alphabeta(board, depth, players[turn%2], float('-inf'), float('inf'))
            else:
                value, move = minmax(board, depth, players[turn%2])

            #timer
            t2 = time.perf_counter()
                

        #copy players move
        board = move
        board.printArray()

        #check if current player lost after this round
        if get_value(board, players[turn % 2]) == 0:
            return end_game(board, players[turn % 2])

        #next turn
        turn += 1





def ai_game(init_board, first_player, depth):
    


    if first_player == constants.PLAYER_1:
        players = [constants.PLAYER_1, constants.PLAYER_2]
        max_player = constants.PLAYER_1
        min_player = constants.PLAYER_2
    else:
        players = [constants.PLAYER_2, constants.PLAYER_1]
        max_player = constants.PLAYER_2
        min_player = constants.PLAYER_1
    
    #variable setup
    board = copy.deepcopy(init_board)
    turn = 0

    t1 = time.perf_counter()

    #game loop
    while True:

        #no moves left for ai before move
        if get_value(board, players[turn % 2]) == 0:
            t2 = time.perf_counter()
            return end_ai(board, depth, players[turn % 2], t2 - t1)

        #if alphabeta pruning is enabled
        if constants.ALPHABETA:
            value, move = alphabeta(board, depth, players[turn % 2], float('-inf'), float('inf'))
        else:
            value, move = minmax(board, depth, players[turn % 2])

        
        #copy move to board
        board = move


        #no moves left for ai after move
        if get_value(board, players[turn % 2]) == 0:
            t2 = time.perf_counter()
            return end_ai(board, depth, players[turn % 2], t2 - t1)


        #next ai's turn
        turn += 1

