from unittest import TestCase

import src.HectocSolver


class Test(TestCase):
    def test_split_in_pieces(self):
        pieces = src.HectocSolver.split_in_pieces([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 4)
        self.assertEqual(pieces, [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11]])
