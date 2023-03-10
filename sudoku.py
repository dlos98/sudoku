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
            print(array[i])

#Read position funtion
def readPosition():
    row = input("Enter row number: ")
    col = input("Enter column number: ")
    val = input("Enter desired value: ")
    return row, col,val

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
    else:
        print("The value in this position is unchangable, please select a new position.")

####################################################################################################################################

#PUZZLES

su1=['9',' ' ,'6',' ' ,' ' ,'1',' ' ,'4',' ' ,'7',' ' ,'1','2','9',' ' ,' ' ,'6',' ' ,'4',' ' ,'2','8',' ' ,'6','3',' ' ,' ' ,' ' ,' ' ,' ' ,' ' ,'2',' ' ,'9','8',' ' ,'6',' ' ,' ' ,' ' ,' ' ,' ' ,' ' ,' ' ,'2',' ' ,'9','4',' ' ,'8',' ' ,' ' ,' ' ,' ' ,' ' ,' ' ,'3','7',' ' ,'8','4',' ' ,'9',' ' ,'4',' ' ,' ' ,'1','3','7',' ' ,'6',' ' ,'6',' ' ,'9',' ' ,' ' ,'1',' ' ,'8']
su2=[' ' ,' ' ,' ' ,' ' ,' ' ,'9','6',' ' ,' ' ,'7','2',' ' ,' ' ,'6',' ' ,'5','1',' ' ,' ' ,'4','3','8',' ' ,'5','7','2','9',' ' ,'5',' ' ,' ' ,' ' ,'7','8','6',' ' ,'9','7','8',' ' ,' ' ,' ' ,'2','3','4',' ' ,'6','1','3',' ' ,' ' ,' ' ,'5',' ' ,'8','1','6','7',' ' ,'2','3','9',' ' ,' ' ,'9','2',' ' ,'3',' ' ,' ' ,'7','6',' ' ,' ' ,'7','1',' ' ,' ' ,' ' ,' ' ,' ' ]
su3=[' ' ,'7',' ' ,' ' ,' ' ,' ' ,'6',' ' ,'8','9',' ' ,' ' ,'7',' ' ,'8','2','5','3','8',' ' ,'2',' ' ,'6',' ' ,'4',' ' ,'7','4',' ' ,'3','1','7',' ' ,'9',' ' ,' ' ,'7',' ' ,'9','4',' ' ,'3','1',' ' ,'5',' ' ,' ' ,'1',' ' ,'2','6','7',' ' ,'4','6',' ' ,'8',' ' ,'9',' ' ,'3',' ' ,'1','2','1','4','8',' ' ,'7',' ' ,' ' ,'9','3',' ' ,'7',' ' ,' ' ,' ' ,' ' ,'4','2']
su4=[' ' ,'2',' ' ,'8',' ' ,' ' ,'9',' ' ,' ' ,' ' ,'8','1','5',' ' ,'2',' ' ,'3','7','5',' ' ,' ' ,'9','4','1','8','2','6',' ' ,' ' ,'5',' ' ,'1','6',' ' ,' ' ,' ' ,' ' ,'4','2',' ' ,' ' ,' ' ,'6','1',' ' ,' ' ,' ' ,' ' ,'7','9',' ' ,'5',' ' ,' ' ,'6','5','9','1','7','3',' ' ,' ' ,'8','3','7',' ' ,'4',' ' ,'9','1','6',' ' ,' ' ,' ' ,'4',' ' ,' ' ,'8',' ' ,'9',' ' ]
su5=[' ' ,' ' ,'8','5','6',' ' ,' ' ,' ' ,' ' ,'1','5','6','2','4','9','3',' ' ,'7',' ' ,'4','9','1',' ' ,'7',' ' ,'5','6','4','2',' ' ,' ' ,'1',' ' ,' ' ,' ' ,' ' ,'8','9',' ' ,' ' ,' ' ,' ' ,' ' ,'4','1',' ' ,' ' ,' ' ,' ' ,'7',' ' ,' ' ,'2','8','9','1',' ' ,'4',' ' ,'8','6','7',' ' ,'7',' ' ,'2','3','5','6','1','9',' ' ,' ' ,' ' ,' ' ,' ' ,'9','1','8',' ' ,' ' ]
su6=[' ',' ','8','5','6',' ',' ',' ',' ','1','5','6','2','4','9','3',' ','7',' ','4','9','1',' ','7',' ','5','6','4','2',' ',' ','1',' ',' ',' ',' ','8','9',' ',' ',' ',' ',' ','4','1',' ',' ',' ',' ','7',' ',' ','2','8','9','1',' ','4',' ','8','6','7',' ','7',' ','2','3','5','6','1','9',' ',' ',' ',' ',' ','9','1','8',' ',' ']

####################################################################################################################################

#PUZZLE PRINT

blankSudoku(su1)

####################################################################################################################################

#RANDOM PUZZLE PRINT

sudokuChoices=[su1,su2,su3,su4,su5,su6]
rdmNumb=random.randint(1,7)

print(rdmNumb,sudokuChoices[rdmNumb-1])
chosen=sudokuChoices[rdmNumb-1]
blankSudoku(chosen)

####################################################################################################################################

#TESTS
#Test
readPosition()

#Fill test
fillSudoku(chosen)

#Bold test
boldNum(chosen)
blankSudoku(chosen)

