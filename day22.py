from itertools import product
from collections import namedtuple
import re
from time import perf_counter
from typing import Set, Tuple


input_regex = re.compile(r"(?m)(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)")
instructions = []
Instruction = namedtuple("Instruction", "turn start end")
Coordinate = namedtuple("Coordinate", "x y z")

with open("days22.txt") as file:
    for line in file:
        turn, x1, x2, y1, y2, z1, z2 = input_regex.match(line).groups()
        start = Coordinate(int(x1), int(y1), int(z1))
        end   = Coordinate(int(x2), int(y2), int(z2))
        instructions.append(
            Instruction(turn, start, end)
        )

print(instructions)

def xyz_range(start, end, cutoff_start=(-50,-50,-50), cutoff_end=(50, 50, 50)) -> Set[Tuple[int, int]]:

    x1, y1, z1 = start
    x2, y2, z2 = end
    x_min, y_min, z_min = cutoff_start
    x_max, y_max, z_max = cutoff_end

    x1 = max(x_min, x1)
    x2 = min(x_max, x2)
    y1 = max(y_min, y1)
    y2 = min(y_max, y2)
    z1 = max(z_min, z1)
    z2 = min(z_max, z2)

    # All combinations of coordinates within their respective ranges
    cuboid = product(
        range(x1, x2+1),
        range(y1, y2+1),
        range(z1, z2+1),
    )

    # Add the coordinates to a set and return it
    return set(cuboid)

start_time = perf_counter()
cubes_on = set()
for (turn, start, end) in instructions:
    if turn == "on":
        cubes_on |= xyz_range(start, end)
    
    elif turn == "off":
        cubes_on -= xyz_range(start, end)
    
    assert len(cubes_on) <= 1_030_301
total_time = perf_counter() - start_time

# print(f"Part 1: {len(cubes_on)} (took {total_time:.3f} seconds)")

# import re
# import sys
# from math import prod
# from collections import Counter

# def intersects(a, b):
#     return all(a[i] <= b[i + 1] and a[i + 1] >= b[i] for i in range(0, 5, 2))

# def get_intersection_area(a, b):
#     return tuple((min if i & 1 else max)(a[i], b[i]) for i in range(6))

# def get_area(area):
#     return prod(area[i + 1] - area[i] + 1 for i in range(0, 5, 2))

# steps = [
#     (line.split(' ')[0], tuple(map(int, re.findall(r'-?\d+', line))))
#     for line in open('days22.txt', 'r')
# ]

# areas = Counter()

# print(steps)

# for step_type, new_area in steps:
#     updated_areas = Counter()

#     if (step_type == 'on'):
#         updated_areas[new_area] += 1

#     for area, value in areas.items():
#         if (intersects(new_area, area)):
#             intersection_area = get_intersection_area(new_area, area)
#             updated_areas[intersection_area] -= value

#     areas.update(updated_areas)

# print(sum(get_area(area) * value for area, value in areas.items()))