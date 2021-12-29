
from collections import defaultdict

# def UpdateStatus(x, y, dx, dy):
#     x += dx
#     y += dy

#     if dx < 0:
#         dx += 1
#     elif dx > 0:
#         dx -= 1

#     dy -= 1

#     return [[x, y], [dx, dy]]


# def HasHitTarget(position, target):
#     return (position[0] >= target[0][0] and position[0] <= target[0][1]) and \
#                (position[1] <= target[1][0] and position[1] >= target[1][1])

# target = []
# with open('day17.txt') as f:
#     for coordinate in f.readline().strip('/n').split(":")[1].split(","):
#         target.append([int(x) for x in coordinate.split('=')[1].split('..')])
#     target[1] = [target[1][1], target[1][0]]

# print(target)

# maxHeight = 0
# for x in range(300):
#     for y in range(300):
#         status = [[0, 0], [x,y]]
#         #A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
#         #A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
#         velocity = status[1].copy
#         height = 0
#         found = False
#         while found == False and status[0][0] <= target[0][1] and status[0][1] >= target[1][1]:
#             # Reference
#             status = UpdateStatus(*status[0], *status[1])
#             height = max(height, status[0][1])
#             if HasHitTarget(status[0], target):
#                 found = True
#         if found == True:
#             print('shooting with velocity', velocity, "made", status[0])
#             maxHeight = max(maxHeight, height)

# print(maxHeight)


# velocity is in 2 axis (x + y)

# part 1:
# - shooting to the target
# each tick 4:
# x += x velocity
# y += y velocity
# x velocity -= 1 (until 0)
# y velocity -= 1

# what is the highest 'y' you can reach and hit?
# (example: (6,9))
# expected 45 


# part2
# expected: 112




# target = []
# with open('day17.txt') as f:
#     for coordinate in f.readline().strip('/n').split(":")[1].split(","):
#         target.append([int(x) for x in coordinate.split('=')[1].split('..')])
#     target[1] = [target[1][1], target[1][0]]


# x1, x2, y1, y2 = target[0][0], target[0][1], target[1][0], target[1][1]

# print(x1, x2, y1, y2)

# count = 0
# max_y = 0
# # abs return absolute (eg. -5 -> 5 and -1232 -> 1232)
# for y in range(y1, abs(y1)):

#     for x in range(1, x2 + 1):
#         print(x)
#         vx, vy = x, y
#         x_p = y_p = 0
#         max_y_path = 0

#         for t in range(2 * abs(y1) + 2):
#             x_p += vx
#             y_p += vy
#             vx = max(vx - 1, 0)
#             vy -= 1

#             max_y_path = max(max_y_path, y_p)

#             if x1 <= x_p <= x2 and y1 <= y_p <= y2:
#                 max_y = max(max_y, max_y_path)
#                 count +=1
#                 break
#             elif x_p > x2 or y_p < y1:
#                 break

# print(max_y)




# data = open("day17.txt").read().strip()
# x_range, y_range = data.split(": ")[1].split(", ")
# x_lower, x_upper = x_range.split("=")[1].split("..")
# x_lower, x_upper = int(x_lower), int(x_upper)
# y_lower, y_upper = y_range.split("=")[1].split("..")
# y_lower, y_upper = int(y_lower), int(y_upper)


# def poi(x_velo, y_velo, area):
#     step = 0
#     x, y = (0, 0)
#     max_y = 0
#     while True:
#         if step > 0:
#             if x_velo > 0:
#                 x_velo -= 1
#             elif x_velo < 0:
#                 x_velo += 1
#             else:
#                 x_velo = 0
#             y_velo -= 1
#         x += x_velo
#         y += y_velo
#         max_y = y if y > max_y else max_y

#         if x < -area or x > x_upper:
#             break
#         if y < y_lower or y > area:
#             break
#         if x_lower <= x <= x_upper and y_lower <= y <= y_upper:
#             return max_y

#         step += 1


