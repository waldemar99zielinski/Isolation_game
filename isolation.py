import constants
from board import Board
from game import game


def main():
    beginner = getBeginner()
    depth = getDepth()
    size = getSize()

    board = Board(size, size)

    if beginner == 'u':
        board.set_position(int(size/2), 0, constants.PLAYER_2)
        board.set_position(int(size/2), size - 1, constants.PLAYER_1)
    else:
        board.set_position(int(size/2), 0, constants.PLAYER_1)
        board.set_position(int(size/2), size - 1, constants.PLAYER_2)

    board.printArrayWithCord()
    
    game(board, beginner, depth)




def getBeginner():
    
    while True:
        player = input('Select who begins the game:\n(U) - user\n(C) - computer\n'  )[0]
        if player.lower() == 'c' or player.lower() == 'u':
            return player.lower()
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
    
    print('Insert board size: ')
    while True:
        size = int(input(''))
        
        if size < 2:
            print('Wrong dimensions. Try again.')
        else:
            break
    return size


main()