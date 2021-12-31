# Get data from file
with open("day2.txt") as fin: 
    data = [i for i in fin.read().strip().split("\n")]

# Part 1
def part1(): 
    forwardPos = 0 
    depthPos = 0
    for instruction in data:
        command = instruction[:-2]
        moveVar = int(instruction[-1])

        if command == 'forward':
            forwardPos += moveVar
        elif command == 'down':
            depthPos += moveVar
        elif command == 'up':
            depthPos -= moveVar

    return forwardPos * depthPos


# Part 2
def part2(): 
    forwardPos = 0 
    depthPos = 0 
    aimPos = 0

    for instruction in data:
        command = instruction[:-2]
        moveVar = int(instruction[-1])

        if command == 'forward':
            forwardPos += moveVar
            depthPos += aimPos * moveVar
        elif command == 'down':
            aimPos += moveVar
        elif command == 'up':
            aimPos -= moveVar
    
    return forwardPos * depthPos

# Answers
print("Answer to part 1: ", part1()) 
print("Answer to part 2: ", part2())