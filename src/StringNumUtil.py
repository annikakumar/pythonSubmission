from __future__ import division

from copy import deepcopy

from pyparsing import (Literal, CaselessLiteral, Word, Combine, Group, Optional,
                       ZeroOrMore, Forward, nums, alphas, oneOf)
import operator

__author__ = 'Paul McGuire'
__version__ = '$Revision: 0.0 $'
__date__ = '$Date: 2009-03-20 $'
__source__ = '''http://pyparsing.wikispaces.com/file/view/fourFn.py
http://pyparsing.wikispaces.com/message/view/home/15549426
'''
__note__ = '''
All I've done is rewrap Paul McGuire's fourFn.py as a class, so I can use it
more easily in other places.
'''


class NumericStringParser(object):
    '''
    Most of this code comes from the fourFn.py pyparsing example

    '''

    def pushFirst(self, strg, loc, toks):
        self.exprStack.append(toks[0])

    def pushUMinus(self, strg, loc, toks):
        if toks and toks[0] == '-':
            self.exprStack.append('unary -')

    def __init__(self):
        """
        expop   :: '^'
        multop  :: '*' | '/'
        addop   :: '+' | '-'
        integer :: ['+' | '-'] '0'..'9'+
        atom    :: PI | E | real | fn '(' expr ')' | '(' expr ')'
        factor  :: atom [ expop factor ]*
        term    :: factor [ multop factor ]*
        expr    :: term [ addop term ]*
        """
        point = Literal(".")
        e = CaselessLiteral("E")
        fnumber = Combine(Word("+-" + nums, nums) +
                          Optional(point + Optional(Word(nums))) +
                          Optional(e + Word("+-" + nums, nums)))
        ident = Word(alphas, alphas + nums + "_$")
        plus = Literal("+")
        minus = Literal("-")
        mult = Literal("*")
        div = Literal("/")
        lpar = Literal("(").suppress()
        rpar = Literal(")").suppress()
        addop = plus | minus
        multop = mult | div
        expop = Literal("^")
        pi = CaselessLiteral("PI")
        expr = Forward()
        atom = ((Optional(oneOf("- +")) +
                 (ident + lpar + expr + rpar | pi | e | fnumber).setParseAction(self.pushFirst))
                | Optional(oneOf("- +")) + Group(lpar + expr + rpar)
                ).setParseAction(self.pushUMinus)
        # by defining exponentiation as "atom [ ^ factor ]..." instead of
        # "atom [ ^ atom ]...", we get right-to-left exponents, instead of left-to-right
        # that is, 2^3^2 = 2^(3^2), not (2^3)^2.
        factor = Forward()
        factor << atom + \
        ZeroOrMore((expop + factor).setParseAction(self.pushFirst))
        term = factor + \
               ZeroOrMore((multop + factor).setParseAction(self.pushFirst))
        expr << term + \
        ZeroOrMore((addop + term).setParseAction(self.pushFirst))
        # addop_term = ( addop + term ).setParseAction( self.pushFirst )
        # expr <<  general_term
        self.bnf = expr
        # map operator symbols to corresponding arithmetic operations
        self.opn = {"+": operator.add,
                    "-": operator.sub,
                    "*": operator.mul,
                    "/": operator.truediv,
                    "^": operator.pow}

    def evaluateStack(self, s):
        op = s.pop()
        if op == 'unary -':
            return -self.evaluateStack(s)
        if op in "+-*/^":
            op2 = self.evaluateStack(s)
            op1 = self.evaluateStack(s)
            return self.opn[op](op1, op2)
        elif op in self.fn:
            return self.fn[op](self.evaluateStack(s))
        elif op[0].isalpha():
            return 0
        else:
            return float(op)

    def eval(self, num_string, parseAll=True):
        self.exprStack = []
        self.bnf.parseString(num_string, parseAll)
        val = self.evaluateStack(self.exprStack[:])
        return val

    def parenthesize(self, string):
        '''
        Return a list of all ways to completely parenthesize operator/operand string
        '''
        operators = ['+', '-', '*', '/']
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

    def remove_all_redundant_brackets(self, solutions):
        solution_iter = deepcopy(solutions)
        for solution in solution_iter:
            without_brackets = self.remove_inner_brackets(solution)
            if (without_brackets != solution):
                solutions.remove(solution)
            if (without_brackets not in solution):
                solutions.append(without_brackets)
        return solutions


    def remove_all_redundant_brackets_and_duplicates(self, solutions):
        return list(set(self.remove_all_redundant_brackets(solutions)))


    def remove_inner_brackets(self, term):
        opening_bracket_index = 0
        while True:
            try:
                opening_bracket_index = term.index("(", opening_bracket_index)
            except ValueError:
                # No (more) opening brackets found
                break

            moving_closing_bracket_index = opening_bracket_index
            moving_closing_bracket_index = self.find_closing_bracket_index(opening_bracket_index, moving_closing_bracket_index, term)

            new_term = term[:opening_bracket_index] + term[opening_bracket_index + 1:moving_closing_bracket_index] + term[
                                                                                                                     moving_closing_bracket_index + 1:]

            # If new term produces opening_bracket_index different value, keep term as it is and try with the next pair of brackets
            is_minus_after_single_bracket = term[opening_bracket_index + 1] == "-" \
                                            and term[opening_bracket_index - 1] is not None \
                                            and term[opening_bracket_index - 1] != "("

            if evaluate(term) != evaluate(new_term) or is_minus_after_single_bracket:
                opening_bracket_index += 1
                continue
            # Adopt new term
            term = new_term
        return term

    def find_closing_bracket_index(self, a, b, term):
        while True:
            b = term.index(")", b + 1)
            if term[a + 1:b].count("(") == term[a + 1:b].count(")"):
                break
        return b


import ast, math

locals =  {key: value for (key,value) in vars(math).items() if key[0] != '_'}
locals.update({"abs": abs, "complex": complex, "min": min, "max": max, "pow": pow, "round": round})

class Visitor(ast.NodeVisitor):
    def visit(self, node):
       if not isinstance(node, self.whitelist):
           raise ValueError(node)
       return super().visit(node)

    whitelist = (ast.Module, ast.Expr, ast.Load, ast.Expression, ast.Add, ast.Sub, ast.UnaryOp, ast.Num, ast.BinOp,
            ast.Mult, ast.Div, ast.Pow, ast.BitOr, ast.BitAnd, ast.BitXor, ast.USub, ast.UAdd, ast.FloorDiv, ast.Mod,
            ast.LShift, ast.RShift, ast.Invert, ast.Call, ast.Name)

def evaluate(expr, locals = {}):
    if any(elem in expr for elem in '\n#') : raise ValueError(expr)
    try:
        node = ast.parse(expr.strip(), mode='eval')
        Visitor().visit(node)
        return eval(compile(node, "<string>", "eval"), {'__builtins__': None}, locals)
    except Exception: raise ValueError(expr)