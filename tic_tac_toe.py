#board
#display board
#play a game
#handle turn
#check win
#check rows
#check colums
#check diaganols
#check tie
#flip player


#--------------GLOBAL VARIABLES--------

#game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

#if game is still going
game_still_going = True

#who won
winner = None

#whos turn is it
current_player = "X"

#--------------------------------------

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():

    #display initial board
    display_board()

    while game_still_going:
        #handle a single turn of player
        handle_turn(current_player)

        check_if_game_over()

        # flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie")


def handle_turn(player):
    print(player + "'s turn.")
    position = input("choose a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3",  '4', '5', '6', '7', '8', '9']:
            position = input("hoose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == '-':
            valid = True
        else:
            print("You cant go there, try again.")

    board[position] = player

    display_board()


def check_if_game_over():
    check_for_winner()
    check_for_tie()


def check_for_winner():

    #set up global variables
    global winner

    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        #theres no winner
        winner = None
    return


def check_rows():
    #set up gloabl vars
    global  game_still_going
    #check if any rows have same value that isnt a -
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    #if any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False

    #return winner(x Or o)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    #setup gloabl vars
    global game_still_going
    # check if any rows have same value that isnt a -
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # if any row does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False

    # return winner(x Or o)
    if column_1:
        return board[0]
    elif column_2:
        return board[3]
    elif column_3:
        return board[6]
    return


def check_diagonals():
    #set up gloabl vars
    global game_still_going
    # check if any rows have same value that isnt a -
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    # if any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False

    # return winner(x Or o)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return

def check_for_tie():
    #set globals
    global  game_still_going
    #checks for a - to see if game is still going and tied
    if "-" not in board:
        game_still_going = False

    return


def flip_player():
    # set up global
    global current_player
    # if current player was X it changes to O
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play_game()