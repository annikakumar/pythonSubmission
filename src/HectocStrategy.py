from abc import abstractmethod

from src import IterToolsHectoc


class HectocStrategy:
    def solve_hectoc_puzzle(self, input_numbers: int):
        raise NotImplementedError("This is the abstract superclass, use the implemented subclasses instead");


class BruteForceStrategy(HectocStrategy):
    def solve_hectoc_puzzle(self, input_numbers: [int]):
        allPermutations = IterToolsHectoc.get_all_concatenated_combinations_with_operators(input_numbers, ['+', '-', '*', '/', '^'])
        print("Number of candidates without parantheses:" + len(allPermutations))

        options = IterToolsHectoc.find_all_paranthesized_options(allPermutations)
        solve = IterToolsHectoc.solve(options, 100)
        print(len(allPermutations))
        return solve


class CloseToHundredStrategy(HectocStrategy):
    @abstractmethod
    def solve_hectoc_puzzle(self, hectoc_input: int):
        raise NotImplementedError("Not yet implemented")


class WorkWithFourStrategy(HectocStrategy):
    @abstractmethod
    def solve_hectoc_puzzle(self, hectoc_input: int):
        raise NotImplementedError("Not yet implemented")


class WorkWithFiveStrategy(HectocStrategy):
    @abstractmethod
    def solve_hectoc_puzzle(self, hectoc_input: int):
        raise NotImplementedError("Not yet implemented")


class WorkWithTenStrategy(HectocStrategy):
    @abstractmethod
    def solve_hectoc_puzzle(self, hectoc_input: int):
        raise NotImplementedError("Not yet implemented")
