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
# handle turn

display_board()
