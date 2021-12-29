with open("data.txt") as f:
    drawn = [int(x) for x in f.readline().strip('\n').split(',')]
    cards = []
    while f.readline():
        card = []
        for i in range(5):
            card.extend([int(x) for x in f.readline().strip('\n').split(' ') if x != ''])
        cards.append(card)
    

def isWinner(card):
    #horizontal
    start = 0
    for i in range(5):
        if card[start] + card[start+1] + card[start+2] + card[start+3] + card[start+4] == 500:
            return True
        start += 5
    start = 0
    for i in range(5):
        if card[start] + card[start+5] + card[start+10] + card[start+15] + card[start+20] == 500:
            return True
        start += 1
    return False

found = False
while found == False:
    number = drawn[0]
    drawn = drawn[1:]
    for card in cards:
        for i in range(len(card)):
            if card[i] == number:
                card[i] == 100
    for card in cards:
        if isWinner(card):
            total = sum([x for x in card if x != 100])
            print('Part 1', total * number)
            found = True;


# found = False
# while found == False:
#     number = drawn[0]
#     drawn = drawn[1:]
    
#     for index in range(len(cards)):
#         for i in range(len(cards[index])):
#             if cards[index][i] == number:
#                 cards[index][i] = 100

#         index = 0
#         while index < len(cards):
#             if isWinner(cards[index]):
#                 if len(cards) > 1:
#                     cards.pop(index)
#                 else:
#                     found = True
#                     print(cards[index])
#                     break
#             else:
#                 index += 1

#total = sum([x for x in cards[index] if x != 100])
#print("Part 2 solution:", total * number)


    #vertical