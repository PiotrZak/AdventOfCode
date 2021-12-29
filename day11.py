with open('day11.txt') as f:
    input = []
    for line in f.read().splitlines():
        input.append([int(x) for x in line])    

steps = 100


def adjacent(x, y):
    for x_d in (-1, 0, 1):
        for y_d in (-1, 0, 1):
            if x_d == y_d == 0:
                continue
            yield x  + x_d, y + y_d

def create_board(data, width, height):
    
    coords = {}
    for i in range(0, width):
        for j in range(0,height):
            coords[(i, j)] = data[i][j]

    step = 0
    while True:
        step += 1
        todo = []

        for k, v in coords.items():
            coords[k] += 1
            if coords[k] > 9:
                todo.append(k)

        while todo:
            pt = todo.pop()
            if coords[pt] == 0:
                continue
            coords[pt] = 0

            for other in adjacent(*pt):
                if other in coords and coords[other] != 0:
                    coords[other] +=1
                    if coords[other] > 9:
                        todo.append(other)

        if all(val == 0 for val in coords.values()):
            break

    print (step)

create_board(input, len(input[0]), len(input))



