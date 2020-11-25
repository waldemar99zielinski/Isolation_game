import unittest
from board import Board
from iso import get_all_possibilities, game, gameAI
import constants

class EndStateChecker(unittest.TestCase):

    def testPlayer1NoMoves(self):
        '''
        [   1 4 0
            4 4 0
            0 0 2 ]
        '''
        board = Board(3,3)
        board.set_position(0, 0, constants.PLAYER_1)
        board.set_position(2, 2, constants.PLAYER_2)
        board.set_position(0, 1, constants.VOID)
        board.set_position(1, 0, constants.VOID)
        board.set_position(1, 1, constants.VOID)
        result = get_all_possibilities(board, constants.PLAYER_1)
        self.assertEqual(
            [],
            result
        )

    def testPlayer2NoMoves(self):
        '''
        [   1 0 0
            4 4 4
            4 4 2 ]
        '''
        board = Board(3, 3)
        board.set_position(0, 0, constants.PLAYER_1)
        board.set_position(2, 2, constants.PLAYER_2)
        board.set_position(0, 1, constants.VOID)
        board.set_position(1, 1, constants.VOID)
        board.set_position(2, 1, constants.VOID)
        board.set_position(0, 2, constants.VOID)
        board.set_position(1, 2, constants.VOID)
        # board.printArray()
        result = get_all_possibilities(board, constants.PLAYER_2)
        self.assertEqual( 
            [], 
            result 
        )

    def testUserLossAtBeginning(self):
        ''' [   1
                2 ]
        '''
        first_player = 'u'
        depth = 2
        board = Board(1, 2)
        board.set_position(0, 0, constants.PLAYER_1)
        board.set_position(0, 1, constants.PLAYER_2)
        # board.printArray()
        result = game(board, first_player, depth)
        self.assertEqual(
            first_player,
            result
        )

    def testAILossAtBeginning(self):
        ''' [   1
                2 ]
        '''
        first_player = 'c'
        depth = 2
        board = Board(1, 2)
        board.set_position(0, 0, constants.PLAYER_1)
        board.set_position(0, 1, constants.PLAYER_2)
        # board.printArray()
        result = game(board, first_player, depth)
        self.assertEqual(
            first_player,
            result
        )
    def testAIvsAI(self):
        '''[ 1 0 0
             0 0 0
             0 0 2]
        '''
        first_player = constants.PLAYER_1
        depth = 2
        board = Board(3,3)
        board.set_position(0, 0, constants.PLAYER_1)
        board.set_position(2, 2, constants.PLAYER_2)
        result = gameAI(board, first_player, depth)
        self.assertEqual(
            'c',
            result
        )


if __name__ == '__main__':
    unittest.main()