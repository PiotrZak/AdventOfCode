from json import loads
from copy import deepcopy

with open('days18.txt') as f:
    tests = [loads(line.strip('/n')) for line in f.readlines()]

# [1,2] + [[3,4],5] becomes [[1,2],[[3,4],5]].

#explode when
# If any pair is nested inside four pairs, the leftmost such pair explodes.
# If any regular number is 10 or greater, the leftmost such regular number splits.

# part 2

class Node:
    def __init__(self, value, depth=0, parent=None, left=None, right=None):
        self.value = value
        self.depth = depth
        self.parent = parent
        self.left = left
        self.right = right

def MakeTree(test, depth=0, parent=None):
    node = Node(test, depth, parent)
    if isinstance(test[0], list):
        node.left = MakeTree(test[0], depth+1,node)
    if isinstance(test[1], list):
        node.right = MakeTree(test[1], depth+1, node)
    return node

value = None
valueFound = False
nodeStack = []

def InOrderExplosion(node):
    global value
    if node.depth == 4:
        if value == None:
            value = node
    else:
        if node.left != None:
            InOrderExplosion(node.left)
        if node.right != None: 
            InOrderExplosion(node.right)

def ChangeClosestRightNumber(node, whatToAdd):
    global value, valueFound, nodeStack

    if id(node.value) == id(value.value):
        if valueFound == False:
            valueFound = True
            for placement in nodeStack[::-1]:
                if isinstance(placement[0][placement[1]], int):
                    placement[0][placement[1]] += whatToAdd
                    nodeStack = []
                    break     
    else:
        if node.right == None:
            nodeStack.append([node.value, 1])
        else:
            ChangeClosestRightNumber(node.right, whatToAdd)
        if valueFound == False:
            if node.left == None:
                nodeStack.append([node.value, 0])
            else:
                ChangeClosestRightNumber(node.left, whatToAdd)

def ChangeClosestLeftNumber(node, whatToAdd):
    global value, valueFound, nodeStack

    if id(node.value) == id(value.value):
        if valueFound == False:
            valueFound = True
            for placement in nodeStack[::-1]:
                if isinstance(placement[0][placement[1]], int):
                    placement[0][placement[1]] += whatToAdd
                    nodeStack = []
                    break     
    else:
        if node.left == None:
            nodeStack.append([node.value, 0])
        else:
            ChangeClosestLeftNumber(node.left, whatToAdd)
        if valueFound == False:
            if node.right == None:
                nodeStack.append([node.value, 1])
            else:
                ChangeClosestLeftNumber(node.right, whatToAdd)
            

def Explode(root):
    global value, valueFound, nodeStack
    value = None
    InOrderExplosion(root)
    if value == None:
        return False
    nodeStack = []
    valueFound = False
    ChangeClosestLeftNumber(root, value.value[0])
    nodeStack = []
    valueFound = False
    ChangeClosestRightNumber(root, value.value[1])
    parent = value.parent
    if isinstance(parent.value[0], list):
        parent.value[0] = 0
    else:
        parent.value[1] = 0
    return True

def InOrderSplit(node):
    global value
    if isinstance(node.value[0], int):
        if value == None and node.value[0] >= 10:
            value = node
    elif node.left != None:
        InOrderSplit(node.left)
    if isinstance(node.value[1], int):
        if value == None and node.value[1] >= 10:
            value = node
    elif node.right != None:
        InOrderSplit(node.right)

def Split(root):
    global value
    value = None
    InOrderSplit(root)
    if value == None or value.value == None:
        return False
    if isinstance(value.value[0], int) and value.value[0] >= 10:
        half = value.value[0] // 2
        halfsies = [half, half] if value.value[0] % 2 == 0 else [half, half+1]
        value.value[0] = halfsies
    elif isinstance(value.value[1], int) and value.value[1] >= 10:
        half = value.value[1] // 2
        halfsies = [half, half] if value.value[1] % 2 == 0 else [half, half+1]
        value.value[1] = halfsies
    return True

def Add(lhs, rhs):
    return [lhs, rhs]

def Magnitude(snailfish):
    value = 3 * (snailfish[0] if isinstance(snailfish[0], int) else Magnitude(snailfish[0]))
    value += 2 * (snailfish[1] if isinstance(snailfish[1], int) else Magnitude(snailfish[1]))
    return value

# for index in range(1, len(tests)):
#     print('adding with ', result)
#     result = Add(result, tests[index])
#     action = True
#     while action == True:
#         tree = MakeTree(result)
#         action = Explode(tree)
#         if action == False:
#             action = Split(tree)
#     print(result)

maxValue = 0

for a in tests:
    for b in tests:
        if id(a) != id(b):
            result = Add(deepcopy(a), deepcopy(b))
            action = True
            while action == True:
                tree = MakeTree(result)
                action = Explode(tree)
                if action == False:
                    action = Split(tree)
            maxValue = max(maxValue, Magnitude(result))

print(maxValue)