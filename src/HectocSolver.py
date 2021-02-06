from src.HectocStrategy import HectocStrategy


class HectocSolver:
    def __init__(self, hectocStrategy: HectocStrategy):
        self.strategy = hectocStrategy

    def solve_hectoc_puzzle(self, input_numbers: int):
        self.strategy.solve_hectoc_puzzle(input_numbers)
