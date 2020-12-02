import unittest
from board import Board
from game import game, ai_game
from algorithms import minmax, alphabeta
from constants import PLAYER_1, PLAYER_2, VOID


class AlgorithmTests(unittest.TestCase):

    #simulate catching opponent in a corrner trap with pure minmax
    def testMinMaxCorner(self):

        board = Board(5, 5)
        b = [
            0, 0, 0, 4, 2,
            0, 0, 0, 0, 4,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 1, 0, 0,
        ]
        board.set_board(b)
        #board.printArrayWithCord()
        value, result = minmax(board, 2, PLAYER_1)
    
        self.assertEqual(

            result.get_position(3, 1),
            VOID

        )

    #simulate catching opponent in a corner trap with alpha-beta pruning
    def testAlphaBetaCorner(self):

        board = Board(5, 5)
        b = [
            0, 0, 0, 4, 2,
            0, 0, 0, 0, 4,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 1, 0, 0,
        ]
        board.set_board(b)
        #board.printArrayWithCord()
        value, result = alphabeta(board, 2, PLAYER_1, float('-inf'), float('inf'))

        self.assertEqual(

            result.get_position(3, 1),
            VOID

        )

    #simulate catching opponent in a trap with pure minmax
    def testMinMaxTunnelOffensive(self):
        board = Board(5, 5)
        b = [
            0, 4, 1, 4, 0,
            0, 4, 0, 4, 4,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 2, 0, 0,
        ]
        board.set_board(b)
        # board.printArrayWithCord()
        value, result = minmax(board, 2, PLAYER_2)

        self.assertEqual(

            result.get_position(2, 1),
            VOID

        )

    #simulate catching opponent in a tunnel trap with alpha-beta pruning
    def testAlphaBetaTunnelOffensive(self):
        board = Board(5, 5)
        b = [
            0, 4, 1, 4, 0,
            0, 4, 0, 4, 4,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 2, 0, 0,
        ]
        board.set_board(b)
        # board.printArrayWithCord()
        value, result = alphabeta(board, 2, PLAYER_2,float('-inf'), float('inf'))

        self.assertEqual(

            result.get_position(2, 1),
            VOID

        )

    #simulate getting out of tunnel trap with alpha-beta pruning
    def testAlphaBetaTunnelDefensive(self):

            board = Board(5, 5)
            b = [
                0, 4, 0, 4, 0,
                0, 4, 1, 4, 4,
                0, 4, 0, 4, 0,
                0, 0, 0, 0, 0,
                0, 0, 2, 0, 0,
            ]
            board.set_board(b)
            # board.printArrayWithCord()
            value, result = alphabeta(board, 3, PLAYER_1, float('-inf'), float('inf'))

            self.assertEqual(

                result.get_position(2, 2),
                PLAYER_1

            )

    #simulate getting out of tunnel trap with MinMax
    def testTunnelDefMinMax(self):
        board = Board(5, 5)
        b = [
            0, 4, 0, 4, 0,
            0, 4, 1, 4, 4,
            0, 4, 0, 4, 0,
            0, 0, 0, 0, 0,
            0, 0, 2, 0, 0,
        ]
        board.set_board(b)
        # board.printArrayWithCord()
        value, result = minmax(board, 2, PLAYER_1)

        self.assertEqual(

            result.get_position(2, 2),
            PLAYER_1

        )

    #simulate whole game between two computers
    def testAIvsAI(self):
        '''[ 1 0 0
             0 0 0
             0 0 2]
        '''
        first_player = PLAYER_1
        depth = 2
        size = 3
        board = Board(size, size)
        board.set_position(0, 0, PLAYER_1)
        board.set_position(2, 2, PLAYER_2)

        loser = ai_game(board, first_player, depth)

        self.assertEqual(
            'c',
            loser
        )

if __name__ == '__main__':
    unittest.main()