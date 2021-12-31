# # -is a wall
# # . is a open space
# Amber (A),
# Bronze (B),
# Copper (C),
# Desert (D)

# rules:

#rules for a legal move:

# Does not pass through any other amphipod
# Does not move from corridor to corridor
# Does not move from room to room
# Only move to room if that room is final destination
# Only move to bottom spot available in room
# Only move to room if free from amphipods not belonging there
# Do not exit room if you are in a room you belong in and all amphipods below you belong there as well

 

# What is the least energy required to organize the amphipods?
# import re
# from copy import deepcopy
# from queue import PriorityQueue
# from typing import Any, Dict, List
  
# PART_2_INSERTIONS = {
#     'A': ['D', 'D'],
#     'B': ['C', 'B'],
#     'C': ['B', 'A'],
#     'D': ['A', 'C'],
# }
 

# class Burrow:
#     AMPHIPOD_TYPES = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
#     PATHS = {
#         0: {'A': [0, 1], 'B': [0, 1, 2], 'C': [0, 1, 2, 3], 'D': [0, 1, 2, 3, 4]},
#         1: {'A': [1], 'B': [1, 2], 'C': [1, 2, 3], 'D': [1, 2, 3, 4]},
#         2: {'A': [2], 'B': [2], 'C': [2, 3], 'D': [2, 3, 4]},
#         3: {'A': [3, 2], 'B': [3], 'C': [3], 'D': [3, 4]},
#         4: {'A': [4, 3, 2], 'B': [4, 3], 'C': [4], 'D': [4]},
#         5: {'A': [5, 4, 3, 2], 'B': [5, 4, 3], 'C': [5, 4], 'D': [5]},
#         6: {'A': [6, 5, 4, 3, 2], 'B': [6, 5, 4, 3], 'C': [6, 5, 4], 'D': [6, 5]}
#     }
 
#     def __init__(self, state: Dict = None, cost: int = 0):
#         self.state = deepcopy(state) if state else {}
#         self.cost = cost
#         self.state_hash = self._state_hash
 
#     def __lt__(self, other):
#         return self.cost < other.cost
 
#     def move_cost(cls, hallway_position: int, room_type: str, room_position: int,  amphipod_type: str):
#         distance = 2 * len(cls.PATHS[hallway_position][room_type]) + room_position \
#                          - (1 if hallway_position in (0, 6) else 0)
#         return distance * cls.AMPHIPOD_TYPES[amphipod_type]
 
#     def _state_hash(self):
#         return hash(tuple(tuple(v) for k, v in sorted(self.state.items())))
 
#     def is_a_winner(self):
#         return all(all(b == a for b in self.state[a]) for a in self.AMPHIPOD_TYPES)
        
#     def possible_moves(self) -> List[Any]:
#         next_possible_states = []
#         for hall_pos in range(len(self.state['H'])):
#             amphipod_type = self.state['H'][hall_pos]
#             if amphipod_type and self.room_open(amphipod_type):
#                 if self.path_to_room_clear(hall_pos, amphipod_type):
#                     room_pos = self.next_spot_in_room(amphipod_type)
#                     new_burrow = Burrow(self.state, self.cost)
#                     new_burrow.move('H', hall_pos, amphipod_type, room_pos)
#                     return [new_burrow]
#         for room in self.AMPHIPOD_TYPES:
#             if not self.room_open(room):
#                 amphipod_type = [_ for _ in self.state[room] if _][0]
#                 room_pos = self.state[room].index(amphipod_type)
#                 for hall_pos in self.PATHS:
#                     if not self.state['H'][hall_pos] and self.path_to_room_clear(hall_pos, room):
#                         new_burrow = Burrow(self.state, self.cost)
#                         new_burrow.move(room, room_pos, 'H', hall_pos)
#                         next_possible_states.append(new_burrow)
#         return next_possible_states
 
#     def move(self, from_room: str, from_pos: int, to_room: str, to_pos: int):
#         self.cost += self.move_cost(from_pos, to_room, to_pos, to_room) if from_room == 'H' \
#             else self.move_cost(to_pos, from_room, from_pos, self.state[from_room][from_pos])
#         self.state[to_room][to_pos] = self.state[from_room][from_pos]
#         self.state[from_room][from_pos] = None
#         self.state_hash = self._state_hash
 
#     def room_open(self, room: str) -> bool:
#         return all(_ in (None, room) for _ in self.state[room])
 
#     def next_spot_in_room(self, room: str) -> int:
#         return len(self.state[room]) - 1 - self.state[room][::-1].index(None)
 
#     def path_to_room_clear(self, hallway_start: int, end_room_type: str) -> bool:
#         for position in self.PATHS[hallway_start][end_room_type]:
#             if position != hallway_start and self.state['H'][position]:
#                 return False
#         return True
 
 
# def find_path(burrow: Burrow) -> Burrow:
#     queue = PriorityQueue()
#     visited = set()
#     queue.put(burrow)
 
