import random
# board
board = [str(i) for i in range(10)]

board[0] = "!"  # we won't use it

# possible moves
possible_moves = [i for i in range(1, 10)]
# computer sign
c_sign = "X"

# gamer sign
g_sign = "O"


# handle sign
def handle_sign():
    while True:
        g_sign = input("Choose your sign! (X or O)")
        if g_sign == "X" or g_sign == "x":
            return "X", "O"

        elif g_sign == "O" or g_sign == "o":
            return "O", "X"


# display board
def display_board():
    """
        displays the board on the screen
    """

    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("-----------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("-----------")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])


# computer plays game
def computer_play():
    computer_move = random.choice(possible_moves)
    print("Computer moved:", computer_move)
    board[computer_move] = c_sign
    possible_moves.remove(computer_move)


# gamer plays
def gamer_play():
    print("Your turn!")
    gamer_move = int(input("Your move: "))
    board[gamer_move] = g_sign
    possible_moves.remove(gamer_move)
    print("---------------------")


# check if board is full
def check_if_board_is_full():
    if " " not in board[1:]:
        return True
    return False


# check if computer win
def check_if_computer_win():
    # check rows
    if (board[1] == c_sign) and (board[2] == c_sign) and (board[3] == c_sign):
        return True
    elif (board[4] == c_sign) and (board[5] == c_sign) and (board[6] == c_sign):
        return True
    elif (board[7] == c_sign) and (board[8] == c_sign) and (board[9] == c_sign):
        return True

    # check columns
    elif (board[1] == c_sign) and (board[4] == c_sign) and (board[7] == c_sign):
        return True
    elif (board[2] == c_sign) and (board[5] == c_sign) and (board[8] == c_sign):
        return True
    elif (board[3] == c_sign) and (board[6] == c_sign) and (board[9] == c_sign):
        return True

    # check diagonals
    elif (board[1] == c_sign) and (board[5] == c_sign) and (board[9] == c_sign):
        return True
    elif (board[3] == c_sign) and (board[5] == c_sign) and (board[7] == c_sign):
        return True

    return False


def check_if_gamer_win():
    # check rows
    if (board[1] == g_sign) and (board[2] == g_sign) and (board[3] == g_sign):
        return True
    elif (board[4] == g_sign) and (board[5] == g_sign) and (board[6] == g_sign):
        return True
    elif (board[7] == g_sign) and (board[8] == g_sign) and (board[9] == g_sign):
        return True

    # check columns
    elif (board[1] == g_sign) and (board[4] == g_sign) and (board[7] == g_sign):
        return True
    elif (board[2] == g_sign) and (board[5] == g_sign) and (board[8] == g_sign):
        return True
    elif (board[3] == g_sign) and (board[6] == g_sign) and (board[9] == g_sign):
        return True

    # check diagonals
    elif (board[1] == g_sign) and (board[5] == g_sign) and (board[9] == g_sign):
        return True
    elif (board[3] == g_sign) and (board[5] == g_sign) and (board[7] == g_sign):
        return True

    return False


# play game
def play_game():
    while True:
        if check_if_board_is_full():
            print("Tie!")
            break
        computer_play()
        if check_if_computer_win():
            display_board()
            print("Computer win!")
            break
        display_board()
        gamer_play()
        if check_if_gamer_win():
            display_board()
            print("Congratulations, you win!")
            break

if __name__ == "__main__":
    while True:
        print("-------------------")
        print("Welcome to Tic Tac Toe!\n")
        # board
        board = [str(i) for i in range(10)]

        board[0] = "!"  # we won't use it

        # possible moves
        possible_moves = [i for i in range(1, 10)]
        # computer sign
        c_sign = "X"

        # gamer sign
        g_sign = "O"
        signs = handle_sign()

        g_sign = signs[0]
        c_sign = signs[1]
        print("You are:", g_sign)
        print("Computer is:", c_sign)

        display_board()
        # clean the board after display
        board[1:] = [" " for i in range(9)]

        print("Do your move between 1-9")
        print("---------------------")

        play_game()
