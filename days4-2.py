file = open("data.txt","r")
strings = file.readlines()

numChoice = [int(i) for i in strings[0].split(',')]
Boards = []

# Part 1 ------------------------------------------------

# class Board:

#     def __init__(self, boardStr):
#         self.board = [['' for i in range(5)] for j in range(5)]
#         for i in range(5):
#                 self.board[i] = [int(STR) for STR in boardStr[i].split()]

#         self.unmarkedBoard = [[True for i in range(5)] for j in range(5)]

#     def markBoard(self, number):
#         for i in range(5):
#             for j in range(5):
#                 if self.board[i][j] == number:
#                     self.unmarkedBoard[i][j] = False
#                     break

#     def checkBoard(self, number):
#         for row in self.unmarkedBoard:
#             if row == [False for i in range(5)]:
#                 return self.getTotal() * number
#         for i in range(5):
#             if [self.unmarkedBoard[j][i] for j in range(5)] == [False for i in range(5)]:
#                 return self.getTotal() * number
#         if [self.unmarkedBoard[i][i] for i in range(5)] == [False for i in range(5)]:
#             return self.getTotal() * number
#         if [self.unmarkedBoard[i][4-i] for i in range(5)] == [False for i in range(5)]:
#             return self.getTotal() * number
#         return -1

#     def getTotal(self):
#         total = 0
#         for i in range(5):
#             for j in range(5):
#                 if self.unmarkedBoard[i][j]:
#                     total += self.board[i][j]

#         return total

# numChoice = [int(i) for i in strings[0].split(',')]
# Boards = []

# for index in range(2, len(strings), 6):

#     stringList = []
#     for i in range(5):
#         stringList.append(strings[index + i][:-1:])
#     Boards.append(Board(stringList))

# currentIndex = 0
# done = False

# while not done:
#     for i in range(len(Boards)):
#         Boards[i].markBoard(numChoice[currentIndex])
#         check = Boards[i].checkBoard(numChoice[currentIndex])
#         if check > 0:
#             print(check)
#             done = True
#             break

#     print(f'Index {currentIndex} done')
#     currentIndex += 1

# End Part 1 ---------------------------------------------



# Part 2 ------------------------------------------------

class Board:

    def __init__(self, boardStr):
        self.board = [['' for i in range(5)] for j in range(5)]
        for i in range(5):
                self.board[i] = [int(STR) for STR in boardStr[i].split()]

        self.unmarkedBoard = [[True for i in range(5)] for j in range(5)]

    def markBoard(self, number):
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == number:
                    self.unmarkedBoard[i][j] = False
                    break

    def checkBoard(self, number):
        for row in self.unmarkedBoard:
            if row == [False for i in range(5)]:
                return self.getTotal() * number
        for i in range(5):
            if [self.unmarkedBoard[j][i] for j in range(5)] == [False for i in range(5)]:
                return self.getTotal() * number
        if [self.unmarkedBoard[i][i] for i in range(5)] == [False for i in range(5)]:
            return self.getTotal() * number
        if [self.unmarkedBoard[i][4-i] for i in range(5)] == [False for i in range(5)]:
            return self.getTotal() * number
        return -1

    def getTotal(self):
        total = 0
        for i in range(5):
            for j in range(5):
                if self.unmarkedBoard[i][j]:
                    total += self.board[i][j]

        return total

numChoice = [int(i) for i in strings[0].split(',')]
Boards = []

for index in range(2, len(strings), 6):

    stringList = []
    for i in range(5):
        stringList.append(strings[index + i][:-1:])
    Boards.append(Board(stringList))

currentIndex = 0
done = False

CHECKS = 5

while len(Boards) > 0:

    for c in range(CHECKS):

        for i in range(len(Boards)-1, -1, -1):

            Boards[i].markBoard(numChoice[currentIndex])
            check = Boards[i].checkBoard(numChoice[currentIndex])

            if check > 0:

                print(check)

                doneBoard = Boards.pop(i)
                i -= 1
                break

    print(f'Index {currentIndex} done')
    currentIndex += 1

# End Part 2 ---------------------------------------------


file.close()
