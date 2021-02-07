from src import IterToolsHectoc
from src.HectocStrategy import HectocStrategy
import time


class HectocSolver:
    def __init__(self, hectocStrategy: HectocStrategy):
        self.strategy = hectocStrategy

    def solve_hectoc_puzzle(self, input_numbers: [int], number_threads: int):
        start = time.time()
        print(start)
        allPermutations = IterToolsHectoc.get_all_concatenated_combinations_with_operators(input_numbers, ['+', '-', '*', '/', '**'])
        print("Finding all permutations in: ")
        time_checkpoint_per = time.time()
        print(time_checkpoint_per - start)
        options = IterToolsHectoc.find_all_paranthesized_options(allPermutations)
        print("Finding all paranthesis in: ")
        time_checkpoint_par = time.time()
        print(time_checkpoint_par - time_checkpoint_per)

        solve = IterToolsHectoc.solve(options, 100)

        end = time.time()
        print(end)
        print("Elapsed time in seconds: " + str(end - start))
        print("Finding all solutions in: ")
        print(end - time_checkpoint_par)
        print(solve)
        return solve




