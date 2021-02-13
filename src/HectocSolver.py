import time
from src import HectocProgram
from src.HectocStrategy import HectocStrategy


class HectocSolver:
    """
    Solver for a hectoc problem given a solving strategy
    """

    def __init__(self, hectocStrategy: HectocStrategy):
        self.strategy = hectocStrategy

    def solve_hectoc_puzzle(self, input_numbers: [int], number_threads: int) -> None:
        start_time = time.time()
        self.strategy.solve_hectoc_puzzle(input_numbers, number_threads)
        end = time.time()
        print(HectocProgram.bcolors.UNDERLINE + HectocProgram.bcolors.OKCYAN + "Elapsed time in seconds: " + str(
            end - start_time) + HectocProgram.bcolors.ENDC)
        return
