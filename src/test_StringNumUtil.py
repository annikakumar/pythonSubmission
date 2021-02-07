from unittest import TestCase

from src.StringNumUtil import *


class TestNumericStringParser(TestCase):
    def test_parenthesize(self):
        failing_eval = "(1)+((2)+((3+4^5^6)))"
        nsp = NumericStringParser()
        nsp.eval(failing_eval)

    def test_kjhjh(self):
        print(evaluate("9**9"))
        print(evaluate("2**3"))