def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """
    Simple Tic-Tac-Toe game implementation.

    This function allows two players to play a game of Tic-Tac-Toe on a
    3x3 grid. Players take turns marking spaces on the grid with their
    respective symbols ('X' or 'O'). The game continues until one player
    wins by placing three of their symbols in a row, column, or diagonal,
    or until the grid is filled with no winner.

    Raises:
        ValueError: If the user inputs a non-numeric value for the row or
                    column during their turn, or if the input is not within
                    the valid range (0, 1, or 2).
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                raise ValueError("Invalid input. Please enter a number between 0 and 2.")
            if board[row][col] == " ":
                board[row][col] = player
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError as e:
            print(e)

    print_board(board)
    print("Player " + player + " wins!")

if __name__ == "__main__":
    tic_tac_toe()