#     while queue:
#         burrow = queue.get()
#         if burrow.is_a_winner:
#             return burrow
#         elif burrow.state_hash not in visited:
#             for possible_move in burrow.possible_moves:
#                 queue.put(possible_move)
#             visited.add(burrow.state_hash)
 
 
# def load_data(infile_path: str) -> Dict:
#     with open(infile_path, 'r', encoding='ascii') as infile:
#         c = [re.match(r'\W*#+(\w)#(\w)#(\w)#(\w)#+', l).groups() for l in infile.readlines()[2:4]]
#         return {
#             'H': [None] * 7,
#             'A': [c[0][0], c[1][0]],
#             'B': [c[0][1], c[1][1]],
#             'C': [c[0][2], c[1][2]],
#             'D': [c[0][3], c[1][3]],
#         }
 
 
# def part_1(infile_path: str) -> int:
#     start_map = load_data(infile_path)
#     result = find_path(Burrow(start_map))
#     return result.cost
 
 
# def part_2(infile_path: str) -> int:
#     start_map = load_data(infile_path)
#     for c in PART_2_INSERTIONS:
#         start_map[c] = [start_map[c][0]] + PART_2_INSERTIONS[c] + [start_map[c][1]]
#     result = find_path(Burrow(start_map))
#     return result.cost
 
 
# def show_moves(b):
#     for i in range(len(b)):
#         print(f'{i} : {b[i].cost} : {b[i].state}')
 
 
# if __name__ == '__main__':
#     part1_answer = part_1('days23.txt')
#     print(f'Part 1: {part1_answer}')
 
#     part2_answer = part_2('days23.txt')
#     print(f'Part 2: {part2_answer}')
 
# import heapq

# HALL_CELLS = [15, 16, 18, 20, 22, 24, 25]
# STACKS = [
#     [69, 57, 45, 31],
#     [71, 59, 47, 33],
#     [73, 61, 49, 35],
#     [75, 63, 51, 37]
# ]
# HALL_ENTRANCES = [17, 19, 21, 23]
# WEIGHTS = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

# def move_home(map):
#     # Try to move from hallway home for all cells, may need to repeat
#     for stack_i, stack in enumerate(STACKS):
#         empty_space = None
#         stack_ch = 'ABCD'[stack_i]
#         distance_in = 4
#         for cell in stack:
#             if map[cell] == '.':
#                 empty_space = cell
#                 break
#             if map[cell] != stack_ch:
#                 break
#             distance_in -= 1
#         if not empty_space:
#             continue

#         hall_entrance = HALL_ENTRANCES[stack_i]
#         for cell in HALL_CELLS:
#             if all((cell2 == cell and map[cell2] == stack_ch) or (cell2 != cell and map[cell2] == '.')
#                     for cell2 in range(min(cell, hall_entrance), max(cell, hall_entrance) + 1)):
#                 # Move home!
#                 distance = (abs(cell - hall_entrance) + distance_in) * WEIGHTS[stack_ch]
#                 new_map = map[0:cell] + '.' + map[cell + 1:]
#                 new_map = new_map[0:empty_space] + stack_ch + new_map[empty_space + 1:]
#                 return distance, new_map
#     return 0, map


# def transitions(map):
#     res = []

#     stack_tops = []
#     distances_out = []

#     for stack in STACKS:
#         stack_top = None
#         distance_out = 5
#         for cell in stack:
#             if map[cell] == '.':
#                 break
#             stack_top = cell
#             distance_out -= 1
#         stack_tops.append(stack_top)
#         distances_out.append(distance_out)

#     # Each stack top can move to an unblocked hallway
#     for stack_i in range(4):
#         if not stack_tops[stack_i]:
#             continue
#         hall_entrance = HALL_ENTRANCES[stack_i]
#         for cell in HALL_CELLS:
#             if all(map[cell2] == '.'
#                    for cell2 in range(min(cell, hall_entrance), max(cell, hall_entrance) + 1)):
#                 # Possible transition
#                 ch = map[stack_tops[stack_i]]
#                 new_map = map[0:cell] + ch + map[cell + 1:]
#                 new_map = new_map[0:stack_tops[stack_i]] + '.' + new_map[stack_tops[stack_i] + 1:]
#                 distance = (distances_out[stack_i] + abs(cell - hall_entrance)) * WEIGHTS[ch]
#                 # print(new_map)
#                 while (True):
#                     distance2, new_map = move_home(new_map)
#                     distance += distance2
#                     if distance2 == 0:
#                         break
#                 res.append((distance, new_map))
#         #break
#     return res

