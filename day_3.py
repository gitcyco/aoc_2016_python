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
import re

load_dotenv()
# print(os.getenv("AOC_SESSION"))

YEAR = 2016
DAY = 3

SAMPLE_INPUT = """5 10 25"""
REAL_INPUT = get_puzzle_input(YEAR, DAY)


def main():
    # part_1()
    part_2()
    
def part_1():
    # puzzle_input = parse_input(SAMPLE_INPUT)
    puzzle_input = parse_input(REAL_INPUT)
    
    # print("SAMPLE:", parse_input(SAMPLE_INPUT))
    # print("REAL:", parse_input(REAL_INPUT))
    
    count = 0
    
    for row in puzzle_input:
        a, b, c = [int(x) for x in re.split(r'\s+', row.strip())]
        print(a,b,c)
        if check(a, b, c):
            count += 1
    print("COUNT:", count)
    
def part_2():
    SAMPLE_INPUT = """101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603"""
    # puzzle_input = parse_input(SAMPLE_INPUT)
    puzzle_input = parse_input(REAL_INPUT)
    # print(puzzle_input)
    count = 0
    cur = 0
    for cut in range(3, len(puzzle_input) + 1, 3):
        parts = list(map(lambda x: re.split('\s+', x.strip()), puzzle_input[cur:cut]))
        for x in range(0, 3):
            items = []
            for y in range(0,3):
                items.append(int(parts[y][x]))
            a, b, c = items
            if check(a,b,c):
                count += 1
        cur += 3
    print("COUNT:", count)
    
def check(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True


if __name__ == "__main__":
    main()
    