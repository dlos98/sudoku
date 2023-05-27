import random
import numpy
from numpy import *

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
    row = input("Enter row number: ")
    col = input("Enter column number: ")
    r=int(row)
    c=int(col)
    arrayPos = (9*(r-1))+(c-1)
    if puz[arrayPos] == ' ':
        val = input("Enter desired value: ")
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

f = open("puzzles.txt", "r")

####################################################################################################################################

#ANSWER KEYS

fKey = open("solvedPuzzles.csv", "r")

####################################################################################################################################

#RANDOM PUZZLE PRINT

#sudokuAnswers=[solvedSu1,solvedSu2,solvedSu3,solvedSu4,solvedSu5,solvedSu6,solvedSu7,solvedSu8,solvedSu9,solvedSu10]
#Chose random puzzle
rdmNumb=random.randint(1,10)


#Read all lines from puzzles file and hold chosen puzzle
csvLines = f.readlines()
chosen = csvLines[rdmNumb-1]

#Convert chosen puzzle string to list of strings
chosenList = convertStrToList(chosen)

#Read lines from answer key file, hold correct puzzle key and convert to list of strings
fileLines = fKey.readlines()
chosenKey = fileLines[rdmNumb-1]
chosenKeyList = convertStrToList(chosenKey)

'''
#Read a specific line
with open("puzzles.txt", "r") as f:
    chosen = f.readlines()[rdmNumb-1]
    print(chosen)
'''
####################################################################################################################################

#PROGRAM
#Equal key
bKey=boldKey(chosenList,chosenKeyList)

#Show puzzle to be solved
boldNum(chosenList)
blankSudoku(chosenList)


#Answer sudoku
while isComplete(fillSudoku(chosenList)) == False:
    isComplete(fillSudoku(chosenList))

#Check user solution
isSolved(chosenList,bKey)