# x_velo_min = 0
# pos = 0
# while pos < x_lower:
#     x_velo_min += 1
#     pos += x_velo_min

# velos = defaultdict(int)
# for x_velo in range(x_velo_min, x_upper + 1):
#     for y_velo in range(-7500, 7500):
#         hit = poi(x_velo, y_velo, 7500)
#         if hit != None:
#             velos[(x_velo, y_velo)] = hit

# p1 = max(velos, key=velos.get)
# print(f"Part 1: {velos[p1]} @ {p1}")
# print(f"Part 2: {len(velos)}")



# import math


# def sgn(x):
#     return (x > 0) - (x < 0)


# def simulate(vx, vy, target, steps=200):
#     x = y = 0
#     max_y = 0
#     x0, xn, y0, yn = target
    
#     if (vx >= 0 and xn < x) or (vx <= 0 and x0 > x) or (vy < 0 and y0 > y):
#         return -1
    
#     for step in range(steps):
#         x += vx
#         y += vy
#         max_y = max(y, max_y)
        
#         if x0 <= x <= xn and y0 <= y <= yn:
#             return max_y
        
#         vx -= sgn(vx)
#         vy -= 1
        
#     return -1


# data = open("day17.txt").read().split(": ")[1:][0].split(", ")
# x_range = data[0].split("=")[1].split("..")
# y_range = data[1].split("=")[1].split("..")

# x_range = [int(x) for x in x_range]
# y_range = [int(y) for y in y_range]

# target = (min(x_range), max(x_range), min(y_range), max(y_range))

# min_x_vel = int(math.sqrt(target[0]))
# max_x_vel = target[1] + 1
# min_y_vel = target[2]
# max_y_vel = abs(target[2]) + 1

# max_y = 0
# viable = 0

# for vx in range(min_x_vel, max_x_vel):
#     for vy in range(min_y_vel, max_y_vel):
#         sim = simulate(vx, vy, target)
#         max_y = max(max_y, sim)
#         viable += sim >= 0
        
# print("max y", max_y)
# print("number of viable initial velocities", viable)

#from d17data import *
#the data is so small so...
sample = '''target area: x=20..30, y=-10..-5'''

my = '''target area: x=150..193, y=-136..-86'''

def parse_data(data):
    #target area: x=241..273, y=-97..-63
    coords = { "x": [], "y": []}
    data = data.split()
    for line in (line for line in data if "=" in line):
        for coord in (coord for coord in line.strip(",")[2:].split('..')):
            coords[line[0]].append(int(coord))
    
    return coords

def launch_probe(velocity,target):
    p_x,p_y = [0,0]
    v_x,v_y = velocity
    t_x = sorted(target["x"])
    t_y = sorted(target["y"])
    max_y = p_y
    while (p_x < max(t_x)+1 and not (v_x == 0 and p_x < min(t_x))) and not (p_x > min(t_x) and p_y < min(t_y)):
        p_x += v_x
        p_y += v_y
        if v_x > 0:
            v_x -= 1
        elif v_x < 0:
            v_x += 1
        v_y -= 1
        if p_y > max_y:
            max_y = p_y
        if (p_x in range(min(t_x),max(t_x)+1)) and (p_y in range(min(t_y),max(t_y)+1)):
            
            return True,velocity,max_y
    
    return False,velocity,max_y

def main():
    target = parse_data(my)
    print(target)
    max_y = 0
    optimal = []
    count = 0

    print(range(1,max(target["x"])*2))
    print(min(target["y"]))
    print(max(target["x"]))


    for x in range(1,max(target["x"])*2):
        for y in range(min(target["y"]),max(target["x"])):
            r,velocity,this_max_y = launch_probe([x,y],target)
            if r == True:
                count += 1
                if this_max_y > max_y:
                    max_y = this_max_y
                    optimal = velocity
    
    print(optimal)
    print(max_y)
    print(count)
    
        
if __name__ == "__main__":
    main()