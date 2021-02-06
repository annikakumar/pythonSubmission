from abc import abstractmethod


class HectocStrategy:
    def solve_hectoc_puzzle(self, input_numbers: int):
        raise NotImplementedError("This is the abstract superclass, use the implemented subclasses instead");


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
