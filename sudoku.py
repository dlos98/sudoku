import random

class style:
    BOLD = "\033[1m"
    END = "\033[0m"

#FUNCTIONS
#Print function
def blankSudoku(puz):
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

#Fill sudoku function
def fillSudoku(puz):
    row = int(input("Enter row number (from 1 to 9): "))
    while row < 1 or row > 9:
        print(style.BOLD + "Please enter a value between 1 and 9" + style.END)
        row = int(input("Enter row number (from 1 to 9): "))
    col = int(input("Enter column number (from 1 to 9): "))
    while col < 1 or col > 9:
        print(style.BOLD + "Please enter a value between 1 and 9" + style.END)
        col = int(input("Enter column number (from 1 to 9): "))
    arrayPos = (9*(row-1))+(col-1)
    if puz[arrayPos] == ' ':
        val = int(input("Enter desired value (from 1 to 9): "))
        while val < 1 or val > 9:
            print(style.BOLD + "Please enter a value between 1 and 9." + style.END)
            val = int(input("Enter desired value (from 1 to 9): "))
        puz[arrayPos]=val
        blankSudoku(puz)
        return puz
    elif type(puz[arrayPos]) == int:
        print(style.BOLD + "You are changing the previous value of row " + row + " and column " + col + style.END)
        val = int(input("Enter desired value (from 1 to 9): [If you do not wish to change ths value enter '0']"))
        if val == 0:
            blankSudoku(puz)
            return puz
        else:
            while val < 1 or val > 9:
                print(style.BOLD + "Please enter a value between 1 and 9." + style.END)
                val = int(input("Enter desired value (from 1 to 9): "))
            puz[arrayPos]=val
            blankSudoku(puz)
            return puz
    else:
        print("The value in this position is unchangable, please select a new position.")
        return puz

#Check puzzle completion
def isComplete(sol):
    for i in range(81):
        if sol[i] == ' ':
            return False

#Solution check
def isSolved(filled, key):
    isSol = True
    for i in range(81):
        if filled[i] != key[i]:
            isSol = False
    if isSol == False:
        print('Sorry, the solution is incorrect. Try again')
    else:
        print('Congratulations!')        
    
#Convert file line string to list of strings (each number is an element of the list)
def convertStrToList(string):
    puzList = list(string.split(","))
    if puzList[80] == ' \n':
        puzList[80] = ' '
    for i in range(9):
        if puzList[80] == (str(i+1) + '\n'):
            puzList[80] = str(i+1)
    return puzList


####################################################################################################################################

#PUZZLES
#Open and read puzzles file
with open('puzzles.csv', 'r') as f:
    puzzlesLines = f.readlines()

####################################################################################################################################

#ANSWER KEYS
#Open and read answer key file
with open('solvedPuzzles.csv', 'r') as fKey:
    answersLines = fKey.readlines()

####################################################################################################################################

#RANDOM PUZZLE PRINT

#sudokuAnswers=[solvedSu1,solvedSu2,solvedSu3,solvedSu4,solvedSu5,solvedSu6,solvedSu7,solvedSu8,solvedSu9,solvedSu10]
#Chose random puzzle
rdmNumb=random.randint(1,10)


#Hold chosen puzzle from file
chosen = puzzlesLines[rdmNumb-1]

#Convert chosen puzzle string to list of strings
chosenList = convertStrToList(chosen)

#Read lines from answer key file, hold correct puzzle key and convert to list of strings
chosenKey = answersLines[rdmNumb-1]
chosenKeyList = convertStrToList(chosenKey)

####################################################################################################################################

#PROGRAM
#Equal key
bKey=boldKey(chosenList,chosenKeyList)

#Show puzzle to be solved
boldNum(chosenList)
blankSudoku(chosenList)


#Answer sudoku
while isComplete(fillSudoku(chosen)) == False:
    isComplete(fillSudoku(chosen))

#Change solution to String
for i in range(81):
    if type(chosen[i]) == int:
        chosen[i] = str(chosen[i])

#Check user solution
isSolved(chosenList,bKey)