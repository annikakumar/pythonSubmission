from copy import deepcopy
from pylint.checkers import typecheck
from src.StringNumUtil import NumericStringParser

operators = ["+", "-", "*", "/", "^"]
nsp = NumericStringParser()


def get_concatenate_int(input: int, secondinput: int) -> int:
    return int(str(input) + str(secondinput))


def solve_two_number_hectoc_equation(input: str, secondinput: str, result: int) -> [str]:
    solutions = []
    for singleOperator in operators:
        solving_string = "(" + input + singleOperator + secondinput + ")"
        neg_solving_string = "(-" + input + singleOperator + secondinput + ")"
        if nsp.eval(solving_string) == result:
            solutions.append(solving_string)
        if nsp.eval(neg_solving_string) == result:
            solutions.append(neg_solving_string)
    if (int(input + secondinput)) == result:
        solutions.append(input + secondinput)
    return list(set(solutions))


def remove_inner_brackets(term):
    opening_bracket_index = 1
    while True:
        try:
            opening_bracket_index = term.index("(", opening_bracket_index)
        except ValueError:
            # No (more) opening brackets found
            break

        moving_closing_bracket_index = opening_bracket_index
        moving_closing_bracket_index = find_closing_bracket_index(opening_bracket_index, moving_closing_bracket_index, term)

        new_term = term[:opening_bracket_index] + term[opening_bracket_index + 1:moving_closing_bracket_index] + term[
                                                                                                                 moving_closing_bracket_index + 1:]

        # If new term produces opening_bracket_index different value, keep term as it is and try with the next pair of brackets
        if nsp.eval(term) != nsp.eval(new_term) or term[opening_bracket_index + 1] == "-":
            opening_bracket_index += 1
            continue
        # Adopt new term
        term = new_term
    return term


def find_closing_bracket_index(a, b, term):
    while True:
        b = term.index(")", b + 1)
        if term[a + 1:b].count("(") == term[a + 1:b].count(")"):
            break
    return b


def solve_three_number_hectoc_equation(input: str, secondinput: str, thirdinput: str, result: int):
    solutions = []

    solutions.extend(solve_two_number_hectoc_equation((input + secondinput), thirdinput, result))
    solutions.extend(solve_two_number_hectoc_equation(input, (secondinput + thirdinput), result))

    for operator in operators:
        neg_solving_string, solving_string = get_negative_and_positive_solving_string(input, operator, secondinput)
        append_if_matches(result, solutions, solving_string)
        append_if_matches(result, solutions, neg_solving_string)

        for second_op in operators:
            candidates = get_candidates_with_brackets(input, operator, secondinput, second_op, thirdinput)
            for candidate in candidates:
                append_if_matches(result, solutions, candidate)

    all_concatenate = input + secondinput + thirdinput
    if int(all_concatenate) == result:
        solutions.append(all_concatenate)

    return remove_all_redundant_brackets_and_duplicates(solutions)


def remove_all_redundant_brackets_and_duplicates(solutions):
    solution_iter = deepcopy(solutions)
    for solution in solution_iter:
        without_brackets = remove_inner_brackets(solution)
        if (without_brackets != solution):
            solutions.remove(solution)
        if (without_brackets not in solution):
            solutions.append(without_brackets)
    return list(set(solutions))


def append_if_matches(result: int, solutions: [str], solving_string: str) -> bool:
    if nsp.eval(solving_string) == result:
        solutions.append(solving_string)
        return True
    return False


def get_candidates_with_brackets(input: str, operator: str, secondinput: str, second_op: str, thirdinput: str) -> [str]:
    candidates = ["(" + input + operator + secondinput + second_op + thirdinput + ")",
                  "(-" + input + operator + secondinput + second_op + thirdinput + ")",
                  "((" + input + operator + secondinput + ")" + second_op + thirdinput + ")",
                  "((-" + input + operator + secondinput + ")" + second_op + thirdinput + ")",
                  "(" + input + operator + "(" + secondinput + second_op + thirdinput + "))",
                  "(" + input + operator + "(-" + secondinput + second_op + thirdinput + "))"]

    return candidates


def get_candidates_with_brackets_four_numbers(input: str, operator: str, secondinput: str, second_op: str,
                                              thirdinput: str, third_op: str, fourthinput: str) -> [str]:
    candidates = []
    first_three = get_candidates_with_brackets(input, operator, secondinput, second_op, thirdinput, third_op)
    last_three = get_candidates_with_brackets(secondinput, second_op, thirdinput, third_op, fourthinput)

    for candidate in first_three:
        candidates.append("(" + candidate + third_op + fourthinput + ")")
    for candidate in last_three:
        candidates.append("(" + input + operator + candidate + ")")
        candidates.append("(-" + input + operator + candidate + ")")

    return candidates


def get_negative_and_positive_solving_string(input, operator, secondinput):
    solving_string = "(" + input + operator + secondinput + ")"
    neg_solving_string = "(-" + input + operator + secondinput + ")"
    return neg_solving_string, solving_string

def solve_four_number_hectoc_equation(input: str, secondinput: str, thirdinput: str, fourthinput: str, result: int) -> [str]:
    5
