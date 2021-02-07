from unittest import TestCase

from src.StringNumUtil import *


class TestNumericStringParser(TestCase):
    def test_eval(self):
        failing_eval = "(1)+((2)+((3+4^5^6)))"
        evaluate(failing_eval)

    def test_manage_overflow(self):
        evaluate("9**9**9**9**9**9**9**9")






