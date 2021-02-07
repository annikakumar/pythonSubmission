import itertools
from src.StringNumUtil import *
operators = ["+", "-", "*", "/", "**"]
nsp = NumericStringParser()

def get_permutations_for_val_and_op(val, ops):
    """
    constructing all possible combinations of values and operators to be conbines in a hectonian way

    :param val: an array of int values
    :param ops: the considered operators
    :return: an array of all combination for the hectoc puzzle
    """
    lst_expr = []
    for values in [val]:
        n = len(values)
        if n >= 1:
            all_operators = list(itertools.product(ops, repeat=len(val) - 1))
            for operators in all_operators:
                exp = str(values[0])
                i = 1
                for operator in operators:
                    exp += operator + str(values[i])
                    i += 1
                lst_expr += [exp]
    return lst_expr

def get_num_combinations(input_number_array: [int]) -> [[int]]:
    results = [deepcopy(input_number_array)]

    if len(input_number_array) == 1:
        return results

    temp_array = input_number_array
    for index in range(find_first_double_digit(temp_array), len(temp_array) - 1):
        new_temp_array = deepcopy(temp_array)
        new_temp_array[index] = int(str(new_temp_array[index]) + str(new_temp_array[index + 1]))
        new_temp_array.pop(index + 1)
        results.extend(get_num_combinations(new_temp_array))
    return results


def get_all_concatenated_combinations_with_operators(values, op_meth):
    concat_combinations = get_num_combinations(values)
    candidates = []
    for combination in concat_combinations:
        concat_combination = get_permutations_for_val_and_op(combination, op_meth)
        candidates.extend(concat_combination)
    return candidates


def find_first_double_digit(temp_array):
    try:
        return next(x[0] for x in enumerate(temp_array) if x[1] > 10)
    except StopIteration:
        return 0


def find_all_paranthesized_options(single_array):
    all_options = []
    for i in single_array:
        all_options.extend(nsp.parenthesize(i))
    return all_options


def solve(paranthesized_options, result=100):
    print("Checking " + str(len(paranthesized_options)) + " candidates in new thread!")

    results = []
    for solution in paranthesized_options:
        try:
            replaced_pow_solution = solution.replace('^', '**')
            nsp_eval = evaluate(replaced_pow_solution)
            if nsp_eval == result:
                results.append(replaced_pow_solution)
        except:
            pass
    results = nsp.remove_all_redundant_brackets_and_duplicates(results)
    if (len(results) > 0):
        print("\n".join(results).replace('**', '^'))
    return results
