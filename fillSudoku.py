from puzzlePrint import *

#Fill sudoku function
def fillSudoku(puz):
    row = input("Enter row number: ")
    col = input("Enter column number: ")
    r=int(row)
    c=int(col)
    arrayPos = (9*(r-1))+(c-1)
    if puz[arrayPos] == ' ':
        val = input("Enter desired value: ")
        puz[arrayPos]=val
        printSudoku(puz)
        return puz
    else:
        print("The value in this position is unchangable, please select a new position.")
        return puz