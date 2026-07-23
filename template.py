import os
from dotenv import load_dotenv, dotenv_values
from elf import (
    get_puzzle_input,
    submit_puzzle_answer,
    get_private_leaderboard,
    get_user_status,
    OutputFormat,
)
from elf.helpers import parse_input, read_input, timer

load_dotenv()
# print(os.getenv("AOC_SESSION"))

YEAR = 2016
DAY = 1

SAMPLE_INPUT = """R5, L5, R5, R3"""
REAL_INPUT = get_puzzle_input(YEAR, DAY)


def main():
    puzzle_input = parse_input(SAMPLE_INPUT)
    # puzzle_input = parse_input(REAK_INPUT)
    
    print("SAMPLE:", parse_input(SAMPLE_INPUT))
    # print("REAL:", parse_input(REAL_INPUT))
    

if __name__ == "__main__":
    main()
    