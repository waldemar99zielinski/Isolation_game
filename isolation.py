import constants
from board import Board
import iso


def main():
    first_player = getBeginner()
    depth = getDepth()
    x, y = getSize()
    # board = Board(constants.BOARDWIDTH,constants.BOARDWIDTH)
    board = Board(x, y)
    board.set_position(0, 0, constants.PLAYER_1)
    board.set_position(x - 1, y - 1, constants.PLAYER_2)
    # board.set_position(constants.BOARDWIDTH - 1, constants.BOARDHEIGHT - 1, constants.PLAYER_2)

    board.printArray()
    iso.game(board, first_player.lower(), depth)




def getBeginner():
    
    while True:
        player = input('Select who begins the game:\n(U) - user\n(C) - computer\n'  )[0]
        if player.lower() == 'c' or player.lower() == 'u':
            return player
        else:
            print('Select correct player')



def getDepth():

    while True:
        depth = int(input( 'Select search depth for alfa-beta algorithm in range <0,10>\n'))

        if depth in range (-1, 11):
            return depth
        else:
            print('Select correct search depth')


def getSize():
    
    print('Insert board dims: ')
    while True:
        x, y = map( int, input().split() )
        
        if (x < 2 or y < 2 or x != y):
            print('Wrong dimensions. Try again.')
        else:
            break
    return x, y

main()