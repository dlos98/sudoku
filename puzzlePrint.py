#Declaring values to make string bold and end the style
class style:
    BOLD = "\033[1m"
    END = "\033[0m"

#Print function
def printSudoku(puz):
    """This function is to print the sudoku puzzle as a grid so user can better identify rows and columns.
    Every 3 rows are identified by a line of '='s, as well as before the first row, the rest are separated by '-'s.
    Before the first column and every 3 columns are separated by 'ㅒ's, the rest by '|'s.

    Args:
        puz (list): List to be shown in grid
    """

    count=0
    print(style.BOLD + "=========================================" + style.END)
    for row in range(9):
        for column in range(9):
            if column == 0:
                print(style.BOLD + "ㅒ" + style.END, end=" ")
            if (column+1)%3 == 0:
                print(puz[column+count],style.BOLD + "ㅒ" + style.END, end=" ")
            else:
                print(puz[column+count],"|", end=" ")
        print()
        if (row+1)%3 == 0:
            print(style.BOLD + "=========================================" + style.END)
        else:
            print("-----------------------------------------")
        count=count+9


#Bold given numbers
def boldNum(array):
    """This function is to make the non-blank numbers from the given list bold.
    This will help users differentiate the numbers given from the numbers input.

    Args:
        array (list): New puzzle list
    """

    for i in range(81):
        if array[i] != ' ':
            array[i] = style.BOLD + array[i] + style.END

#Bold answer key
def boldKey(blank,key):
    """This function is to make the numbers in the answer key list, that match the non-blank numbers in the new puzzle list, bold.
    This is done so when comparing the output to the answer key, the predetermined number match.

    Args:
        blank (list): List corresponding to new puzzle
        key (list): List corresponding to answer key for new puzzle

    Returns:
        list: Answer key list with bolded numbers
    """

    for i in range(81):
        if blank[i] == key[i]:
            key[i] = style.BOLD + key[i] + style.END
    return key

#Convert file line string to list of strings (each number is an element of the list)
def convertStrToList(string):
    """Converts a single line string obtained from csv file into a list of strings containing each element.
    Uses ',' as the sparator.

    Args:
        string (String): String from csv file (Contains ','s).

    Returns:
        list: List of strings obtained after splitting the single string.
    """

    puzList = list(string.split(","))
    if puzList[80] == ' \n':
        puzList[80] = ' '
    for i in range(9):
        if puzList[80] == (str(i+1) + '\n'):
            puzList[80] = str(i+1)
    return puzList