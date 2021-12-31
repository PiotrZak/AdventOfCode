# from copy import deepcopy
# from typing import List, Optional
 
 
# class CucumberMap:
#     def __init__(self, initial_map: List[List[str]]) -> None:
#         self.map = initial_map
 
#     def move_cucumbers(self) -> bool:
#         moved = False
 
#         # move east
#         new_map: List = deepcopy(self.map)
#         for row_num in range(len(self.map)):
#             for col_num in range(len(self.map[row_num])):
#                 next_i = col_num + 1 if col_num + 1 < len(self.map[row_num]) else 0
#                 if self.map[row_num][col_num] == '>' and not self.map[row_num][next_i]:
#                     new_map[row_num][next_i] = '>'
#                     new_map[row_num][col_num] = None
#                     moved = True
#         self.map = new_map
 
#         # move south
#         new_map = deepcopy(self.map)
#         for row_num in range(len(self.map)):
#             next_row_num = row_num + 1 if row_num + 1 < len(self.map) else 0
#             for col_num in range(len(self.map[row_num])):
#                 if self.map[row_num][col_num] == 'v' and not self.map[next_row_num][col_num]:
#                     new_map[row_num][col_num] = None
#                     new_map[next_row_num][col_num] = 'v'
#                     moved = True
#         self.map = new_map
 
#         return moved
 
#     def dump(self) -> str:
#         return '\n'.join([''.join([c if c else '.' for c in r]) for r in self.map]) + '\n'
 
 
# def load_data(infile_path: str) -> List[List[Optional[str]]]:
#     data = []
#     with open(infile_path, 'r', encoding='ascii') as infile:
#         [data.append([p if p != '.' else None for p in line.strip()]) for line in infile]
#     return data
 
 
# def part_1() -> int:
#     cm = CucumberMap(load_data('day25.txt'))
#     i = 1
#     while cm.move_cucumbers():
#         i += 1
#     return i
 
 
# if __name__ == '__main__':
#     part1_answer = part_1()
#     print(f'Part 1: {part1_answer}')
 

import time


def part1_string(input_list):
    def move(matrix, sym):
        for i, l in enumerate(matrix):
            ll = l[0]
            l = (l + l[0]).replace(f'{sym}.', f'.{sym}')
            matrix[i] = ''.join(l[-1] + l[1:-1]) if l[-1] != ll else ''.join(l[:-1])
        return matrix

    matrix = input_list
    step = 0
    while 1:
        step += 1
        right_next = [''.join(line) for line in zip(*move(matrix, '>'))]
        down_new = [''.join(line) for line in zip(*move(right_next, 'v'))]
        if matrix == down_new:
            return step + 3
        matrix = down_new


with open("day25.txt", "r", encoding='UTF-8') as file:
    input_list = [str(line.strip()) for line in file]

t0 = time.time()
result = part1_string(input_list)
t1 = time.time()
print(f"{result} in {round(t1-t0, 4)} seconds")