from unittest import TestCase
from src.HectocPartialEquationSolver import *


class Test(TestCase):

    def test_solve_hectoc_problem(self):
        solution = solve(846659)
        self.assertTrue("84+6+6-5+9" in solution)
    def test_solve_two_digits_add(self):
        solution = solve_two_number_hectoc_equation('1', '2', 3)
        self.assertTrue("(1+2)" in solution)

    def test_solve_two_digits_minus(self):
        solution = solve_two_number_hectoc_equation('2', '3', 1)
        self.assertTrue("(-2+3)" in solution)

    def test_solve_two_digits_minus(self):
        solution = solve_two_number_hectoc_equation('22', '21', 1)
        self.assertTrue("(22-21)" in solution)

    def test_solve_two_digits_pow(self):
        solution = solve_two_number_hectoc_equation('2', '3', 8)
        self.assertTrue("(2^3)" in solution)

    def test_solve_two_digits_mult(self):
        solution = solve_two_number_hectoc_equation('2', '3', 6)
        self.assertTrue("(2*3)" in solution)

    def test_get_concatenate_int(self):
        self.assertEqual(get_concatenate_int(1, 2), 12)
        self.assertEqual(get_concatenate_int(1, 200), 1200)
        self.assertEqual(get_concatenate_int(4, 2), 42)
        self.assertEqual(get_concatenate_int(233, 2), 2332)

    def test_solve_three_digits_equation(self):
        solutions = solve_three_number_hectoc_equation('1', '2', '3', 4)
        self.assertTrue("(1^2+3)" in solutions)
        self.assertTrue("(-1+2+3)" in solutions)

    def test_solve_three_number_equation_concat_three_digitjjs(self):
        solutions = solve_three_number_hectoc_equation('1', '2', '3', 123)
        self.assertTrue("123" in solutions)

    def test_solve_three_number_equation_concat_two_digitsMadd(self):
        solutions = solve_three_number_hectoc_equation('1', '2', '3', 15)
        self.assertTrue("(12+3)" in solutions)

    def test_solve_three_number_equation_concat_two_digitsMaffdd(self):
        solutions = solve_three_number_hectoc_equation('1', '2', '30', 18)
        self.assertTrue("(-12+30)" in solutions)

    def test_solve_three_number_equation_concatdd_two_digitsMadd(self):
        solutions = solve_three_number_hectoc_equation('12', '2', '3', 4)
        print(solutions)
        self.assertTrue("(12+(-2^3))" in solutions)

    def test_solve_three_number_equation_remove_redundant_brackets(self):
        solutions = solve_three_number_hectoc_equation('12', '2', '3', 4)
        self.assertTrue("(12-2^3)" in solutions)
        self.assertFalse("(12-(2^3))" in solutions)

    def test_solve_three_number_equation_concat_two_digits(self):
        solutions = solve_three_number_hectoc_equation('1', '2', '3', 7)
        print(solutions)
        self.assertTrue("(1+2*3)" in solutions)
        self.assertTrue("(-1+2^3)" in solutions)

    def test_solve_four_digits_equation_single(self):
        solutions = solve_four_number_hectoc_equation('1', '2', '3', '4', 10)
        self.assertTrue("(1+2+3+4)" in solutions)
        self.assertFalse("(1+(2+3)+4)" in solutions)


    def test_solve_four_digits_equation_singmmmle(self):
        solutions = solve_four_number_hectoc_equation('1', '2', '3', '3', 10)
        self.assertTrue("(-1^2+3*3)" in solutions)
        self.assertFalse("((-1^2)+3*3)" in solutions)

    def test_solve_four_digits_equation_single_(self):
        solutions = solve_four_number_hectoc_equation('1', '2', '3', '4', 1234)
        print(solutions)
        self.assertTrue("1234" in solutions)

    def test_solve_four_digits_equation_singl__e(self):
        solutions = solve_four_number_hectoc_equation('1', '2', '3', '4', 119)
        print(solutions)
        self.assertTrue("(123-4)" in solutions)
