from helpers import get_move_coords, get_value
from algorithms import minmax, alphabeta
import constants
import copy
import time

def end_ai(board, depth, ai, time):

    if constants.LOG_END:
        print('AI ', ai, ' lost.')

    if constants.DEBUG:
        x, y = board.get_size()
        log = str(x) + 'x' + str(y) + ' ' + str(depth) + ' ' + str(time) + '\n'
        f.write(log)

    return 'c'


def end_game(board, current_player, user):

    board.printArrayWithCord()


    if current_player is user:
    
        if constants.LOG_END:
            print('User Lost')
        return 'u'

    else:
    
        if constants.LOG_END:
            print('AI Lost')

        return 'c'



def user_turn(board, player):

    
    legal_moves = set('qweadzxc')

    while True:

        #first letter input
        move = input('Move with\nQWE\nA D\nZXC: ')[0]

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
        print('input fields coords to erase from the board')
        print('insert x: ')

        vx = input()

        if vx.isnumeric():
            vx = int(vx)
        else:
            print("wrong input")
            continue
        print('insert y: ')
        vy = input()
        if vy.isnumeric():
            vy = int(vy)
        else:
            print("wrong input")
            continue
        #try erasing cell
        if board.is_move_legal(vx, vy):
            board.set_position(vx, vy, constants.VOID)
            break
            
        else:
            print('incorrect coords')
    


    return board



def game(init_board, first_player, depth):

    #variable setup
    players = [constants.PLAYER_1, constants.PLAYER_2]
    board = copy.deepcopy(init_board)
    turn = 0
    
    if first_player == 'c':
        user = 2
    
    elif first_player == 'u':
        user = 1
    
    else:
        # print('Incorrect player')
        return 1




    #game loop
    while True:


        #check if current player lost this round
        if get_value(board, players[turn % 2]) == 0:
            return end_game(board, players[turn % 2], user)


        #its not ai's turn
        if players[turn % 2] is user:

            #make a move 
            move = user_turn(board, players[turn % 2])


        #it's ai's turn
        else:

            #timer
            t1 = time.perf_counter()
            print("Computer move, please wait...")
            #if alpha-beta pruning is enabled
            if constants.ALPHABETA:
                value, move = alphabeta(board, depth, players[turn%2], float('-inf'), float('inf'))
            else:
                value, move = minmax(board, depth, players[turn%2])

            #timer
            t2 = time.perf_counter()

        #copy players move
        board = move
        board.printArrayWithCord()


        turn += 1





def ai_game(init_board, first_player, depth):
    

    #variable setup
    players = [constants.PLAYER_1, constants.PLAYER_2]
    board = copy.deepcopy(init_board)
    
    if first_player == constants.PLAYER_1:
        turn = 0
    
    elif first_player == constants.PLAYER_2:
        turn = 1
    
    else:
        # print('Wrong first player')
        return 1


    t1 = time.perf_counter()

    #game loop
    while True:

        #no moves left for ai this round
        if get_value(board, players[turn % 2]) == 0:
            t2 = time.perf_counter()
            return end_ai(board, depth, players[turn % 2], t2 - t1)

        move_start = time.perf_counter()

        #if alphabeta pruning is enabled
        if constants.ALPHABETA:
            value, move = alphabeta(board, depth, players[turn % 2], float('-inf'), float('inf'))
        else:
            value, move = minmax(board, depth, players[turn % 2])

        move_end = time.perf_counter()
        #copy move to board
        board = move

        if constants.LOG_MOVE_TIME:
            print('Ai {} took {} to move' .format(players[turn % 2], move_end - move_start))


        #next ai's turn
        turn += 1

