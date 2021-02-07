import logging
from random import choices, randint
from src.HectocStrategy import *
from src.HectocSolver import HectocSolver

MAX_TRIES_QUESTION = 3
MAX_TRIES = 5
DEFAULT_STRATEGY = "BF"
DEFAULT_THREADS = 1

class HectocSolvingProgram:
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

    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)

    def validate_hectoc_input(self, input_string):
        try:
            input = int(input_string)
        except:
            return
        if (not isinstance(input, int)
                or input < 0
                or len(str(input)) != 6 or "0" in str(input)):
            return
        else:
            return input

    def log_input_error(self):
        print("\nThe input you have entered is not valid. The required format is six digits without empty spaces, "
              "such as for example: 123456")

    def get_valid_user_hectoc_number_input(self, newtry: bool = False, times: int = 1) -> int:
        if (newtry):
            self.log.info("New Try!")
        user_input = input("Enter a six digit number as an input to the hectoc puzzle: ")
        int_input = self.validate_hectoc_input(user_input)
        if int_input is None:
            self.log_input_error()
            if times > MAX_TRIES_QUESTION:
                user_input = input("Should i just pick a random set of numbers for you instead? [y/n] ")
                if (user_input == 'y'):
                    hectoc_input = self.get_random_hectoc_input()
                    print("Method called with: " + str(hectoc_input))
                    return hectoc_input
            if times > MAX_TRIES:
                hectoc_input = self.get_random_hectoc_input()
                print("I have picked a number for you! It is " + str(hectoc_input))
                print("On we go...")
                return hectoc_input
            print("Another Try!\n")
            int_input = self.get_valid_user_hectoc_number_input(True, times + 1)
        return int_input

    def get_random_hectoc_input(self):
        return int(''.join(choices('123456789', k=randint(6, 6))))

    def determine_strategy(self):
        print("Tell me, which strategy you would like to use: Enter BF for brute force, or 4,5,10 respectively for the 4,5 or 10 strategy")
        print("If you enter anything else, the default: BF is used")
        user_input = input("Type the desired strategy or enter for BF:  ")
        if(user_input == "BF" or user_input == "4" or user_input == "5" or user_input == "10"):
            print("great, we use your strategy: " + user_input)
        else:
            print("As you wish, fallback to Brute Force!")
        return DEFAULT_STRATEGY

    def determine_number_of_threads(self):
        print("We can support multiple threads for the solution and be faster!")
        user_input = input("Enter the number of threads you would like to run in parallel or enter for single threading:  ")
        try:
            number_threads = int(user_input)
        except:
            print("This was an invalid input..resuming with 1 thread")
            return 1
        if number_threads > 16:
            print("I dont think you have this many threads... let´s continue with 16, this will be more than sufficient!")
            return 16
        return number_threads

    def solve_hectoc_problem(self, validated_input: int, strategy: str, threads: int):
        solver = HectocSolver(BruteForceStrategy())
        solver.solve_hectoc_puzzle(list(map(int, str(validated_input))), 1)






