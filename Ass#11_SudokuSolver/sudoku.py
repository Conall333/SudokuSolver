'''
Name & Student ID: Conall McCarthy, *********
Date: 20/02/18
Description: Assignment 11, Write a program that takes a file with each line being a row of a unsolved
sudoku puzzle, create a board, solve the sudoku puzzle using 2 functions (1. solveBoard and 2. isValidMove)
and print out a formatted board.

1.solveBoard(b, row, col)
Write a recursive function that attempts to solve the board. Each row should be considered and if all
the rows are completed the board should be solved. Within each row if a column contains a number
the next column is checked recursively. If a column is empty a number should be placed in the
column (if valid) and the function again recursively called.
#
2. def isValidMove (b, row, col, number):Write a function that evaluated whether a
number can be placed in a given row and column as a valid move. Remember that a number (1-9)
cannot be repeated within a given row, column and mini-grid. This function should return True if the
move is valid. Hint use the module (%) operator for the mini-grid case.
'''


# reads in a file in the format of 9 numbers on 9 lines separated by spaces and converts it into a list of lists
# with each inner list being a row
def readBoard(file):
    infile = open(file, "r")
    b = []
    for line in infile:
        newline = line.strip("\n")
        row = newline.split(" ")
        # converts the list row to a list of numbers, not characters
        list_num = []
        for num in row:
            list_num.append(int(num))
        b.append(list_num)
    print(b)
    infile.close()
    return b
# takes a board in the form of a list of lists and formats it into a sudoku table
def printBoard(SBoard):

    for rowNo in range(9):
        if rowNo % 3 == 0:
            print("+---------+---------+---------+")
        for colNo in range(9):
            if colNo % 3 == 0:
                print("|", end="")
            if SBoard[rowNo][colNo] == 0:
                print("   ", end="")
            else:
                print(" %i " % (SBoard[rowNo][colNo]), end="")
        print("|")
    print("+---------+---------+---------+")


# takes a sudoku board(list of lists) and solves the board using recursion
def solveBoard(b, row, col):
    # initially sets result to false
    result = False
    # base case
    # if: Have I reached row number 9. If I have, I've solved the board return True and return the filled out board.
    if row == 9:
        result = True
        return result, b
    # else (recursive case)
    # if the current square is not 0 recursively call the function again passing in the next square .
    else:
        if b[row][col] != 0:
            # if col is less than 8 increment the column, call the function again passing back the result
            # (true or false) and the board, then returns the result and the board
            if col < 8:
                result, b = solveBoard(b, row, col + 1)
                return result, b
            # if the col is == 8, sets col back to 0 and increments the row, call the function again passing back the
            # result (true or false) and the board, then returns the result and the board
            elif col == 8:
                result, b = solveBoard(b, row + 1, 0)
                return result, b

        # else consider every possible combination of number
        else:
            # is this a validNumber?
            # loops through the numbers 1-9
            for new_insert in range(1, 10, 1):

                if isValidMove(b, row, col, new_insert):
                    # update the square with the number
                    b[row][col] = new_insert
                    # finds the next position
                    if col < 8:
                        next_col = col + 1
                        next_row = row
                    else:
                        next_row = row + 1
                        next_col = 0
                    # if recursively calling the function again (next row next col) == true:
                    # return true and the board
                    result, b = solveBoard(b, next_row, next_col)
                    if result == True:
                        return True, b
            # At the end of my loop, set the square back to zero, pass back false and the board
            # if no valid move is found, sets the square back to 0
            b[row][col] = 0

        return result, b


# function that takes the board, current position(row and col) and checks if a number can be placed in that position
def isValidMove(b, row, col, number):
    valid = True

    # CHECK COLUMN
    # checking if number is in the column
    # creates a columns list appending every number in the current to a column using a while loop
    col_list = []
    x = 0
    while x < 9:
        col_list.append(b[x][col])
        x += 1

    if number in col_list:
        valid = False

    # CHECK ROW
    # checks if the number is in the current row (rows already in a list in b)
    elif number in b[row]:
        valid = False

    # CHECK MINI GRID
    else:
        # list to hold the grid numbers
        grid_list = []
        # finds the top row of the grid
        row_check = (row // 3) * 3
        # 2 for loops with a range of 3, that append the numbers in the same gird as current number
        # being checked to the gird list using modular arithmetic
        for row_num in range(0,3,1):
            # finds the leftmost column of the grid, resets on each outer loop
            col_check = (col // 3) * 3
            for col_num in range(0,3,1):
                # appends what is in the current box to the grid list
                grid_list.append(b[row_check][col_check])
                # increments the column on each loop
                col_check += 1
            # increments the row on each loop
            row_check += 1

        # checks if the current number is in the grid_list
        if number in grid_list:
            valid = False
    # returns valid if number passes checks
    return valid


# Main Program
filename = "easyPuzzle.txt"
# filename = "hardPuzzle.txt"
board = readBoard(filename)


print("\nPROBLEM:")
printBoard(board)

# calls the function and checks if the answer is true of false
check_answer, solvedBoard = solveBoard(board, 0, 0)
if check_answer == False:
    print("Solution does not exist")
    printBoard(solvedBoard)
else:
    print("\nSOLUTION:")
    printBoard(solvedBoard)


