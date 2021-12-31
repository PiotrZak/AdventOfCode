# with open('day10.txt') as f:
#     input = []
#     for line in f.read().splitlines():
#         input.append([x for x in line])    

# with open('day10.txt') as f:
#     file = [x for x in f.readlines()]

# left ='<{(['
# right = '>})]'
# scores =[25137,1197,3,57]
# total =0
# stack = []

# for line in file:
#     for character in line:
#         if character in left:
#             stack.append(character)
#             print(stack)
#         elif character in right:
#             index = right.find(character)
#             #[-1] last element in sequence
#             if stack[-1] != left[index]:
#                 total += scores[index]
#                 found = True
#                 break
#             else:
#                 del(stack[-1])

# print(total)


nav_sub = open("day10.txt","r").read().splitlines()

symbol_dict = {"]":"[", ")":"(", ">":"<", "}":"{"}
symbol_values = {"]":2, ")":1, ">":4, "}":3}
symbol_list = []
score_list = []
temp_score = 0
incomplete_nav_sub = []

for i in nav_sub:
    for u in i:
        if u in symbol_dict.values():
            symbol_list.append(u)
        elif u in symbol_dict.keys():
            if symbol_list[-1] == symbol_dict.get(u):
                symbol_list = symbol_list[:-1]
            else:
                break
    else:
        incomplete_nav_sub.append(i)
        continue
    
    symbol_list = []
    
for i in incomplete_nav_sub:
    symbol_dict = {"]":"[", ")":"(", ">":"<", "}":"{"}
    for u in i:
        if u in symbol_dict.values():
            symbol_list.append(u)
        elif u in symbol_dict.keys():
            if symbol_list[-1] == symbol_dict.get(u): 
                symbol_list = symbol_list[:-1]
    
    symbol_dict = {"[":"]", "(":")", "<":">", "{":"}"}
    while len(symbol_list) > 0:
        x = symbol_dict.get(symbol_list[-1])
        temp_score = temp_score * 5 + symbol_values.get(x)
        symbol_list = symbol_list[:-1]
        
    score_list.append(temp_score)
    temp_score = 0
    symbol_list = []

score_list.sort()
middle = (len(score_list) - 1)/2
print(score_list[int(middle)])


    