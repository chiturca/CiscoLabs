### 3.7.1 Lists in lists
# Lists can consist of scalars (namely numbers) and elements of a much more complex structure (you've already seen such examples as strings, booleans, or even other lists in the previous Section Summary lessons). Let's have a closer look at the case where a list's elements are just lists.
# We often find such arrays in our lives. Probably the best example of this is a chessboard.
# Let's assume that we're able to use the selected numbers to represent any chess piece. We can also assume that every row on the chessboard is a list.
row = []
WHITE_PAWN = "WHITE_PAWN" #I have created it symbolically
for i in range(8):
    row.append(WHITE_PAWN) #It builds a list containing eight elements representing the second row of the chessboard ‒ the one filled with pawns (assume that WHITE_PAWN is a predefined symbol representing a white pawn).

## List comprehensions
# A list comprehension is actually a list, but created on-the-fly during program execution, and is not described statically.
row = [WHITE_PAWN for i in range(8)]
    # the data to be used to fill the list (WHITE_PAWN)
    # the clause specifying how many times the data occurs inside the list (for i in range(8))
squares = [x ** 2 for x in range(10)]
twos = [2 ** i for i in range(8)]
odds = [x for x in squares if x % 2 != 0 ]
print(squares) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(twos) #[1, 2, 4, 8, 16, 32, 64, 128]
print(odds) #[1, 9, 25, 49, 81]

### 3.7.2 Two-dimensional arrays
# Let's also assume that a predefined symbol named EMPTY designates an empty field on the chessboard.
# So, if we want to create a list of lists representing the whole chessboard, it may be done in the following way:
board = []
EMPTY=0 #I have created it symbolically
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
    # the inner part of the loop creates a row consisting of eight elements (each of them equal to EMPTY) and appends it to the board list;
    # the outer part repeats it eight times;
    # in total, the board list consists of 64 elements (all equal to EMPTY)
# This model perfectly mimics the real chessboard, which is in fact an eight-element list of elements, all being single rows. Let's summarize our observations:
    # the elements of the rows are fields, eight of them per row;
    # the elements of the chessboard are rows, eight of them per chessboard.
# The board variable is now a two-dimensional array. It's also called, by analogy to algebraic terms, a matrix.
# As list comprehensions can be nested, we can shorten the board creation in the following way:
board = [[EMPTY for i in range(8)] for j in range(8)]

# CHESSBOARD CREATED(HARDCODED OFCOURSE):
board = []
EMPTY=0
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
board[0][3] = "WHITE_QUEEN"
board[0][4] = "WHITE_KING"
board[0][2] = "WHITE_BISHOP"
board[0][5] = "WHITE_BISHOP"
board[0][1] = "WHITE_KNIGHT"
board[0][6] = "WHITE_KNIGHT"
board[0][0] = "WHITE_ROOK"
board[0][7] = "WHITE_ROOK"
board[1]= ["WHITE_PAWN" for i in range(8)]
board[6]= ["BLACK_PAWN" for i in range(8)]
board[7][3] = "BLACK_QUEEN"
board[7][4] = "BLACK_KING"
board[7][2] = "BLACK_BISHOP"
board[7][5] = "BLACK_BISHOP"
board[7][1] = "BLACK_KNIGHT"
board[7][6] = "BLACK_KNIGHT"
board[7][0] = "BLACK_ROOK"
board[7][7] = "BLACK_ROOK"
print(board) #Output:
#[
# ['WHITE_ROOK', 'WHITE_KNIGHT', 'WHITE_BISHOP', 'WHITE_QUEEN', 'WHITE_KING', 'WHITE_BISHOP', 'WHITE_KNIGHT', 'WHITE_ROOK'], 
# ['WHITE_PAWN', 'WHITE_PAWN', 'WHITE_PAWN', 'WHITE_PAWN', 'WHITE_PAWN', 'WHITE_PAWN', 'WHITE_PAWN', 'WHITE_PAWN'], 
# [0, 0, 0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0, 0, 0], 
# ['BLACK_PAWN', 'BLACK_PAWN', 'BLACK_PAWN', 'BLACK_PAWN', 'BLACK_PAWN', 'BLACK_PAWN', 'BLACK_PAWN', 'BLACK_PAWN'], 
# ['BLACK_ROOK', 'BLACK_KNIGHT', 'BLACK_BISHOP', 'BLACK_QUEEN', 'BLACK_KING', 'BLACK_BISHOP', 'BLACK_KNIGHT', 'BLACK_ROOK']
# ]

### 3.7.3 Multidimensional nature of lists: advanced applications
# Python does not limit the depth of list-in-list inclusion. Here you can see an example of a three-dimensional array:
# Imagine a hotel. It's a huge hotel consisting of three buildings, 15 floors each. There are 20 rooms on each floor. For this, you need an array which can collect and process information on the occupied/free rooms.
    # First step ‒ the type of the array's elements. In this case, a Boolean value (True/False) would fit.
    # Step two ‒ calm analysis of the situation. Summarize the available information: three buildings, 15 floors, 20 rooms.
# Now you can create the array:
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
# The first index (0 through 2) selects one of the buildings; the second (0 through 14) selects the floor, the third (0 through 19) selects the room number. All rooms are initially free.
# Now you can book a room for two newlyweds: in the second building, on the tenth floor, room 14:
rooms[1][9][13] = True
# and release the second room on the fifth floor located in the first building:
rooms[0][4][1] = False
# Check if there are any vacancies on the 15th floor of the third building:
vacancy = 0
for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
# The vacancy variable contains 0 if all the rooms are occupied, or the number of available rooms otherwise.