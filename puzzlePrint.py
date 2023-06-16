#Declaring values to make string bold and end the style
class style:
    BOLD = "\033[1m"
    END = "\033[0m"

#Print function
def printSudoku(puz):
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
    for i in range(81):
        if array[i] != ' ':
            array[i] = style.BOLD + array[i] + style.END

#Bold answer key
def boldKey(blank,key):
    for i in range(81):
        if blank[i] == key[i]:
            key[i] = style.BOLD + key[i] + style.END
    return key

#Convert file line string to list of strings (each number is an element of the list)
def convertStrToList(string):
    puzList = list(string.split(","))
    if puzList[80] == ' \n':
        puzList[80] = ' '
    for i in range(9):
        if puzList[80] == (str(i+1) + '\n'):
            puzList[80] = str(i+1)
    return puzList