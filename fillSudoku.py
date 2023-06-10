from puzzlePrint import *

#Fill sudoku function
def fillSudoku(puz):
    while True:
        try:
            row = int(input("Enter row number (from 1 to 9): "))
            break
        except:
            print('A non-integer was entered')
    '''row = int(input("Enter row number (from 1 to 9): "))
    while row < 1 or row > 9:
        print(style.BOLD + "Please enter a value between 1 and 9" + style.END)
        row = int(input("Enter row number (from 1 to 9): "))'''
    while True:
        try:
            col = int(input("Enter column number (from 1 to 9): "))
            break
        except:
            print('A non-integer was entered')
    '''col = int(input("Enter column number (from 1 to 9): "))
    while col < 1 or col > 9:
        print(style.BOLD + "Please enter a value between 1 and 9" + style.END)
        col = int(input("Enter column number (from 1 to 9): "))'''
    arrayPos = (9*(row-1))+(col-1)
    if puz[arrayPos] == ' ':
        val = int(input("Enter desired value (from 1 to 9): "))
        while val < 1 or val > 9:
            print(style.BOLD + "Please enter a value between 1 and 9." + style.END)
            val = int(input("Enter desired value (from 1 to 9): "))
        puz[arrayPos]=val
        printSudoku(puz)
        return puz
    elif type(puz[arrayPos]) == int:
        print(style.BOLD + "You are changing the previous value of row " + row + " and column " + col + style.END)
        val = int(input("Enter desired value (from 1 to 9): [If you do not wish to change ths value enter '0']"))
        if val == 0:
            printSudoku(puz)
            return puz
        else:
            while val < 1 or val > 9:
                print(style.BOLD + "Please enter a value between 1 and 9." + style.END)
                val = int(input("Enter desired value (from 1 to 9): "))
            puz[arrayPos]=val
            printSudoku(puz)
            return puz
    else:
        print("The value in this position is unchangable, please select a new position.")
        return puz