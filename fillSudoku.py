from puzzlePrint import *

#Fill sudoku function
def fillSudoku(puz):
    """This function is for filling the puzzle given to the user.
    1. First, the user is asked for a row number: 
        - If the input is not an integer, an error message will be displayed and the input will be asked for again.
        - If the input is a number but is out of range 1-9, the input will be asked for again, 
            an error message will also be displayed if a non-integer is input.
    2. After the row number is accepted, the column number will be asked for.
        - The same conditions for the row number apply for the column number.
    3. Since a list is being worked with, and equation is applied using the row and column numbers(coordinates) input.
        The equation gives a number corresponding to the position in the list (from 0 to 80) for the input coordinates.
    4. Once the position in the list is obtained, the position content is checked:
        4.1. If the content is blank (a space ' '), the user will be asked for the value they wish the position to have.
            The same conditions set for the coordinates input apply.
        4.2. If the content is an integer, the user is asked if they are sure they want to change this vaule indicating 
        the coordinates chosen.
            - If the user inputs a '0' the change is ignored.
            - If another number is input, the previous conditions are applied and the list position value is changed.
        4.3. If the content is different that what is specified, the user will not be allowed to modify the value in the position.
    5. After the value un the position is changed, the new modified list is returned.

    ***When the content is an integer the user is allowed to change the value because it means it was a value previously
        set by the user. This is because the list recieved is full of strings, so if the position has a non-integer
        and it is not ' ' it means the value is a predetermined value and can not be changed.

    Args:
        puz (list): String list containing the new puzzle or puzzle with user inputs (depends on user's progress).

    Returns:
        list: List with new user input (contains strings and integers)
    """

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