"""

"""
import sys 
import os
sys.path.append(os.path.abspath(os.getcwd()))
from utils import get_input, decorator_timer

input_type = 'prod'
day = '5'
year = '2023'
lines = get_input(input_type, day, year)

def parse_input(lines):
    seeds = []
    maps_array = []
    map_values = []
    in_map = False
    for line in lines:
        if line.startswith("seeds:"):
            seeds = line.split(':')[1].strip(' ').split(' ')
            seeds = [int(x) for x in seeds if x != '']
        if "map:" in line:
            in_map = True
            continue
        
        if in_map and line != '':
            parsed_map_value = [int(x) for x in line.split(' ') if x != '']
            map_values.append(parsed_map_value)
        elif in_map and line == '':
            in_map = False
            maps_array.append(map_values)
            map_values = []
    maps_array.append(map_values)
    return seeds, maps_array


def solution_p1_helper(seed, map_array):
    for val in map_array:
        # print(f"{val[1]} <= {seed} <= {val[1] + val[2] - 1} --> {val}, {seed} = {val[0] + (seed - val[1])}")
        if seed <= val[1] + val[2] - 1 and seed >= val[1]:
            # print("--------------------------\n\n")
            return val[0] + (seed - val[1])
    # print("--------------------------\n\n")
    return seed 

# @decorator_timer
def solution_p1(seeds, maps_array):
    min_seed_value = None
    for seed in seeds:
        for map_array in maps_array:
            seed = solution_p1_helper(seed, map_array)
        min_seed_value = seed if min_seed_value is None else min(min_seed_value, seed)
    return min_seed_value

# @decorator_timer
def solution_p2(seeds, maps_array):
    A = []
    for i in range(0, len(seeds), 2):
        A.append((seeds[i], seeds[i]+seeds[i+1]))
    print(A)
    print(maps_array)
    for items in maps_array:
        F = []
        while len(A) != 0:
            start, end = A.pop()
            for ai, bi, ci in items:
                overlap_start = max(start, bi)
                overlap_end = min(end, bi+ci)
                if overlap_start < overlap_end:
                    F.append((overlap_start + ai - bi, overlap_end + ai - bi))
                    if overlap_start > start:
                        A.append((start, overlap_start))
                    if overlap_end < end:
                        A.append((overlap_end, end))
                    break # if this break is trigger exit then following else block won't run
            else:
                F.append((start, end))
        A = F
    return min(A)[0]
                    
seeds, maps_array = parse_input(lines)
# print(seeds, maps_array)
# print(solution_p1(seeds, maps_array))
print(solution_p2(seeds, maps_array))