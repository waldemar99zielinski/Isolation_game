import constants

class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = [constants.AVAILABLE for x in range(width*height)] 


    def get_position(self, x, y):
        return self.array[y*self.width+x]


    def printArray(self):
        for j in range(0,self.height):
            for i in range (0, self.width):
               print(self.array[j*self.width+i], end=" ")
            print() 


    def set_position(self, x, y, value):
        # print('new position set: ', x, y, ' with value ', value)
        self.array[y*( self.width )+x] = value


    def get_index(self, value):
        index = self.array.index(value)
        return index%self.width, int(index/self.height)


    def set_board(self, board):
        self.array = board;


    def is_move_legal(self, px, py):
       
        if px < 0 or px >= self.width:
            return False
        if py < 0 or py >= self.height:
            return False
        if self.get_position(px, py) == constants.AVAILABLE:
            return True

        return False
