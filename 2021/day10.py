# with open('day10.txt') as f:
#     input = []
#     for line in f.read().splitlines():
#         input.append([x for x in line])    

with open('day10.txt') as f:
    file = [x for x in f.readlines()]

left ='<{(['
right = '>})]'
scores =[25137,1197,3,57]
total =0
stack = []

for line in file:
    for character in line:
        if character in left:
            stack.append(character)
            print(stack)
        elif character in right:
            index = right.find(character)
            #[-1] last element in sequence
            if stack[-1] != left[index]:
                total += scores[index]
                found = True
                break
            else:
                del(stack[-1])

print(total)


    