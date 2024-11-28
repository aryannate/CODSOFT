import math

# Function to display the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check for a winner
def check_winner(board):
    # Rows, columns, and diagonals
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    for combination in winning_combinations:
        if board[combination[0][0]][combination[0][1]] == board[combination[1][0]][combination[1][1]] == board[combination[2][0]][combination[2][1]] and board[combination[0][0]][combination[0][1]] != ' ':
            return board[combination[0][0]][combination[0][1]]
    return None

# Function to check if the board is full (draw)
def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Minimax with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == 'X': return -10 + depth
    if winner == 'O': return 10 - depth
    if is_full(board): return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# AI move
def best_move(board):
    best_value = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_value = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = ' '
                if move_value > best_value:
                    best_value = move_value
                    move = (i, j)
    return move

# Main game loop
def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = input("Choose your marker (X or O): ").upper()
    ai = 'O' if player == 'X' else 'X'
    print("You are", player, "and AI is", ai)
    print_board(board)

    while True:
        # Player's turn
        if player == 'X':
            print("Your turn!")
            row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
            if board[row][col] == ' ':
                board[row][col] = player
            else:
                print("Cell already taken! Try again.")
                continue
        else:
            print("AI's turn!")
            move = best_move(board)
            if move:
                board[move[0]][move[1]] = ai

        print_board(board)

        # Check for winner
        winner = check_winner(board)
        if winner:
            print(winner, "wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # Swap turns
        player, ai = ai, player

# Run the game
tic_tac_toe()
