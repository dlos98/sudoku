from puzzlePrint import *

#Fill sudoku function
def fillSudoku(puz):
    #Row value
    while True:
        try:
            row = int(input("Enter row number (from 1 to 9): "))
            break
        except ValueError:
            print(style.BOLD + 'A non-integer was entered. Try again.' + style.END)
    while row < 1 or row > 9:
        print(style.BOLD + "Please enter a value between 1 and 9" + style.END)
        try:
            row = int(input("Enter row number (from 1 to 9): "))
        except ValueError:
            print(style.BOLD + 'A non-integer was entered. Try again.' + style.END)
    #Column value
    while True:
        try:
            col = int(input("Enter column number (from 1 to 9): "))
            break
        except ValueError:
            print(style.BOLD + 'A non-integer was entered. Try again.' + style.END)
    while col < 1 or col > 9:
        print(style.BOLD + "Please enter a value between 1 and 9" + style.END)
        try:
            col = int(input("Enter column number (from 1 to 9): "))
        except ValueError:
            print(style.BOLD + 'A non-integer was entered. Try again.' + style.END)

    arrayPos = (9*(row-1))+(col-1)

    #Position value
    if puz[arrayPos] == ' ':
        while True:
            try:
                val = int(input("Enter desired value (from 1 to 9): "))
                break
            except ValueError:
                print(style.BOLD + 'A non-integer was entered. Try again.' + style.END)
        while val < 1 or val > 9:
            print(style.BOLD + "Please enter a value between 1 and 9." + style.END)
            try:
                val = int(input("Enter desired value (from 1 to 9): "))
            except ValueError:
                print(style.BOLD + 'A non-integer was entered. Try again.' + style.END)
        puz[arrayPos]=val
        printSudoku(puz)
        return puz
    elif type(puz[arrayPos]) == int:
        print(style.BOLD + "You are changing the previous value of row " + str(row) + " and column " + str(col) + style.END)
        while True:
            try:
                val = int(input("Enter desired value (from 1 to 9): [If you do not wish to change ths value enter '0']"))
                break
            except ValueError:
                print(style.BOLD + 'A non-integer was entered. Try again.' + style.END)
        if val == 0:
            printSudoku(puz)
            return puz
        else:
            while val < 1 or val > 9:
                print(style.BOLD + "Please enter a value between 1 and 9." + style.END)
                try:
                    val = int(input("Enter desired value (from 1 to 9): "))
                except:
                    print(style.BOLD + 'A non-integer was entered. Try again.' + style.END)
            puz[arrayPos]=val
            printSudoku(puz)
            return puz
    else:
        print("The value in this position is unchangable, please select a new position.")
        return puz