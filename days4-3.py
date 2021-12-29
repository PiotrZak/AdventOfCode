import sys
with open('data.txt', 'r') as f:
	T = f.readlines()

board_nums = []
total_boards = (len(T) - 2) // 6 + 1
print(total_boards)
for board_num in range(1, total_boards + 1):
	board_nums.append(board_num)

boards = [] # 3d matrix
num_pos = dict() # k: num; v: list of positions
called_states = dict() # k: position; v: if called

def clean_row_str(n_board, row):
	string = T[row]
	str_nums = list(filter(lambda x : x != '', string.split(" ")))
	nums = list(map(int, str_nums))
	board = (n_board - 2) // 6 + 1
	board_row = row - (board - 1) * 6 - 1
	
	for i in range(0, len(nums)):
		num = nums[i]
		pos = str(board * 100 + board_row * 10 + i + 1)
		called_states[pos] = False
		
		if num not in num_pos:
			num_pos[num] = [pos]
		else: 
			num_pos[num].append(pos)
			
	return nums

def update_state(called_num):
	if called_num in num_pos:
		ls_pos = num_pos[called_num]
		for pos in ls_pos:
			called_states[pos] = True
	else:
		return False

def check_board(board):
	for row in range(1, 6):
		verticals = True
		for col in range(1, 6):
			pos = str(board * 100 + row * 10 + col)
			verticals = verticals and called_states[pos]
		if verticals is True:
			return True
			
	for col in range(1, 6):
		horizontals = True
		for row in range(1, 6):
			pos = str(board * 100 + row * 10 + col)
			horizontals = horizontals and called_states[pos]
		if horizontals is True:
			return True
	return False

def init_boards():
	n_board = 2
	while n_board < len(T):
		board = []
		for i in range(0, 5):
			row = n_board + i
			board.append(clean_row_str(n_board, row))
		boards.append(board)
		n_board += 6

def get_score(board, called_num):
	unmarked_sum = 0
	for row in range(1, 6):
		for col in range(1, 6):
			pos = str(board * 100 + row * 10 + col)
			if called_states[pos] is False:
				unmarked_sum += boards[board - 1][row - 1][col - 1]
	return unmarked_sum * called_num

def run_bingo():
	init_boards()
	called = list(map(int, T[0].split(",")))
	for called_num in called:
		update_state(called_num)
		for board_num in board_nums:
			bingo = check_board(board_num)
			if bingo is True and len(board_nums) > 1:
				board_nums.remove(board_num)
			elif bingo is True and len(board_nums) == 1: 
				return(get_score(board_num, called_num))
	return None

print(run_bingo())