def build_map(map, filler):
    w = len(map[0]) + 2
    new_map = []
    new_map.append([filler] * w)
    for line in map:
        new_map.append([filler] + line + [filler])
    new_map.append([filler] * w)
    return new_map


def get_neighbors(r, c, map, filler):
    bs = ""
    for rm in range(-1, 2):
        for cm in range(-1, 2):
            if r + rm < 0 or r + rm >= len(map) or c + cm < 0 or c + cm >= len(map[0]):
                bs += str(filler)
            else:
                bs += str(map[r + rm][c + cm])
    return 1 if alg[int(bs, 2)] == "#" else 0


data = open("day20.txt").read().strip().split("\n\n")
alg = data.pop(0)
map = [[0 if j == "." else 1 for j in i] for i in data[0].split("\n")]


for i in range(1, 50 + 1):
    # determine state of infinite pixels
    filler = 1 if alg[0] == "#" and alg[-1] == "." and not i % 2 else 0
    map = build_map(map, filler)
    # iterate over map and find updates
    changes = {}
    for r in range(len(map)):
        for c in range(len(map[0])):
            changes[(r, c)] = get_neighbors(r, c, map, filler)
    # apply updates to map
    for r, c in changes:
        map[r][c] = changes[(r, c)]
    if i == 2:
        print(f"Part 1: {sum([val for sublist in map for val in sublist])}")
print(f"Part 2: {sum([val for sublist in map for val in sublist])}")



# import numpy as np
# from numpy.lib.stride_tricks import as_strided
# from typing import Callable
# from pyterator import iterate


# PADDING_SIZE = 2
# WINDOW_SIZE = (3,3)
# DTYPE = np.uint16
# WINDOW = np.array([[256,128,64],[32,16,8],[4,2,1]], dtype=DTYPE)


# def get_algorithm(f) -> list:
#     raw_algorithm = next(f).strip()
#     return [i for i, ch in enumerate(raw_algorithm) if ch=='#']

# def get_padding_value(algorithm: list) -> Callable:
#     if 0b111111111 not in algorithm and 0b000000000 in algorithm:
#         return lambda i: i%2  # They alternate 😱
#     else:
#         return lambda _: 0

# def enhance(X: np.ndarray, algorithm: list, pad_value: int) -> np.ndarray:
#     """Enhances a non-padded 2D array"""

#     X = np.pad(X, (PADDING_SIZE,), constant_values=pad_value).astype(DTYPE)
#     h, w = X.shape
    
#     # Define output fields
#     shape = (h-2, w-2) + WINDOW_SIZE
#     strides = tuple(stride*X.itemsize for stride in [h, 1, h, 1])
    
#     # 2D convolution
#     fields = as_strided(X, shape=shape, strides=strides)
#     binaries = np.tensordot(fields, WINDOW)
    
#     # Convert to light and dark pixels
#     return np.isin(binaries, algorithm) * 1

# def get_initial_img(f) -> list:
#     f.seek(0)
#     return (
#         iterate(f).skip(2).filter_map(str.strip)
#         .map(lambda line: [1 if x=='#' else 0 for x in line])
#         .to_list()
#     )

# if __name__ == '__main__':
#     f = open("day19.txt", "r")

#     algorithm = get_algorithm(f)
#     padding_value = get_padding_value(algorithm)

#     img = get_initial_img(f)
#     for i in range(50):
#         img = enhance(img, algorithm, padding_value(i))

#     print(img.sum())
#     f.close()


# import sys

# file = open('day20.txt')

# algo_string = next(file).strip()
# if algo_string[0] == ".":
#     algo = [
#       {i for i, p in enumerate(algo_string) if p == "#"},
#     ]
# elif algo_string[-1] == ".":
#     algo = [
#         {i for i, p in enumerate(algo_string) if p == "."},
#         {i^511 for i, p in enumerate(algo_string) if p == "#"},
#     ]
# else:
#     print("Infinity")
#     sys.exit()

# image = {(x, y) for y, line in enumerate("".join(file).strip().split("\n")) for x, p in enumerate(line) if p == "#"}


# for i in range(50):
#     (x1, x2), (y1, y2) = ((min(d), max(d)) for d in zip(*image))
#     image = {(x, y) for x in range(x1-1, x2+2) for y in range(y1-1, y2+2) if sum(1<<(8-z) for z in range(9) if (x-1+z%3, y-1+z//3) in image) in algo[i%len(algo)]}

# (x1, x2), (y1, y2) = ((min(d), max(d)) for d in zip(*image))
# for y in range(y1, y2+1):
#     print("".join(("#" if (x, y) in image else ".") for x in range(x1, x2+1)))

# print(len(image))