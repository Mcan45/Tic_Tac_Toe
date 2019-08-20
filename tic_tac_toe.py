import random
import time
import os


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


# make the winner move
def get_winner_pos():
    winner_pos = []
    if board[1] == " " and board[2] == c_sign and board[3] == c_sign:
        winner_pos.append(1)
    if board[1] == " " and board[4] == c_sign and board[5] == c_sign:
        winner_pos.append(1)
    if board[1] == " " and board[5] == c_sign and board[9] == c_sign:
        winner_pos.append(1)
    if board[2] == " " and board[1] == c_sign and board[3] == c_sign:
        winner_pos.append(2)
    if board[2] == " " and board[5] == c_sign and board[8] == c_sign:
        winner_pos.append(2)
    if board[3] == " " and board[1] == c_sign and board[2] == c_sign:
        winner_pos.append(3)
    if board[3] == " " and board[6] == c_sign and board[9] == c_sign:
        winner_pos.append(3)
    if board[3] == " " and board[5] == c_sign and board[7] == c_sign:
        winner_pos.append(3)
    if board[4] == " " and board[1] == c_sign and board[7] == c_sign:
        winner_pos.append(4)
    if board[4] == " " and board[5] == c_sign and board[6] == c_sign:
        winner_pos.append(4)
    if board[5] == " " and board[1] == c_sign and board[9] == c_sign:
        winner_pos.append(5)
    if board[5] == " " and board[2] == c_sign and board[8] == c_sign:
        winner_pos.append(5)
    if board[5] == " " and board[3] == c_sign and board[7] == c_sign:
        winner_pos.append(5)
    if board[5] == " " and board[4] == c_sign and board[6] == c_sign:
        winner_pos.append(5)
    if board[6] == " " and board[3] == c_sign and board[9] == c_sign:
        winner_pos.append(6)
    if board[6] == " " and board[4] == c_sign and board[5] == c_sign:
        winner_pos.append(6)
    if board[7] == " " and board[1] == c_sign and board[4] == c_sign:
        winner_pos.append(7)
    if board[7] == " " and board[3] == c_sign and board[5] == c_sign:
        winner_pos.append(7)
    if board[7] == " " and board[8] == c_sign and board[9] == c_sign:
        winner_pos.append(7)
    if board[8] == " " and board[2] == c_sign and board[5] == c_sign:
        winner_pos.append(8)
    if board[8] == " " and board[7] == c_sign and board[9] == c_sign:
        winner_pos.append(8)
    if board[9] == " " and board[1] == c_sign and board[5] == c_sign:
        winner_pos.append(9)
    if board[9] == " " and board[3] == c_sign and board[6] == c_sign:
        winner_pos.append(9)
    if board[9] == " " and board[7] == c_sign and board[8] == c_sign:
        winner_pos.append(9)

    return winner_pos


# make the blocker move
def get_blocker_pos():
    blocker_pos = []
    if board[1] == " " and board[2] == g_sign and board[3] == g_sign:
        blocker_pos.append(1)
    if board[1] == " " and board[4] == g_sign and board[5] == g_sign:
        blocker_pos.append(1)
    if board[1] == " " and board[5] == g_sign and board[9] == g_sign:
        blocker_pos.append(1)
    if board[2] == " " and board[1] == g_sign and board[3] == g_sign:
        blocker_pos.append(2)
    if board[2] == " " and board[5] == g_sign and board[8] == g_sign:
        blocker_pos.append(2)
    if board[3] == " " and board[1] == g_sign and board[2] == g_sign:
        blocker_pos.append(3)
    if board[3] == " " and board[6] == g_sign and board[9] == g_sign:
        blocker_pos.append(3)
    if board[3] == " " and board[5] == g_sign and board[7] == g_sign:
        blocker_pos.append(3)
    if board[4] == " " and board[1] == g_sign and board[7] == g_sign:
        blocker_pos.append(4)
    if board[4] == " " and board[5] == g_sign and board[6] == g_sign:
        blocker_pos.append(4)
    if board[5] == " " and board[1] == g_sign and board[9] == g_sign:
        blocker_pos.append(5)
    if board[5] == " " and board[2] == g_sign and board[8] == g_sign:
        blocker_pos.append(5)
    if board[5] == " " and board[3] == g_sign and board[7] == g_sign:
        blocker_pos.append(5)
    if board[5] == " " and board[4] == g_sign and board[6] == g_sign:
        blocker_pos.append(5)
    if board[6] == " " and board[3] == g_sign and board[9] == g_sign:
        blocker_pos.append(6)
    if board[6] == " " and board[4] == g_sign and board[5] == g_sign:
        blocker_pos.append(6)
    if board[7] == " " and board[1] == g_sign and board[4] == g_sign:
        blocker_pos.append(7)
    if board[7] == " " and board[3] == g_sign and board[5] == g_sign:
        blocker_pos.append(7)
    if board[7] == " " and board[8] == g_sign and board[9] == g_sign:
        blocker_pos.append(7)
    if board[8] == " " and board[2] == g_sign and board[5] == g_sign:
        blocker_pos.append(8)
    if board[8] == " " and board[7] == g_sign and board[9] == g_sign:
        blocker_pos.append(8)
    if board[9] == " " and board[1] == g_sign and board[5] == g_sign:
        blocker_pos.append(9)
    if board[9] == " " and board[3] == g_sign and board[6] == g_sign:
        blocker_pos.append(9)
    if board[9] == " " and board[7] == g_sign and board[8] == g_sign:
        blocker_pos.append(9)

    return blocker_pos