# def is_win(map):
#     # Only checks the top of the stacks so will fail on some inputs
#     for stack_i, stack in enumerate(STACKS):
#         if map[stack[3]] != 'ABCD'[stack_i]:
#             return False
#     return True

# def main():
#     lines = open('days23.txt').readlines()
#     insert = ['  #D#C#B#A#\n', '  #D#B#A#C#\n']
#     start_map = ''.join(lines[0:3] + insert + lines[3:])
#     visited = set()
#     heap = [(0, start_map)]
#     heapq.heapify(heap)

#     while(heap):
#         total_dist, map = heapq.heappop(heap)
#         if is_win(map):
#             print(f'Part 2 Answer: {total_dist}')
#             break
#         if map in visited:
#             continue
#         visited.add(map)
#         for dist, new_map in transitions(map):
#             heapq.heappush(heap, (total_dist + dist, new_map))

# main()


data = (*((*line,) for line in open("days23.txt")),)
typeCost = {'A':1, 'B':10, 'C':100, 'D':1000}
rooms = {'A': 3, 'B':5, 'C':7, 'D':9}

def extend(state):
  return (*state[:3], (*"  #D#C#B#A#",), (*"  #D#B#A#C#",), *state[3:],)

def roomSize(state):
  return len(state)-3

def field(state, x, y):
  return state[y][x]

def stoppableFields(state):
  return tuple(i for i in range(1, len(state[0]) - 1) if i not in rooms.values())

def isInOwnRoom(state, x, y):
  if not isAmphipod(state, x, y):
    return False
  if x == rooms[field(state, x, y)]:
    return True
  return False

def isInAnyRoom(state, x, y):
  return y > 1

def isRoomComplete(state, x):
  for y in range(2,2+roomSize(state)):
    if not isInOwnRoom(state, x, y):
      return False
  return True

def roomsComplete(state):
  for room in rooms.values():
    if not isRoomComplete(state, room): return False
  return True

def isAmphipod(state, x, y):
  val = field(state, x, y)
  return val if val in rooms.keys() else False

def isEmpty(state, x, y):
  return field(state, x, y) == '.'

def isRoomEmpty(state, x):
  for y in range(2,2+roomSize(state)):
    if not isEmpty(state, x, y):
      return False
  return True

def hasRoomAvailable(state, x, y):
  amphipod = field(state, x, y)
  room = rooms[amphipod]
  if isRoomEmpty(state, room): return True
  for y in range(2,2+roomSize(state)):
    if not isEmpty(state, room, y) and not isInOwnRoom(state, room, y):
      return False
  return True

def isPathEmpty(state, x, targetX):
  while x != targetX:
    if x > targetX:
      x-=1
    if x < targetX:
      x+=1
    if not isEmpty(state, x, 1):
      return False
  return True

def isBlockingRoom(state, x, y):
  for j in range(y+1, 2+roomSize(state)):
    if isAmphipod(state, x, j) and not isInOwnRoom(state, x, j):
      return True
  return False

def isBlockedInRoom(state, x, y):
  if y < 3: return False
  return not isEmpty(state, x, y-1)

def moveinPos(state, room):
  for y in range(1+roomSize(state), 1, -1):
    if isEmpty(state, room, y):
      return y

def canMove(state, x, y):
  return (not isInOwnRoom(state, x, y) or isBlockingRoom(state, x, y)) and not isBlockedInRoom(state, x, y)

def moveCost(state, x, y, i, j):
  return ((y - 1) + abs(x - i)  + (j - 1)) * typeCost[field(state, x,y)]

def move(d, x, y, i, j):
  newData = (*((*(((field(d,a,b),field(d,x,y))[a==i and b==j],field(d,i,j))[a==x and b==y] for a in range(len(d[b]))),) for b in range(len(d))),)
  return (newData, moveCost(d, x, y, i, j))

def checkState(state, cache):
  cached = cache.get(state)
  if cached is not None:
    return cached
  if roomsComplete(state):
    return 0
  costs = []
  for y in range(1, len(state)):
    for x in range(1, len(state[y])):
      amphipod = isAmphipod(state, x, y)
      if not amphipod:
        continue
      if canMove(state, x, y):
        room = rooms[amphipod]
        if hasRoomAvailable(state, x, y) and isPathEmpty(state, x, room):
          newState, newCost = move(state, x, y, room, moveinPos(state, room))
          cost = checkState(newState, cache)
          if cost != -1:
            costs.append(cost + newCost)
        elif isInAnyRoom(state, x, y):
          for i in stoppableFields(state):
            if not isPathEmpty(state, x, i):
              continue
            newState, newCost = move(state, x, y, i, 1)
            cost = checkState(newState, cache)
            if cost != -1:
              costs.append(cost + newCost)
  cache[state] = min(costs) if costs else -1
  return cache[state]

print(checkState(data, {}), checkState(extend(data), {}))
