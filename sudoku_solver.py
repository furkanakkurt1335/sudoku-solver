import os, sys

def print_board(board):
	for i in range(len(board)):
		for j in range(len(board[0])):
			print(board[i][j], end=' ')
		print()

def write_board(board, path):
	with open(path, 'a', encoding='utf-8') as f:
		f.write('\n\n')
		for i in range(len(board)):
			for j in range(len(board[0])):
				f.write(str(board[i][j]))
				if j != len(board[0])-1: f.write(' ')
			if i != len(board)-1: f.write('\n')

def board_finished(board):
	for i in range(len(board)):
		if '.' in board[i]:
			return False
	return True

def get_empty(board):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == '.': return i, j
	return -1

def get_col(board, col_index):
	res_col = []
	for i in range(len(board)):
		res_col.append(board[i][col_index])
	return res_col

def valid(board, pos, val, nums):
	size = len(board)
	row, col = pos
	board[row][col] = val
	for i in range(len(board)):
		row = board[i]
		col = get_col(board, i)
		for j in nums:
			if col.count(j) > 1 or row.count(j) > 1: return False
	row_count = 0
	col_count = 0
	for k in range(9):
		l = []
		for i in range(3):
			for j in range(3):
				l.append(board[i+row_count][j+col_count])
		col_count += 3
		if k % 3 == 2:
			row_count += 3
			col_count = 0
		for j in nums:
			if l.count(j) > 1: return False
	return True
		
def solve_board(board, nums):
	if board_finished(board):
		return True
	
	pos = get_empty(board)
	if pos == -1: return True
	row, col = pos
	for i in nums:
		if valid(board, pos, i, nums):
			board[row][col] = i
			if solve_board(board, nums):
				return True
			board[row][col] = '.'
		else: board[row][col] = '.'
	return False

if len(sys.argv) == 1: print('No input paths given'); exit()
input_path = sys.argv[1]
path = os.path.dirname(os.path.realpath(__file__))
size = 9
board = [[-1 for i in range(size)] for j in range(size)]
with open(f'{path}\\{input_path}', 'r', encoding='utf-8') as f:
	input_tokens = f.read().split()
for i in range(size):
	for j in range(size):
		token_t = input_tokens[i*size+j]
		if token_t == '.': board[i][j] = '.'
		else: board[i][j] = int(token_t)
nums = [i for i in range(1, 10)]
solve_board(board, nums)
# print_board(board)
write_board(board, f'{path}\\{input_path}')