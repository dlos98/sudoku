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
    

####################################################################################################################################

#PUZZLES

f = open("puzzles.txt", "r")
"""
su1=[' ','4',' ',' ',' ',' ','5','8','2',' ','2','3','7','5',' ',' ','1','4',' ','8','6',' ','2',' ',' ',' ',' ',' ','7',' ','4',' ','6','1',' ',' ',' ','6',' ',' ','3',' ',' ','9',' ',' ',' ','1','2',' ','5',' ','4',' ',' ',' ',' ',' ','8',' ','4','3',' ','6','5',' ',' ','1','7','9','2',' ','8','3','9',' ',' ',' ',' ','6',' ']
su2=[' ',' ',' ',' ',' ','9','6',' ',' ','7','2',' ',' ','6',' ','5','1',' ',' ','4','3','8',' ','5','7','2','9',' ','5',' ',' ',' ','7','8','6',' ','9','7','8',' ',' ',' ','2','3','4',' ','6','1','3',' ',' ',' ','5',' ','8','1','6','7',' ','2','3','9',' ',' ','9','2',' ','3',' ',' ','7','6',' ',' ','7','1',' ',' ',' ',' ',' ']
su3=[' ','7',' ',' ',' ',' ','6',' ','8','9',' ',' ','7',' ','8','2','5','3','8',' ','2',' ','6',' ','4',' ','7','4',' ','3','1','7',' ','9',' ',' ','7',' ','9','4',' ','3','1',' ','5',' ',' ','1',' ','2','6','7',' ','4','6',' ','8',' ','9',' ','3',' ','1','2','1','4','8',' ','7',' ',' ','9','3',' ','7',' ',' ',' ',' ','4',' ']
su4=[' ','2',' ','8',' ',' ','9',' ',' ',' ','8','1','5',' ','2',' ','3','7','5',' ',' ','9','4','1','8','2','6',' ',' ','5',' ','1','6',' ',' ',' ',' ','4','2',' ',' ',' ','6','1',' ',' ',' ',' ','7','9',' ','5',' ',' ','6','5','9','1','7','3',' ',' ','8','3','7',' ','4',' ','9','1','6',' ',' ',' ','4',' ',' ','8',' ','9',' ']
su5=[' ',' ','8','5','6',' ',' ',' ',' ',' ','5','6','2','4','9','3',' ','7',' ','4','9','1',' ','7',' ','5','6','4','2',' ',' ','1',' ',' ',' ',' ','8','9',' ',' ',' ',' ',' ','4','1',' ',' ',' ',' ','7',' ',' ','2','8','9','1',' ','4',' ','8','6','7',' ','7',' ','2','3','5','6','1','9',' ',' ',' ',' ',' ','9','1','8',' ',' ']
su6=[' ','2','8','4',' ','1','3','7','5',' ',' ','7','2','9','8','6',' ',' ','4',' ',' ',' ',' ','7','8',' ','9','7',' ',' ',' ',' ','2',' ','9',' ','1','8',' ','9',' ','4',' ','6','3',' ','9',' ','7',' ',' ',' ',' ','1','8',' ','6','3',' ',' ',' ',' ','7',' ',' ','5','8','7','9','1',' ',' ','3','7','9','1',' ','6','5','8',' ']
su7=['1','8','3','5','2','9',' ',' ','4',' ',' ',' ','7','1','8',' ',' ',' ','9','5','7',' ','3',' ',' ','1',' ','5','3',' ',' ',' ',' ',' ',' ','6','2',' ','4','8',' ','3','1',' ','9','6',' ',' ',' ',' ',' ',' ','3','8',' ','4',' ',' ','5',' ','2','8','3',' ',' ',' ','3','7','2',' ',' ',' ','3',' ',' ','4','8','1','9','6','7']
su8=[' ','4','3',' ',' ',' ','9',' ',' ',' ',' ','8','2',' ','9','7','3',' ','6',' ','9','5',' ',' ','1',' ','4','9','5','4',' ','8',' ',' ',' ','3',' ',' ',' ',' ','6',' ',' ',' ',' ','3',' ',' ',' ','1',' ','8','4','7','8',' ','6',' ',' ','7','4',' ','9',' ','9','7','3',' ','4','2',' ',' ',' ',' ','5',' ',' ',' ','3','7',' ']
su9=[' ',' ',' ','5',' ','4','2',' ',' ',' ',' ','7',' ',' ',' ',' ',' ','4',' ',' ','1','3',' ','9',' ','6','8','7','4',' ','2','8','1','5',' ','6','3',' ','2',' ',' ',' ','1',' ','7','6',' ','5','7','9','3',' ','4','2','5','3',' ','6',' ','7','9',' ',' ','1',' ',' ',' ',' ',' ','4',' ',' ',' ',' ','4','9',' ','5',' ',' ',' ']
su10=['1',' ','8','2',' ',' ','7',' ',' ',' ',' ',' ','4',' ','8',' ','9','5','5','9',' ',' ','3','7','1','4','8',' ','2','9',' ',' ','3',' ','5',' ',' ','8',' ',' ',' ',' ',' ','1',' ',' ','5',' ','7',' ',' ','3','2',' ','8','1','4','5','6',' ',' ','7','3','2','3',' ','8',' ','4',' ',' ',' ',' ',' ','5',' ',' ','1','4',' ','2']
"""
####################################################################################################################################

