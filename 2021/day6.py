# lines = []

# with open('day6.txt') as f:
#     data = [int(x) for x in f.readline().split(',')]

# for days in range(80):
#     index = 0
#     endDay = len(data)
#     while index < endDay:
#         if data[index] == 0:
#             data[index] = 6
#             data.append(8)
#         else:
#             data[index] -= 1
#         index += 1

# print(len(data))


data = {}

with open('day6.txt') as f:
    array = [int(x) for x in f.readline().split(',')]

    for value in range(max(9, max(array))):
        data[value] = 0
    for element in array:
        data[element] += 1

print(data)

for days in range(256):
    zeroes = data[0]
    data[0] = 0
    for index in range(1, len(data)):
        print(data)
        data[index-1] += data[index]
        data[index] = 0
    data[6] += zeroes
    data[8] += zeroes

solution = 0
for key in data:
    solution += data[key]

print(solution)
