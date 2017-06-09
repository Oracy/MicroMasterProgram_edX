import random, time # random used for board initialization, time used for sleep

def printBoard(board): # a simple formatting change for console viewing
	print("") # blank line for readability
	for row in board:
		line = ""
		for cell in row:
			char = "o" if cell == 1 else "."
			line += char + " "
		print(line)

def neighbors(board, x, y):
	yBound = len(board) # number of rows
	xBound = len(board[0]) # number of columns
	if x > xBound or y > yBound or x < 0 or y < 0: # catches bad (OOB) input
		return 0
	result = 0
	# Here is a table showing how we reference the neighbor cells, given a cell [y][x].
	#
	#   1st col  2nd col  3rd col
	# +---------+-------+---------+
	# | x-1,y-1 | x,y-1 | x+1,y-1 | First Row
	# +---------+-------+---------+
	# | x-1,y   | x,y   | x+1,y   | Second Row
	# +---------+-------+---------+
	# | x-1,y+1 | x,y+1 | x+1,y+1 | Third Row
	# +---------+-------+---------+
	if (y - 1 >= 0): # first row
		if (x - 1 >= 0): result += board[y - 1][x - 1] # first column
		result += board[y - 1][x] # second column
		if (x + 1 < xBound): result += board[y - 1][x + 1] # third column
	if (x - 1 >= 0): result += board[y][x - 1] # second row
	if (x + 1 < xBound): result += board[y][x + 1]
	if (y + 1 < yBound): # third row
		if (x - 1 >= 0): result += board[y + 1][x - 1]
		result += board[y + 1][x]
		if (x + 1 < xBound): result += board[y + 1][x + 1]
	return result

def main():
	random.seed() # ensuring we get a new random board each time (default seed is sys time)
	rows = int(input("Number of rows: "))
	columns = int(input("Number of columns: "))
	board = [[random.randint(0,1) for i in range(rows)] for j in range(columns)]
	step = [[0 for i in range(rows)] for j in range(columns)] # intermediary board to prevent conflicts in rule checking
	
	while(True): # for simplicity, the code will run indefinitely
		printBoard(board)
		time.sleep(0.5) # delay between frames
		for y in range(len(board)):
			for x in range(len(board[y])):
				n = neighbors(board, x, y)
				if (n == 3) or (n == 2 and board[y][x] == 1): # using standard rules
					step[y][x] = 1
				else:
					step[y][x] = 0
		board = [[x for x in y] for y in step] # we mimic a deep copy to force assigning ByVal

main()