#ANSWER KEYS

solvedSu1=['1','4','7','9','6','3','5','8','2','9','2','3','7','5','8','6','1','4','5','8','6','1','2','4','3','7','9','2','7','8','4','9','6','1','5','3','4','6','5','8','3','1','2','9','7','3','9','1','2','7','5','8','4','6','7','1','2','6','8','9','4','3','5','6','5','4','3','1','7','9','2','8','8','3','9','5','4','2','7','6','1']
solvedSu2=['1','8','5','2','1','9','6','4','3','7','2','9','4','6','3','5','1','8','6','4','3','8','1','5','7','2','9','3','5','4','9','2','7','8','6','1','9','7','8','6','5','1','2','3','4','2','6','1','3','8','4','9','5','7','8','1','6','7','4','2','3','9','5','4','9','2','5','3','8','1','7','6','5','3','7','1','9','6','4','8','2']
solvedSu3=['1','7','5','3','4','2','6','9','8','9','4','6','7','1','8','2','5','3','8','3','2','5','6','9','4','1','7','4','2','3','1','7','5','9','8','6','7','6','9','4','8','3','1','2','5','5','8','1','9','2','6','7','3','4','6','5','8','2','9','4','3','7','1','2','1','4','8','3','7','5','6','9','3','9','7','6','5','1','8','4','2']
solvedSu4=['4','2','6','8','3','7','9','5','1','9','8','1','5','6','2','4','3','7','5','3','7','9','4','1','8','2','6','8','9','5','2','1','6','3','7','4','7','4','2','3','8','5','6','1','9','1','6','3','7','9','4','5','8','2','6','5','9','1','7','3','2','4','8','3','7','8','4','2','9','1','6','5','2','1','4','6','5','8','7','9','3']
solvedSu5=['2','7','8','5','6','3','4','1','9','1','5','6','2','4','9','3','8','7','3','4','9','1','8','7','2','5','6','4','2','7','8','1','5','9','6','3','8','9','5','6','3','2','7','4','1','6','3','1','9','7','4','5','2','8','9','1','3','4','2','8','6','7','5','7','8','2','3','5','6','1','9','4','5','6','4','7','9','1','8','3','2']
solvedSu6=['9','2','8','4','6','1','3','7','5','5','3','7','2','9','8','6','1','4','4','6','1','5','3','7','8','2','9','7','5','3','6','1','2','4','9','8','1','8','2','9','5','4','7','6','3','6','9','4','7','8','3','2','5','1','8','1','6','3','2','5','9','4','7','2','4','5','8','7','9','1','3','6','3','7','9','1','4','6','5','8','2']
solvedSu7=['1','8','3','5','2','9','6','7','4','4','6','2','7','1','8','3','9','5','9','5','7','6','3','4','8','1','2','5','3','8','1','9','7','4','2','6','2','7','4','8','6','3','1','5','9','6','1','9','2','4','5','7','3','8','7','4','1','9','5','6','2','8','3','8','9','6','3','7','2','5','4','1','3','2','5','4','8','1','9','6','7']
solvedSu8=['2','4','3','6','7','1','9','8','5','5','1','8','2','4','9','7','3','6','6','7','9','5','3','8','1','2','4','9','5','4','7','8','2','6','1','3','7','8','1','4','6','3','5','9','2','3','6','2','9','1','5','8','4','7','8','3','6','1','2','7','4','5','9','1','9','7','3','5','4','2','6','8','4','2','5','8','9','6','3','7','1']
solvedSu9=['8','6','3','5','7','4','2','1','9','9','2','7','1','6','8','3','5','4','4','5','1','3','2','9','7','6','8','7','4','9','2','8','1','5','3','6','3','8','2','4','5','6','1','9','7','6','1','5','7','9','3','8','4','2','5','3','8','6','4','7','9','2','1','1','9','6','8','3','2','4','7','5','2','7','4','9','1','5','6','8','3']
solvedSu10=['1','4','8','2','5','9','7','3','6','3','7','6','4','1','8','2','9','5','5','9','2','6','3','7','1','4','8','6','2','9','1','4','3','8','5','7','7','8','3','9','2','5','6','1','4','4','5','1','7','8','6','3','2','9','8','1','4','5','6','2','9','7','3','2','3','7','8','9','4','5','6','1','9','6','5','3','7','1','4','8','2']

####################################################################################################################################

#RANDOM PUZZLE PRINT

#sudokuChoices=[su1,su2,su3,su4,su5,su6,su7,su8,su9,su10]
sudokuAnswers=[solvedSu1,solvedSu2,solvedSu3,solvedSu4,solvedSu5,solvedSu6,solvedSu7,solvedSu8,solvedSu9,solvedSu10]
rdmNumb=random.randint(1,10)
print(rdmNumb)
chosen = []

for i, line in enumerate(f):
    if i == 0:
        chosen = line


print(chosen)

"""
chosen=sudokuChoices[rdmNumb-1]
chosenKey=sudokuAnswers[rdmNumb-1]
"""

####################################################################################################################################

#PROGRAM
#Equal key
bKey=boldKey(chosen,chosenKey)

#Show puzzle to be solved
boldNum(chosen)
blankSudoku(chosen)

#Answer sudoku
while isComplete(fillSudoku(chosen)) == False:
    isComplete(fillSudoku(chosen))

#Check user solution
isSolved(chosen,bKey)