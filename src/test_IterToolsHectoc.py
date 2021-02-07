from unittest import TestCase
import unittest

from src import IterToolsHectoc


class Test(TestCase):
    def test_list_all(self):
        self.fail()

    def test_all_concatenate_options(self):
        allPermutations = IterToolsHectoc.list_all(IterToolsHectoc.operators, [1, 2, 3, 4, 5, 6])
        print(allPermutations)

    def test_all_concatenate_options(self):
        allPermutations = IterToolsHectoc.get_num_combinations([1])
        self.assertEqual(1, len(allPermutations))

        allPermutations = IterToolsHectoc.get_num_combinations([1, 2])
        self.assertEqual(2, len(allPermutations))
        self.assertListEqual([[1, 2], [12]], allPermutations)

    def test_all_concatenate_options_three_numbers(self):
        allPermutations = IterToolsHectoc.get_num_combinations([1, 2, 3])
        self.assertEqual([[1, 2, 3], [12, 3], [1, 23], [123]].sort(), allPermutations.sort())

    def test_all_concatenate_options_four_numbers(self):
        allPermutations = IterToolsHectoc.get_num_combinations([1, 2, 3, 4])
        self.assertEqual([[1, 2, 3, 4],
                          [12, 3, 4],
                          [1, 23, 4],
                          [1, 2, 34],
                          [123, 4],
                          [1, 234],
                          [1234]
                          ].sort(), allPermutations.sort())

    def test_find_first_double_digit(self):
        index = IterToolsHectoc.find_first_double_digit([0, 20, 1])
        self.assertEqual(index, 1)
        self.assertEqual(IterToolsHectoc.find_first_double_digit([0, 0, 20]), 2)
        self.assertEqual(IterToolsHectoc.find_first_double_digit([0, 0, 1]), 0)

    def test_get_all_expressions_for_values_and_operators(self):
        expressions = IterToolsHectoc.get_permutations_for_val_and_op(['1', '2'], ['+', '-'])
        self.assertEqual(['1+2', '1-2'], expressions)
        expressions = IterToolsHectoc.get_permutations_for_val_and_op(['1', '2', '3'], ['+', '-'])
        self.assertEqual(['1+2+3', '1-2-3', '1+2-3', '1-2+3'].sort(), expressions.sort())
        expressions = IterToolsHectoc.get_permutations_for_val_and_op([1, 2, 3], ['+', '-'])
        self.assertEqual(['1+2+3', '1-2-3', '1+2-3', '1-2+3'].sort(), expressions.sort())

    def test_combine_expressions_and_cffoncat(self):
        allPermutations = IterToolsHectoc.get_all_concatenated_combinations_with_operators([1, 2, 3], ['+', '-'])
        print(allPermutations)

    def test_combine_expressions_and_concat(self):
        allPermutations = IterToolsHectoc.get_all_concatenated_combinations_with_operators([1, 2, 3], ['+', '-', '^', '/', '*'])
        print(allPermutations)
        print(len(allPermutations))

    def test_combine_expressions_and_concat(self):
        allPermutations = IterToolsHectoc.get_all_concatenated_combinations_with_operators([1, 2, 3, 4, 5, 6], ['+', '-', '^', '/', '*'])
        print(allPermutations)
        print(len(allPermutations))

    def test_combine_expressions_and_concsssat(self):
        allPermutations = IterToolsHectoc.get_all_concatenated_combinations_with_operators([1, 2, 3, 4, 5, 6], ['+', '-', '^', '/', '*'])
        print(allPermutations)
        print(len(allPermutations))

    def test_combine_expresddsions_and_concsssat(self):
        allPermutations = IterToolsHectoc.get_all_concatenated_combinations_with_operators([1, 2, 3], ['+', '-', '^'])
        options = IterToolsHectoc.find_all_paranthesized_options(allPermutations)
        solve = IterToolsHectoc.solve(options, 6)
        print(options)
        print(solve)

        print(len(allPermutations))



