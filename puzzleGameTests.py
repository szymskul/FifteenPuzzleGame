import unittest
import FifteenPuzzleGame

class TestMoveFunction(unittest.TestCase):

    def test_move_left(self):
        board = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 0, 11],
            [12, 13, 14, 15]
        ]
        expected_board = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 0, 10, 11],
            [12, 13, 14, 15]
        ]
        FifteenPuzzleGame.moveFunction("L", board)
        self.assertEqual(board, expected_board)

    def test_move_right(self):
        board = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 0, 11],
            [12, 13, 14, 15]
        ]
        expected_board = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 0],
            [12, 13, 14, 15]
        ]
        FifteenPuzzleGame.moveFunction("R", board)
        self.assertEqual(board, expected_board)

    def test_move_up(self):
        board = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 0, 11],
            [12, 13, 14, 15]
        ]
        expected_board = [
            [1, 2, 3, 4],
            [5, 6, 0, 8],
            [9, 10, 7, 11],
            [12, 13, 14, 15]
        ]
        FifteenPuzzleGame.moveFunction("U", board)
        self.assertEqual(board, expected_board)

    def test_move_down(self):
        board = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 0, 11],
            [12, 13, 14, 15]
        ]
        expected_board = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 14, 11],
            [12, 13, 0, 15]
        ]
        FifteenPuzzleGame.moveFunction("D", board)
        self.assertEqual(board, expected_board)

    def test_incorrect_move(self):
        board = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 0],
            [12, 13, 14, 15]
        ]
        expected_board = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 0],
            [12, 13, 14, 15]
        ]
        FifteenPuzzleGame.moveFunction("R", board)
        self.assertEqual(board, expected_board)

    def test_checking_board(self):
        board = [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 0, 11],
                [12, 13, 14, 15]
        ]
        expected_board = [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 0, 11],
                [12, 13, 14, 15]
        ]
        not_excepted_board = [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 0]
        ]
        FifteenPuzzleGame.checkingBoard(board, expected_board)
        self.assertEqual(board, expected_board)
        FifteenPuzzleGame.checkingBoard(board, not_excepted_board)
        self.assertNotEqual(board, not_excepted_board)

if __name__ == '__main__':
    unittest.main()