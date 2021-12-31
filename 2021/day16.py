import math
from functools import reduce
import operator

with open('data16.txt') as f:
    data = [[x for x in line.strip('\n')] for line in f]


bits =  []

for i in data[0]:
    if i == '0':
        bits.append('0000')
    elif i == '1':
        bits.append('0001')
    elif i == '2':
        bits.append('0010')
    elif i == '3':
        bits.append('0011')
    elif i == '4': 
        bits.append('0100')
    elif i == '5':
        bits.append('0101')
    elif i == '6':
        bits.append('0110')
    elif i == '7':
        bits.append('0111')
    elif i == '8':
        bits.append('1000')
    elif i == '9':
        bits.append('1001')
    elif i == 'A':
        bits.append('1010')
    elif i == 'B':
        bits.append('1011')
    elif i == 'C':
        bits.append('1100')
    elif i == 'D':
        bits.append('1101')
    elif i == 'E':
        bits.append('1110')
    elif i == 'F':
        bits.append('1111')

print(bits)

def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 

bitsSingle = listToString(bits)
print(bitsSingle)

def package(index):
    packetTypeID = int(bitsSingle[index+3:index+6], 2)
    index += 6
    if packetTypeID == 4:
        literalValue = ""
        group = '1'
        while group[0] == '1':
            group = bitsSingle[index:index+5]
            literalValue += bitsSingle[index+1:index+5]
            index += 5
        return int(literalValue, 2), index
    else:
        total = 0
        numbers = []
        if bitsSingle[index] == '0':
            lengthOfSubpackets = int(bitsSingle[index+1:index+16], 2)
            index += 16
            while total < lengthOfSubpackets:
                value, newIndex = package(index)
                numbers.append(value)
                total += (newIndex - index)
                index = newIndex
        else:
            numberOfSubpackets = int(bitsSingle[index+1:index+12], 2)
            index += 12
            for i in range(numberOfSubpackets):
                value, newIndex = package(index)
                numbers.append(value)
                total += (newIndex - index)
                index = newIndex

        if packetTypeID == 0:
            return sum(numbers), index
        elif packetTypeID == 1:
            return reduce(operator.mul, numbers, 1), index
        elif packetTypeID == 2:
            return min(numbers), index
        elif packetTypeID == 3:
            return max(numbers), index
        elif packetTypeID == 5:
            return (1, index) if numbers[0] > numbers[1] else (0, index)
        elif packetTypeID == 6:
            return (1, index) if numbers[0] < numbers[1] else (0, index)
        elif packetTypeID == 7:
            return (1, index) if numbers[0] == numbers[1] else (0, index)

        return totalPacketVersions, index

# def package(index):

#     start = index
#     packetVersion = int(bitsSingle[index:index+3], 2)
#     packetTypeID = int(bitsSingle[index+3:index+6], 2)
#     index += 6
#     if packetTypeID == 4:
#         literalValue = ""
#         group = '1'
#         while group[0] == '1':
#             group = bitsSingle[index:index+5]
#             literalValue += bitsSingle[index+1:index+5]
#             index += 5
#         return packetVersion, index
#     else:
#         if bitsSingle[index] == '0':
#             lengthOfSubpackets = int(bitsSingle[index+1:index+16], 2)
#             index += 16
#             totalPacketVersions = packetVersion
#             total = 0
#             while total < lengthOfSubpackets:
#                 value, newIndex = package(index)
#                 total += (newIndex - index)
#                 index = newIndex
#                 totalPacketVersions += value
#             return totalPacketVersions, index
#         else:
#             numberOfSubpackets = int(bitsSingle[index+1:index+12], 2)
#             index += 12
#             totalPacketVersions = packetVersion
#             total = 0
#             for i in range(numberOfSubpackets):
#                 value, newIndex = package(index)
#                 total += (newIndex - index)
#                 index = newIndex
#                 totalPacketVersions += value
#         return totalPacketVersions, index

def GetTotalPacketVersions():
    value, index = package(0)
    return value

print(GetTotalPacketVersions())