from puzzlePrint import *
from fillSudoku import *
from solutionCheck import *
import random

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
printSudoku(chosenList)

boldNum(chosen)
printSudoku(chosen)

#Answer sudoku
while isComplete(fillSudoku(chosen)) == False:
    isComplete(fillSudoku(chosen))

#Change solution to String
for i in range(81):
    if type(chosen[i]) == int:
        chosen[i] = str(chosen[i])

#Check user solution
isSolved(chosenList,bKey)