from random import choices, randint
from typing import Optional

from src.HectocSolver import HectocSolver
from src.HectocStrategy import *

MAX_TRIES_QUESTION = 3
MAX_TRIES = 5
DEFAULT_THREADS = 1
DEFAULT_STRATEGY = "BF"


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class HectocSolvingProgram:
    """
    The Program taking care of user input handling for a hectoc problem solver
    """

    def run(self) -> None:
        """
        Entry point for hectoc program
        """
        print(bcolors.BOLD +
              "\nWelcome to the Hectoc Solver. This hectoc_program can solve the hectoc puzzle with different strategies and present you with the solutions. "
              "The puzzle takes six digits as input and finds solutions reaching 100. \n" + bcolors.ENDC)

        hectoc_int_input = self.get_valid_user_hectoc_number_input()
        hectoc_int_strategy = self.determine_strategy_notimplemented()
        threads = self.determine_number_of_threads()

        self.solve_hectoc_problem(hectoc_int_input, hectoc_int_strategy, threads)

    def validate_hectoc_input(self, input_string) -> Optional[int]:
        """
        validates an input string considering requirements for hectoc input

        :param input_string: the input string
        :return: the integer parsed input or none if input not valid
        """
        try:
            input = int(input_string)
        except:
            return
        if (not isinstance(input, int)
                or input < 0
                or len(str(input)) != 6 or "0" in str(input)):
            return
        return input

    def log_input_error(self):
        print(
            bcolors.WARNING + "\nThe input you have entered is not valid. The required format is six digits from 1-9 without empty spaces, "
                              "such as for example: 123456" + bcolors.ENDC)

    def get_valid_user_hectoc_number_input(self, times: int = 1) -> int:
        """
        Extracts and evaluates user input for the hectoc problem
        :param times:
        :return:
        """
        if (times > 1):
            print("New Try!\n")
        user_input = input("Enter a six digit number as an input to the hectoc puzzle: ")
        int_input = self.validate_hectoc_input(user_input)
        if int_input is None:
            return self.handle_repeated_input_error(times)
        return int_input

    def handle_repeated_input_error(self, times):
        self.log_input_error()
        if MAX_TRIES_QUESTION < times < MAX_TRIES:
            user_input = input(bcolors.WARNING + "Should i just pick a random set of numbers for you instead? [y/n] " + bcolors.ENDC)
            if (user_input == 'y'):
                hectoc_input = self.get_random_hectoc_input()
                print(bcolors.OKGREEN + "Method called with: " + str(hectoc_input) + bcolors.ENDC)
                return hectoc_input
        if times > MAX_TRIES:
            hectoc_input = self.get_random_hectoc_input()
            print(bcolors.FAIL + "I have picked a number for you! It is " + str(hectoc_input) + bcolors.ENDC)
            print("On we go...")
            return hectoc_input
        return self.get_valid_user_hectoc_number_input(times + 1)

    def get_random_hectoc_input(self):
        return int(''.join(choices('123456789', k=randint(6, 6))))

    def determine_strategy(self):
        print("Tell me, which strategy you would like to use: Enter BF for brute force, or 4,5,10 respectively for the 4,5 or 10 strategy")
        print("If you enter anything else, the default: BF is used")
        user_input = input("Type the desired strategy or enter for BF:  ")
        if (user_input == "BF" or user_input == "4" or user_input == "5" or user_input == "10"):
            print("great, we use your strategy: " + user_input)
        else:
            print("As you wish, fallback to Brute Force!")
        return DEFAULT_STRATEGY

    def determine_number_of_threads(self):
        print("We can support multiple threads for the solution and be faster!")
        user_input = input("Enter the number of threads you would like to run in parallel or enter for single threading:  ")
        try:
            number_threads = int(user_input)
            if (number_threads < 0):
                print(bcolors.WARNING + "This was an invalid input..resuming with 1 thread" + bcolors.ENDC)
                return 1
        except:
            print(bcolors.WARNING + "This was an invalid input..resuming with 1 thread" + bcolors.ENDC)
            return 1
        if number_threads > 8:
            print(
                bcolors.WARNING + "I dont think we will need that many threads... let´s continue with 8, this will be more than sufficient!" + bcolors.ENDC)
            return 8
        return number_threads

    def solve_hectoc_problem(self, validated_input: int, strategy: str, threads: int):
        print(bcolors.OKGREEN + "The calcuation is started with the following parameters: \n Input:" + str(validated_input) +
              "\n strategy: " + str(strategy) +
              "\n Number of threads: " + str(threads) + bcolors.ENDC)

        solver = HectocSolver(strategy)
        solver.solve_hectoc_puzzle(list(map(int, str(validated_input))), threads)

        self.want_to_play_another_round()

    def determine_strategy_notimplemented(self) -> HectocStrategy:
        print("There is only one strategy implemented which is brute force... let´s hope it is fast enough...")
        return BruteForceStrategy()

    def want_to_play_another_round(self):
        user_input = input(bcolors.OKBLUE + "Want to play another round? [y/n]" + bcolors.ENDC)
        if (user_input == "y" or user_input == "Y"):
            print(bcolors.OKBLUE + "Great! Let´s get to it" + bcolors.ENDC)
            self.run()
        else:
            print(bcolors.OKBLUE + "Yea I thought so... all good things come to an end. Have a good day anyway!" + bcolors.ENDC)

    banner = "" \
             " .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.\n" \
             "| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |\n" \
             "| |  ____  ____  | || |  _________   | || |     ______   | || |  _________   | || |     ____     | || |     ______   | |\n" \
             "| | |_   ||   _| | || | |_   ___  |  | || |   .' ___  |  | || | |  _   _  |  | || |   .'    `.   | || |   .' ___  |  | |\n" \
             "| |   | |__| |   | || |   | |_  \_|  | || |  / .'   \_|  | || | |_/ | | \_|  | || |  /  .--.  \  | || |  / .'   \_|  | |\n" \
             "| |   |  __  |   | || |   |  _|  _   | || |  | |         | || |     | |      | || |  | |    | |  | || |  | |         | |\n" \
             "| |  _| |  | |_  | || |  _| |___/ |  | || |  \ `.___.'\  | || |    _| |_     | || |  \  `--'  /  | || |  \ `.___.'\  | |\n" \
             "| | |____||____| | || | |_________|  | || |   `._____.'  | || |   |_____|    | || |   `.____.'   | || |   `._____.'  | |\n" \
             "| |              | || |              | || |              | || |              | || |              | || |              | |\n" \
             "| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |\n" \
             " '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'\n"