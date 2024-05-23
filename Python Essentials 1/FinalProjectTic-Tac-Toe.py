# Your task is to write a simple program which pretends to play tic-tac-toe with the user. To make it all easier for you, we've decided to simplify the game. Here are our assumptions:
    # the computer (i.e., your program) should play the game using 'X's;
    # the user (e.g., you) should play the game using 'O's;
    # the first move belongs to the computer − it always puts its first 'X' in the middle of the board;
    # all the squares are numbered row by row starting with 1 (see the example session below for reference)
    # the user inputs their move by entering the number of the square they choose − the number must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
    # the program checks if the game is over − there are four possible verdicts: the game should continue, the game ends with a tie, you win, or the computer wins;
    # the computer responds with its move and the check is repeated;
    # don't implement any form of artificial intelligence − a random field choice made by the computer is good enough for the game.
# Example:
# +-------+-------+-------+
# |       |       |       |
# |   1   |   2   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+
# Enter your move: 1
# +-------+-------+-------+
# |       |       |       |
# |   O   |   2   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+
# Enter your move: 8
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# Enter your move: 4
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# Enter your move: 7
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# You won!

## Requirements
# Implement the following features:
    # the board should be stored as a three-element list, while each element is another three-element list (the inner lists represent rows) so that all of the squares may be accessed using the following syntax:
        # board[row][column]
    # each of the inner list's elements can contain 'O', 'X', or a digit representing the square's number (such a square is considered free)
    # the board's appearance should be exactly the same as the one presented in the example.
    # implement the functions defined for you in the editor.

# Drawing a random integer number can be done by utilizing a Python function called randrange(). The example program below shows how to use it (the program prints ten random numbers from 0 to 8).
# Note: the from-import instruction provides access to the randrange function defined within an external Python module callled random.
    # from random import randrange
    
    # for i in range(10):
    #     print(randrange(8))

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        for col in row:
            print(f"|   {col}   ", end="")
        print("|")
        print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    move = int(input("Enter your move (1-9): "))
    row, col = divmod(move - 1, 3)
    if board[row][col] in ['X', 'O']:
        print("Invalid move. Please choose an empty square.")
        return enter_move(board)
    else:
        board[row][col] = 'O'


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['X', 'O']:
                free_fields.append((i, j))
    return free_fields


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)):
            return True
    for j in range(3):
        if all(board[i][j] == sign for i in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)):
        return True
    if all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    from random import choice
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = choice(free_fields)
        board[row][col] = 'X'

def main():
    # board = [[str(i * 3 + j + 1) for j in range(3)] for i in range(3)]
    board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]
    display_board(board)
    turn = 'user'
    while True:
        if turn == 'user':
            enter_move(board)
            display_board(board)
            if victory_for(board, 'O'):
                print("You won!")
                break
            if not make_list_of_free_fields(board):
                print("It's a tie!")
                break
            turn = 'computer'
        else:
            draw_move(board)
            display_board(board)
            if victory_for(board, 'X'):
                print("Computer won!")
                break
            if not make_list_of_free_fields(board):
                print("It's a tie!")
                break
            turn = 'user'

if __name__ == "__main__":
    main()
