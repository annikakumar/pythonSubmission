from __future__ import division

import ast
import operator as op
from copy import deepcopy


class NumericStringParser(object):
    """
    Class dealing with evaluation and formatting issues of arithmetic string expressions
    """

    def parenthesize(self, string):
        '''
        Return a list of all ways to completely parenthesize operator/operand string
        '''
        operators = ['+', '-', '*', '/', '^']
        depth = len([s for s in string if s in operators])
        if depth == 0:
            return [string]
        if depth == 1:
            return ['(' + string + ')']
        answer = []
        for index, symbol in enumerate(string):
            if symbol in operators:
                left = string[:index]
                right = string[(index + 1):]
                strings = ['(' + lt + ')' + symbol + '(' + rt + ')'
                           for lt in self.parenthesize(left)
                           for rt in self.parenthesize(right)]
                answer.extend(strings)
        return answer

    def remove_all_redundant_brackets_and_replace_pow(self, solutions):
        """
        removes all redundant brackets from expressions and replaces the ** from eval with readable ^
        :param solutions: the solutions eith possibly redundant brackets
        :return: solutions without redundant brackets and with the readably power operator
        """
        solution_iter = deepcopy(solutions)
        for solution in solution_iter:
            without_brackets = self.remove_inner_brackets(solution)
            if (without_brackets != solution):
                solutions.remove(solution)
            if (without_brackets not in solution):
                solutions.append(without_brackets.replace('**', '^'))
        return solutions

    def remove_all_redundant_brackets_and_duplicates(self, solutions):
        return list(set(self.remove_all_redundant_brackets_and_replace_pow(solutions)))

    def remove_inner_brackets(self, expression):
        """
        removes redundant brackets of a single expression
        :param expression: the string to be cleansed of redundant brackets
        :return: the cleansed expression
        """
        opening_bracket_index = 0
        while True:
            try:
                opening_bracket_index = expression.index("(", opening_bracket_index)
            except ValueError:
                break

            moving_closing_bracket_index = opening_bracket_index
            moving_closing_bracket_index = self.find_closing_bracket_index(opening_bracket_index, moving_closing_bracket_index, expression)

            new_term = expression[:opening_bracket_index] + expression[opening_bracket_index + 1:moving_closing_bracket_index] + expression[
                                                                                                                                 moving_closing_bracket_index + 1:]
            is_minus_after_single_bracket = expression[opening_bracket_index + 1] == "-" \
                                            and expression[opening_bracket_index - 1] is not None \
                                            and expression[opening_bracket_index - 1] != "("

            if evaluate(expression) != evaluate(new_term) or is_minus_after_single_bracket:
                opening_bracket_index += 1
                continue
            expression = new_term
        return expression

    def find_closing_bracket_index(self, a, b, term):
        while True:
            b = term.index(")", b + 1)
            if term[a + 1:b].count("(") == term[a + 1:b].count(")"):
                break
        return b


operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg}


def evaluate(expr):
    return eval_(ast.parse(expr, mode='eval').body)

def eval_(node):
    try:
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return operators[type(node.op)](eval_(node.left), eval_(node.right))
        elif isinstance(node, ast.UnaryOp):
            return operators[type(node.op)](eval_(node.operand))
        else:
            raise TypeError(node)
    except:
        pass

def power(a, b):
    """
    in order to restrict the value range and avoid endless running times of evaluations
    """
    if any(abs(n) > 1000 for n in [a, b]):
        raise ValueError((a, b))
    return op.pow(a, b)


operators[ast.Pow] = power
