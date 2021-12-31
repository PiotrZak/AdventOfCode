import copy
import sys
# def dijkstra(G, start, end ) -> int:
#     """
#     A simple implementation of Dijkstra's shortest path algorithm for finding the
#     shortest path from ``start`` to ``end`` in ``G``.
#     """
#     Q = []
#     D = {}
#     heapq.heappush(Q, (0, start))
#     seen = set()

#     while Q:
#         cost, el = heapq.heappop(Q)
#         if el in seen:
#             continue
#         seen.add(el)
#         for c, x in G[el]:
#             if cost + c < D.get(x, math.inf):
#                 D[x] = cost + c
#                 heapq.heappush(Q, (cost + c, x))

#     return D[end]

#     def grid_adjs(coord, bounds,adjs_type,bounds_type):

#     # Iterate through all of the deltas for the N dimensions of the coord. A delta is
#     # -1, 0, or 1 indicating that the adjacent cell is one lower, same level, or higher
#     # than the given coordinate.

#         for delta in it.product((-1, 0, 1), repeat=len(coord)):
#             if all(d == 0 for d in delta):
#                 # This is the coord itself, skip.
#                 continue

#             if adjs_type == AdjacenciesType.COMPASS:
#                 if sum(map(abs, delta)) > 1:
#                     # For compass adjacencies, we only care when there's only one dimension
#                     # different than the coordinate.
#                     continue

#             if bounds is not None:
#                 in_bounds = True
#                 for i, (d, (low, high)) in enumerate(zip(delta, bounds)):
#                     if bounds_type == BoundsType.RANGE:
#                         in_bounds &=m low <= coord[i] + d < high
#                     elif bounds_type == BoundsType.INCLUSIVE:
#                         in_bounds &= low <= coord[i] + d <= high
#                     elif bounds_type == BoundsType.EXCLUSIVE:
#                         in_bounds &= low < coord[i] + d < high
#                     if not in_bounds:
#                         continue

#                 if not in_bounds:
#                     continue
#             yield tuple(c + d for c, d in zip(coord, delta))



# def part1(lines):
#     G = dict(set)

#     for r, line in enumerate(lines):
#         for c, char in enumerate(line):
#             for r1, c1 in grid_adjs((r, c), ((0, len(lines)), (0, len(lines[0])))):
#                 if (r, c) == (0, 0):
#                     G[(r, c)].add((0, (r1, c1)))
#                 else:
#                     G[(r, c)].add((int(char), (r1, c1)))

#     x = int(lines[-1][-1])
#     if x > 9:
#         x = 1 + (x - 10)

#     G[(len(lines) - 1, len(lines[0]) - 1)].add((x, (2 ** 40, 2 ** 40)))
#     return dijkstra(G, (0, 0), (2 ** 40, 2 ** 40))


# print(part1(data))


# - djiijkstra's algorithm (/ˈdaɪkstrəz/ DYKE-strəz) is an algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks.



data = dict()

# with open('data15.txt') as f:
#     data = [[int(x) for x in line.strip('\n')] for line in f]


# def get_value(data, x, y):
#     if (x < 0) or (y < 0) or (x >= len(data[0])) or (y >= len(data)):
#         return -1
#     return data[x][y]

# allPaths = [[0,[[0,0]], [], [len(data[0])-1, len(data)-1]]]

# bestPaths = [[sys.maxsize] * len(data[0]) for _ in range(len(data))]    

# while len(allPaths) > 0:
#     allPaths.sort(key=lambda x: -x[0])
#     path = allPaths.pop()
#     if path[3] in path[2]:
#         print(path)
#     else:
#         openList = path[1].copy()
#         path[1] = []
#         for next in openList:
#             #Deep copy is a process in which the copying process occurs recursively.
#             newPath = copy.deepcopy(path)
#             newPath[2].append(next)
#             neighbors = [[next[0]-1, next[1]], [next[0]+1, next[1]], [next[0], next[1]-1], [next[0], next[1]+1]]

#             for neighbor in neighbors:
#                 value = get_value(data, *neighbor)
#                 if value >= 0 and neighbor not in newPath[2]:
#                     if newPath[0] + value < bestPaths[neighbor[0]][neighbor[1]]:
#                         bestPaths[neighbor[0]][neighbor[1]] = newPath[0] + value
#                         finalPath = copy.deepcopy(newPath)
#                         finalPath[0] += value
#                         finalPath[1].append(neighbor)
#                         allPaths.append(finalPath)
                        
# print(bestPaths[-1][-1])


with open('data15.txt') as f:
    data = [[int(x) for x in line.strip('\n')] for line in f]

    #horizontally
    for line in data:
        for index in range(4 * len(line)):
            newValue = line[index] + 1
            line.append(newValue if newValue < 10 else 1)
    for index in range(4 * len(data)):
        new = [x+1 for x in data[index]]
        for index in range(len(new)):
            if new[index] > 9:
                new[index] -= 9
        data.append(new)


def get_value(data, x, y):
    if (x < 0) or (y < 0) or (x >= len(data[0])) or (y >= len(data)):
        return -1
    return data[x][y]

end = [len(data[0])-1, len(data)-1]
allPaths = [[0,[[0,0]], [], []]]
bestPaths = [[sys.maxsize] * len(data[0]) for _ in range(len(data))]    

while len(allPaths) > 0:
    allPaths.sort(key=lambda x: -x[0])
    path = allPaths.pop()
    if end == path[1][0]:
        print(path)
    else:
        openList = path[1].copy()
        path[1] = []
        for next in openList:
            #Deep copy is a process in which the copying process occurs recursively.
            newPath = copy.deepcopy(path)
            #newPath[2].append(next)
            neighbors = [[next[0]-1, next[1]], [next[0]+1, next[1]], [next[0], next[1]-1], [next[0], next[1]+1]]

            for neighbor in neighbors:
                value = get_value(data, *neighbor)
                if value >= 0:
                    if newPath[0] + value < bestPaths[neighbor[0]][neighbor[1]]:
                        bestPaths[neighbor[0]][neighbor[1]] = newPath[0] + value
                        finalPath = copy.deepcopy(newPath)
                        finalPath[0] += value
                        finalPath[1].append(neighbor)
                        allPaths.append(finalPath)
                        
print(bestPaths[-1][-1])