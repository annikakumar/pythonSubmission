import logging
from random import choices, randint

from src.HectocProgram import HectocSolvingProgram

hectoc_program = HectocSolvingProgram()

print(hectoc_program.banner)
print("\nWelcome to the Hectoc Solver. This hectoc_program can solve the hectoc puzzle with different strategies and present you with the solutions. "
    "The puzzle takes six digits as input and finds solutions reaching 100. \n")

hectoc_int_input = hectoc_program.get_valid_user_hectoc_number_input()
hectoc_int_strategy = hectoc_program.determine_strategy()
threads = hectoc_program.determine_number_of_threads()

print(hectoc_int_input)
print(hectoc_int_strategy)
print(threads)

hectoc_program.solve_hectoc_problem(hectoc_int_input, hectoc_int_strategy, threads)




