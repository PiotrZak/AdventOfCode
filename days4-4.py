with open('data.txt', 'r') as f:
    num_data, *board_data = f.read().split('\n\n')
    

def create_boards(num_data, board_data):
    nums = map(int, num_data.split(','))
    boards = []
    for board in board_data:
        rows = [[int(i) for i in row.split()] for row in board.split('\n')]
        boards.append([set(row) for row in rows])
        boards.append([set(col) for col in zip(*rows)])
    return nums, boards

def get_winning_score(num, board):
    return (sum(sum(group) for group in board) - num) * num

def AOC_day4_pt1():
    nums, boards = create_boards(num_data, board_data)
    print(boards)
    for num in nums:
        print(num)
        for idx, board in enumerate(boards):
            if {num} in board:
                print('num')
                print ({num})
                print('board')
                print(board)
                return get_winning_score(num, board)
            else:
                boards[idx] = [group.difference({num}) for group in board]

def AOC_day4_pt2():
    nums, boards = create_boards(num_data, board_data)
    for num in nums:
        for idx, board in enumerate(boards):
            if board is not None:
                if {num} in board:
                    winner = get_winning_score(num, board)
                    boards[idx] = None
                    if idx%2:
                        boards[idx-1] = None
                    else:
                        boards[idx+1] = None
                else:
                    boards[idx] = [group.difference({num}) for group in board]
    return winner

print(AOC_day4_pt1())
#print(AOC_day4_pt2())