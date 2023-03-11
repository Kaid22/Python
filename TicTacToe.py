import math

# Initialize the game board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Print the game board
def print_board():
    print("  0 1 2")
    for i in range(3):
        print(i, end=' ')
        for j in range(3):
            print(board[i][j], end=' ')
        print()

# Check if the game is over
def is_game_over():
    # Check rows
    for i in range(3):
        if board[i][0] != ' ' and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return True

    # Check columns
    for j in range(3):
        if board[0][j] != ' ' and board[0][j] == board[1][j] and board[1][j] == board[2][j]:
            return True

    # Check diagonals
    if board[0][0] != ' ' and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return True

    if board[0][2] != ' ' and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return True

    # Check for tie
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False

    return True

# Check if a move is valid
def is_valid_move(row, col):
    if row < 0 or row >= 3 or col < 0 or col >= 3:
        return False
    if board[row][col] != ' ':
        return False
    return True

# Make a move
def make_move(player, row, col):
    board[row][col] = player

# Undo a move
def undo_move(row, col):
    board[row][col] = ' '

# Get the score for the current board state
def get_score():
    # Check rows
    for i in range(3):
        if board[i][0] != ' ' and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0] == 'X':
                return -1
            elif board[i][0] == 'O':
                return 1

    # Check columns
    for j in range(3):
        if board[0][j] != ' ' and board[0][j] == board[1][j] and board[1][j] == board[2][j]:
            if board[0][j] == 'X':
                return -1
            elif board[0][j] == 'O':
                return 1

    # Check diagonals
    if board[0][0] != ' ' and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return -1
        elif board[0][0] == 'O':
            return 1

    if board[0][2] != ' ' and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return -1
        elif board[0][2] == 'O':
            return 1

    # Game is not over
    return 0

# Minimax algorithm
def minimax(player, depth):
    # Check if the game is over or the maximum depth is reached
    if is_game_over() or depth == 0:
        return get_score()

    # Maximize the score for the computer (O player)
    if player == 'O':
        max_score = -math.inf
        for i in range(3):
            for j in range(3):
                if is_valid_move(i, j):
                    make_move(player, i, j)
                    score = minimax('X', depth-1)
                    undo_move(i, j)
                    max_score = max(max_score, score)
        return max_score

    # Minimize the score for the human (X player)
    if player == 'X':
        min_score = math.inf
        for i in range(3):
            for j in range(3):
                if is_valid_move(i, j):
                    make_move(player, i, j)
                    score = minimax('O', depth-1)
                    undo_move(i, j)
                    min_score = min(min_score, score)
        return min_score

# Make a computer move
def make_computer_move():
    best_score = -math.inf
    best_row = -1
    best_col = -1
    for i in range(3):
        for j in range(3):
            if is_valid_move(i, j):
                make_move('O', i, j)
                score = minimax('X', 5)
                undo_move(i, j)
                if score > best_score:
                    best_score = score
                    best_row = i
                    best_col = j
    make_move('O', best_row, best_col)

# Play the game
player = 'X'
while not is_game_over():
    if player == 'X':
        print_board()
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        while not is_valid_move(row, col):
            print("Invalid move. Try again.")
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))
        make_move(player, row, col)
    else:
        print("Computer's turn")
        make_computer_move()
    player = 'O' if player == 'X' else 'X'

# Print the final game board
print_board()

# Print the winner or tie message
if get_score() == -1:
    print("X won!")
elif get_score() == 1:
    print("O won!")
else:
    print("Tie!")
