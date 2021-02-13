from unittest import TestCase

from src.HectocStrategy import HectocStrategy

class Test(TestCase):
    def test_split_in_pieces(self):
        pieces = HectocStrategy().split_in_pieces([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 4)
        self.assertEqual(pieces, [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11]])
