# board
board = [" " for i in range(9)]

# possible moves

# handle sign
# display board


def display_board():
    """
            displays the board on the screen
    """

    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

# play game
# check is player or computer win
# check is board full


def check_if_full():
    if " " not in board:
        return True
    return False
# handle turn

if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!\n")
    display_board()
    print(check_if_full())
