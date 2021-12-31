from collections import deque

array = []
data = set()
folds = []

with open('data13.txt') as f:
    line = f.readline()
    while line != '\n':
        line = tuple([int(x) for x in line.strip('\n').split(',')])
        data.add(line)
        line = f.readline()
    line = f.readline()
    while line:
        line = line.strip('\n').split(' ')[2].split('=')
        line[1] = int(line[1])
        folds.append(line)
        line = f.readline()

def fold_X(data, value):
    after = set()
    for point in data:
        if point[0] > value:
            p = (value - (point[0] - value), point[1])
            after.add(p)
        else:
            p = (point[0], point[1])
            after.add(p)
    return after

def fold_Y(data, value):
    after = set()
    for point in data:
        if point[1] > value:
            p = (point[0], value - (point[1] - value))
            after.add(p)
        else:
            p = (point[0], point[1])
            after.add(p)
    return after

for fold in folds:
    if fold[0] == 'x':
        data = fold_X(data, fold[1])
    else:
        data = fold_Y(data, fold[1])
    print(len(data))

array = [ [' '] * 120 for i in range(40) ]

for point in data:
        array[point[1]][point[0]] = '#' 

for line in array:
        s = ""
        for c in line:
                s += c
        print(s)



#print(array[0])
#print(array[0][0])

max_x = 1310
max_y = 893

# for item in array:
#     if len(item) > 1:
#         for index, i in enumerate(item):
#             if index % 2 == 0:
#                 if int(i) > max_x:
#                     max_x = int(i)
#             else:
#                 if int(i) > max_y:
#                     max_y = int(i)

# def create_board():
#     for i in range(0, max_x):
#         for j in range(0, max_y):
#             if (i == 0 if i > 0 else i, j) in array[0]:
#                 print('#', end='')
#             else:
#                 print('.', end='')  
# create_board()




#print(coords)