# Initialize the board
board = [' ' for _ in range(9)]

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def play_game():
    current_player = 'X'
    for turn in range(9):
        print_board()
        move = int(input(f"Player {current_player}, choose your move (0-8): "))
        if board[move] == ' ':
            board[move] = current_player
            if check_winner(current_player):
                print_board()
                print(f"🎉 Player {current_player} wins!")
                return
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")
            turn -= 1
    print_board()
    print("It's a draw!")

play_game()