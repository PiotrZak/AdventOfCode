
# code = ''
# lines = []
# first_letter = []
# second_letter = []

# with open('data14.txt') as f:
#     line = f.readline()
#     code = line;
#     for i in f.readlines():
#         fragmented = i.strip('\n').split('->')
#         if len(fragmented) > 1:
#             first_letter.append(fragmented[0])
#             second_letter.append(fragmented[1])
        
# pairs = []
    
# for i, char in enumerate(code):
#     if len(code) > i+1:
#         pairs.append((char, code[i+1])) 

# print(pairs)




with open('data14.txt') as f:
    phraseString = f.readline().strip('\n')
    line = f.readline()   
    line = f.readline()
    data = dict()
    while line:
        conversion = line.strip('\n').split('->') 
        data[conversion[0].strip(' ')] = conversion[1].strip(' ')
        line = f.readline()
    phrase = dict.fromkeys(data, 0)
    for index in range(len(phraseString)-1):
        phrase[phraseString[index:index+2]] += 1


for generation in range(40):
    newPhrase = dict.fromkeys(data, 0)
    for key in phrase:
        newPhrase[key[0] + data[key]] += phrase[key]
        newPhrase[data[key] + key[1]] += phrase[key]
    phrase = newPhrase

elements = dict.fromkeys(data.values(), 0)
for key in phrase:
    elements[key[0]] += phrase[key]
    elements[key[1]] += phrase[key]

for key in elements:
    if(elements[key] % 2 == 1):
        elements[key] = (elements[key] // 2) + 1
    else:
        elements[key] = (elements[key] // 2)

maximum = elements[max(elements, key=elements.get)]
minimum = elements[min(elements, key=elements.get)]

print(maximum - minimum)

# for generations in range(40):
#     next = phrase[0]
#     for i in range(len(phrase) - 1):
#         start = phrase[i:i+2]
#         next += data[start]
#         next += start[1]
#     phrase = next

# elements = dict.fromkeys(set([x for x in phrase]), 0)

# for character in phrase:
#     elements[character] += 1

