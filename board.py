import constants

class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = [constants.AVAILABLE for x in range(constants.BOARDWIDTH*constants.BOARDHEIGHT)] 


    def get_position(self, x, y):
        return self.array[y*constants.BOARDWIDTH+x]


    def printArray(self):
        for j in range(0,constants.BOARDHEIGHT):
            for i in range (0, constants.BOARDWIDTH):
               print(self.array[j*constants.BOARDWIDTH+i], end=" ")
            print() 


    def set_position(self, x, y, value):
        # print('new position set: ', x, y, ' with value ', value)
        self.array[y*( constants.BOARDWIDTH )+x] = value


    def get_index(self, value):
        index = self.array.index(value)
        return index%constants.BOARDWIDTH, int(index/constants.BOARDHEIGHT)


    def set_board(self, board):
        self.array = board;


    def is_move_legal(self, px, py):
       
        if px < 0 or px >= constants.BOARDWIDTH:
            return False
        if py < 0 or py >= constants.BOARDHEIGHT:
            return False
        if self.get_position(px, py) == constants.AVAILABLE:
            return True

        return False
