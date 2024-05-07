def print_board(board):
	for row in board:
		print(" | ".join(row))
		print("-" * 5)

def check_winner(board):
	for row in board:
		if row.count(row[0]) == len(row) and row[0] != " ":
			return True

	for col in range(len(board[0])):
		if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
			return True

	if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
		return True

	if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
		return True

	return False

def is_board_full(board):
	for row in board:
		if " " in row:
			return False
	return True

def tic_tac_toe():
	board = [[" "]*3 for _ in range(3)]
	player = "X"
	while not (check_winner(board) or is_board_full(board)):
		print_board(board)
		try:
			row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
			col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
		except ValueError:
			print("Please enter valid integers for row and column.")
			continue

		if row not in range(3) or col not in range(3):
			print("Please enter row and column indices within the range 0-2.")
			continue

		if board[row][col] == " ":
			board[row][col] = player
			if player == "X":
				player = "O"
			else:
				player = "X"
		else:
			print("The spot at row {}, column {} is already taken! Try again.".format(row, col))

	print_board(board)
	if check_winner(board):
		print("Player " + player + " wins!")
	else:
		print("It's a tie!")

tic_tac_toe()
