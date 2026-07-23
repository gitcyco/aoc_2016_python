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
DAY = 2

SAMPLE_INPUT = """ULL
RRDDD
LURDL
UUUUD"""

REAL_INPUT = get_puzzle_input(YEAR, DAY)


def main():
    # part_1()
    part_2()
    
    

    
def part_1():
    keypad = [[1,2,3], [4,5,6], [7,8,9]];
    cur = [1,1]
    dirs = {'D': [0,1], 'R': [1,0], 'U': [0,-1], 'L': [-1,0]}
    len_x = len(keypad[0])
    len_y = len(keypad)
    
    # puzzle_input = parse_input(SAMPLE_INPUT)
    puzzle_input = parse_input(REAL_INPUT)
    
    print("SAMPLE:", parse_input(SAMPLE_INPUT))
    # print("REAL:", parse_input(REAL_INPUT))
    
    code = ''
    
    for row in puzzle_input:
        for item in row:
            dir_x, dir_y = dirs[item]
            cur = [sum(x) for x in zip(dirs[item], cur)]
            cur[0] = 0 if cur[0] < 0 else cur[0]
            cur[1] = 0 if cur[1] < 0 else cur[1]
            cur[0] = len_x - 1 if cur[0] > len_x - 1 else cur[0]
            cur[1] = len_y - 1 if cur[1] > len_y - 1 else cur[1]
        code += str(keypad[cur[1]][cur[0]])
            
    print("CODE:", code)
    
    keypad = """  1  
 234 
56789
 ABC 
  D  """
    test = parse_input(keypad)
    print("TEST:", test)
    
def part_2():
    keypad_input = """  1  
 234 
56789
 ABC 
  D  """
    keypad = parse_input(keypad_input)
    cur = [0,2]
    dirs = {'D': [0,1], 'R': [1,0], 'U': [0,-1], 'L': [-1,0]}
    len_x = len(keypad[2])
    len_y = len(keypad)
    print("KEYPAD:", keypad)
    print("LENS:", len_x, len_y)
    # puzzle_input = parse_input(SAMPLE_INPUT)
    puzzle_input = parse_input(REAL_INPUT)
    
    print("SAMPLE:", parse_input(SAMPLE_INPUT))
    # print("REAL:", parse_input(REAL_INPUT))
    
    code = ''
    
    for row in puzzle_input:
        for item in row:
            dir_x, dir_y = dirs[item]
            new_x, new_y = [sum(x) for x in zip(dirs[item], cur)]
            if new_x >= 0 and new_x < len_x and new_y >= 0 and new_y < len_y and keypad[new_y][new_x] != ' ':
                cur[0] = new_x
                cur[1] = new_y
        code += str(keypad[cur[1]][cur[0]])
    print("CODE:", code)
    
if __name__ == "__main__":
    main()
    