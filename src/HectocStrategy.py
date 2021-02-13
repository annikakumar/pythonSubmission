from abc import abstractmethod
import multiprocessing as mp
from src import IterToolsHectoc
import time


class HectocStrategy:
    """
    An abstract strategy providing solving capabilities for a hectoc problem
    """
    def solve_hectoc_puzzle(self, input_numbers: [int], number_threads: int):
        raise NotImplementedError("This is the abstract superclass, use the implemented subclasses instead")

    def split_in_pieces(self, options: [str], number_threads: int):
        """
        Splits array into subarrays for multithreading
        :param options: aray to split
        :param number_threads: number of buckets
        :return: array with splits
        """
        option_array = []
        len_opt = len(options)
        step_size = len_opt // number_threads + 1
        if step_size == 0:
            return options
        for i in range(1, number_threads + 1):
            sub_array = options[(i - 1) * step_size: min(i * step_size, len_opt)]
            option_array.append(sub_array)
        return option_array

    def run_in_parallel(self, candidates, number_threads):
        processes = []
        options_split = self.split_in_pieces(candidates, number_threads)
        ctx = mp.get_context('spawn')
        for candidate in options_split:
            p = ctx.Process(target=IterToolsHectoc.solve, args=(candidate,))
            processes.append(p)
            p.start()
        for process in processes:
            process.join()


class BruteForceStrategy(HectocStrategy):
    @abstractmethod
    def solve_hectoc_puzzle(self, input_numbers: [int], number_threads: int):

        allPermutations = self.find_permutations(input_numbers)

        candidates = self.find_candidates(allPermutations)

        self.run_in_parallel(candidates, number_threads)

    def find_candidates(self, allPermutations):
        cand_start = time.time()
        candidates = IterToolsHectoc.find_all_paranthesized_options(allPermutations)
        cand_end = time.time()
        print("Finding all paranthesis in: " + str(cand_end - cand_start) + " seconds")
        print("Resulting: " + str(len(candidates)) + " solution candidates")
        return candidates

    def find_permutations(self, input_numbers):
        per_start = time.time()
        allPermutations = IterToolsHectoc.get_all_concatenated_combinations_with_operators(input_numbers, ['+', '-', '*', '/', '^'])
        per_end = time.time()
        print(
            "Finding " + str(len(allPermutations)) + " operator and number combinations in: " + str(per_end - per_start) + " seconds")
        return allPermutations


class CloseToHundredStrategy(HectocStrategy):
    @abstractmethod
    def solve_hectoc_puzzle(self, input_numbers: [int], number_threads: int):
        raise NotImplementedError("Not yet implemented")


class WorkWithFourStrategy(HectocStrategy):
    @abstractmethod
    def solve_hectoc_puzzle(self, input_numbers: [int], number_threads: int):
        raise NotImplementedError("Not yet implemented")


class WorkWithFiveStrategy(HectocStrategy):
    @abstractmethod
    def solve_hectoc_puzzle(self, input_numbers: [int], number_threads: int):
        raise NotImplementedError("Not yet implemented")


class WorkWithTenStrategy(HectocStrategy):
    @abstractmethod
    def solve_hectoc_puzzle(self, input_numbers: [int], number_threads: int):
        raise NotImplementedError("Not yet implemented")
