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

SAMPLE_INPUT = """R8, R4, R4, R8"""
REAL_INPUT = get_puzzle_input(YEAR, DAY)


def main():
    part_1()
    part_2()

    
def part_1():
    # puzzle_input = parse_input(SAMPLE_INPUT)
    # puzzle_input = SAMPLE_INPUT
    puzzle_input = REAL_INPUT
    # puzzle_input = parse_input(REAK_INPUT)
    
    print("SAMPLE:", parse_input(SAMPLE_INPUT))
    # print("REAL:", parse_input(REAL_INPUT))
    
    inputs = list(map(lambda x: x.strip(), puzzle_input.split(',')))
    print(inputs)
    start = [0,0]
    cur = [0,0]
    dirs = [[0,1], [1,0], [0,-1], [-1,0]]
    dir_index = 0
    for item in inputs:
        dir, dist = parse_dir(item)
        print(dir, dist)
        dir_index += 1 if dir == 'R' else -1
        dir_index = len(dirs) - 1 if dir_index < 0 else dir_index % len(dirs)
        x, y = dirs[dir_index]
        cur[0] += x * int(dist)
        cur[1] += y * int(dist)
    
    print("CUR:", cur, get_dist(start, cur))
    
def part_2():
    # puzzle_input = parse_input(SAMPLE_INPUT)
    # puzzle_input = SAMPLE_INPUT
    puzzle_input = REAL_INPUT
    # puzzle_input = parse_input(REAK_INPUT)
    
    print("SAMPLE:", parse_input(SAMPLE_INPUT))
    # print("REAL:", parse_input(REAL_INPUT))
    
    inputs = list(map(lambda x: x.strip(), puzzle_input.split(',')))
    print(inputs)
    start = [0,0]
    cur = [0,0]
    dirs = [[0,1], [1,0], [0,-1], [-1,0]]
    dir_index = 0
    visited = {'0,0': True}
    STOP = False
    for item in inputs:
        if STOP:
            break
        dir, dist = parse_dir(item)
        print(dir, dist)
        dir_index += 1 if dir == 'R' else -1
        dir_index = len(dirs) - 1 if dir_index < 0 else dir_index % len(dirs)
        x, y = dirs[dir_index]
        for i in range(int(dist)):
            cur[0] += x
            cur[1] += y
            check = f'{cur[0]},{cur[1]}'
            print("CHECK:", check, cur)
            if check not in visited:
                visited[check] = True
            else:
                print("FOUND!", check, cur)
                STOP = True
                break
    
    print("CUR:", cur, get_dist(start, cur))

def get_dist(coords_a, coords_b):
    # ∣x₁−x₂∣+∣y₁−y₂∣
    return abs(coords_a[0] - coords_b[0]) + abs(coords_a[1] - coords_b[1])
    
        
def parse_dir(input):
    dir = input[0]
    dist = input[1::]
    return [dir, dist]

if __name__ == "__main__":
    main()
    