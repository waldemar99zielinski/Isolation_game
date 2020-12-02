import unittest
from board import Board
from game import game, ai_game
from algorithms import minmax, alphabeta
from constants import PLAYER_1, PLAYER_2, VOID


class AlgorithmTests(unittest.TestCase):

    def testminmaxCorner(self):

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
        """
        [
            0, 0, 0, 4, 2,
            0, 0, 0, 4, 4,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 1, 0, 0,
        ]
        """
        self.assertEqual(

            result.get_position(3, 1),
            VOID

        )

    def testAlfabetaCorner(self):

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
        """
        [
            0, 0, 0, 4, 2,
            0, 0, 0, 4, 4,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 1, 0, 0,
        ]
        """
        self.assertEqual(

            result.get_position(3, 1),
            VOID

        )

    def testminmaxTunnel(self):
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
        """
        [
            0, 0, 0, 4, 2,
            0, 0, 0, 4, 4,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 1, 0, 0,
        ]
        """
        self.assertEqual(

            result.get_position(2, 1),
            VOID

        )

    def testalfabetaTunnel(self):
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
        """
        [
            0, 0, 0, 4, 2,
            0, 0, 0, 4, 4,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0,
            0, 0, 1, 0, 0,
        ]
        """
        self.assertEqual(

            result.get_position(2, 1),
            VOID

        )


if __name__ == '__main__':
    unittest.main()