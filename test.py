import unittest
from board import Board
from game import game, ai_game
from helpers import get_all_possibilities
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
        size = 3
        board = Board(size, size)
        board.set_position(0, 0, constants.PLAYER_1)
        board.set_position(2, 2, constants.PLAYER_2)
        result = ai_game(board, first_player, depth)
        self.assertEqual(
            'c',
            result
        )

    # def testDepthSizeAI(self):
    #     for depth in range(1, 2):
    #         for size in range (3, 5):
    #             for run in range(1, 6):
    #                 with self.subTest('run'):
    #                     print('Depth ', depth, ' size ', size, 'x', size, ' run ', run)
    #                     board = Board(size, size)
    #                     board.set_position(0, 0, constants.PLAYER_1)
    #                     board.set_position(size - 1, size - 1, constants.PLAYER_2)
    #                     result = ai_game(board, constants.PLAYER_1, depth)
    #                     del board
    #     self.assertEqual(
    #         'c',
    #         result
    #     )

    def testWrongAI(self):
        first_player = 'xd'
        depth = 2
        size = 3
        board = Board(size, size)
        board.set_position(0, 0, constants.PLAYER_1)
        board.set_position(2, 2, constants.PLAYER_2)
        result = ai_game(board, first_player, depth)

        self.assertEqual(
            1,
            result
        )

    def testWrongPlayer(self):
        first_player = 'xd'
        depth = 2
        size = 3
        board = Board(size, size)
        board.set_position(0, 0, constants.PLAYER_1)
        board.set_position(2, 2, constants.PLAYER_2)
        result = game(board, first_player, depth)

        self.assertEqual(
            1,
            result
        )

    def testAIClassic(self):
        first_player = 1
        depth = 2
        size = 3
        board = Board(size, size)
        board.set_position(0, 0, constants.PLAYER_1)
        board.set_position(size - 1, size - 1, constants.PLAYER_2)
        result = ai_game(board, first_player, depth)

        self.assertEqual(
            'c',
            result
        )
    
if __name__ == '__main__':
    unittest.main()