# computer plays game
def computer_play():
    print("Computer is playing...")
    random_second = random.randint(0, 2)
    time.sleep(random_second)

    winner_moves = get_winner_pos()
    blocker_moves = get_blocker_pos()

    if len(winner_moves) > 0:
        computer_move = random.choice(winner_moves)
        if computer_move in possible_corners:
            possible_corners.remove(computer_move)
        elif computer_move in possible_middle:
            possible_middle.remove(computer_move)
        else:
            possible_edges.remove(computer_move)

    elif len(blocker_moves) > 0:
        computer_move = random.choice(blocker_moves)
        if computer_move in possible_corners:
            possible_corners.remove(computer_move)
        elif computer_move in possible_middle:
            possible_middle.remove(computer_move)
        else:
            possible_edges.remove(computer_move)
    else:

        # plays randomly from corners
        if len(possible_corners) > 0:
            computer_move = random.choice(possible_corners)
            possible_corners.remove(computer_move)
        elif len(possible_middle) > 0:
            computer_move = 5
            possible_middle.remove(computer_move)
        elif len(possible_edges) > 0:
            computer_move = random.choice(possible_edges)
            possible_edges.remove(computer_move)

    print("Computer moved:", computer_move)
    board[computer_move] = c_sign


# gamer plays
def gamer_play():

    while True:
        print("Your turn!")
        gamer_move = input("Your move: ")

        # if numeric
        if gamer_move in [str(i) for i in range(1, 10)]:
            gamer_move = int(gamer_move)

            # if move is played before
            if gamer_move not in possible_corners and gamer_move not in possible_middle and gamer_move not in possible_edges:
                print("Impossible move!")

            # if move is appropirate play regularly
            else:
                board[gamer_move] = g_sign
                if gamer_move in [1, 3, 7, 9]:
                    possible_corners.remove(gamer_move)
                elif gamer_move == 5:
                    possible_middle.remove(gamer_move)
                elif gamer_move in [2, 4, 6, 8]:
                    possible_edges.remove(gamer_move)
                print("---------------------")
                break

        # if not numeric
        else:
            print("Press [1-9]")


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

        computer_play()
        display_board()
        if check_if_computer_win():
            print("Computer win!")
            break
        if check_if_board_is_full():
            print("Tie!")
            break
        gamer_play()
        display_board()
        if check_if_gamer_win():
            print("Congratulations, you win!")
            break
        if check_if_board_is_full():
            print("Tie!")


# clean the console
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":

    while True:
        cls()
        print("-------------------")
        print("Welcome to Tic Tac Toe!\n")

        # board
        board = [str(i) for i in range(10)]

        board[0] = "!"  # we won't use it

        # possible moves
        possible_corners = [1, 3, 7, 9]
        possible_middle = [5]
        possible_edges = [2, 4, 6, 8]

        signs = handle_sign()
        # gamer sign

        g_sign = signs[0]
        # computer sign
        c_sign = signs[1]

        display_board()
        # clean the board after display
        board[1:] = [" " for i in range(9)]

        print("You are:", g_sign)
        print("Computer is:", c_sign)

        print("Do your move between 1-9")
        print("---------------------")

        play_game()
        print("Press q to quit game")
        quit = input("any key to continue: ")
        if quit == "q" or quit == "Q":
            print("Quitting...")
            time.sleep(1)
            break
