from puzzlePrint import *
from fillSudoku import *
from solutionCheck import *
import random

#open and read files
with open('puzzles.csv', 'r') as f:
    puzzlesLines = f.readlines()

with open('solvedPuzzles.csv', 'r') as fKey:
    answersLines = fKey.readlines()

#Chose random number to choose puzzle to be played
rdmNumb=random.randint(1,10)
chosen = puzzlesLines[rdmNumb-1]
chosenList = convertStrToList(chosen)
chosenKey = answersLines[rdmNumb-1]
chosenKeyList = convertStrToList(chosenKey)

#Print the puzzle and bolden predetermined numbers
bKey=boldKey(chosenList,chosenKeyList)
boldNum(chosenList)
printSudoku(chosenList)

#Check puzzle completion
while isComplete(fillSudoku(chosenList)) == False:
    isComplete(fillSudoku(chosenList))

for i in range(81):
    if type(chosenList[i]) == int:
        chosenList[i] = str(chosenList[i])
 
 #Check solution
isSolved(chosenList,bKey)