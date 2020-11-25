import constants
from board import Board
import iso


def main():
    first_player = getBeginner()
    depth = getDepth()
    # board = Board(constants.BOARDWIDTH,constants.BOARDWIDTH)
    board = Board(3, 3)
    board.set_position(0, 0, constants.PLAYER_1)
    board.set_position(2, 2, constants.PLAYER_2)
    # board.set_position(constants.BOARDWIDTH - 1, constants.BOARDHEIGHT - 1, constants.PLAYER_2)
    print('xd')
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


main()