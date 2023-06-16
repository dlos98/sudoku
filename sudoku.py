from puzzlePrint import *
from fillSudoku import *
from solutionCheck import *
import random

####FILES####
#Open and read puzzles file
with open('puzzles.csv', 'r') as f:
    puzzlesLines = f.readlines()

#Open and read answer key file
with open('solvedPuzzles.csv', 'r') as fKey:
    answersLines = fKey.readlines()

####RANDOM PUZZLE SELECTION####
#Chose random number according to number of puzzles saved in file
rdmNumb=random.randint(1,10)

#Hold chosen puzzle from file according to random number
chosen = puzzlesLines[rdmNumb-1]

#Convert chosen puzzle single string to list of strings
chosenList = convertStrToList(chosen)

#Hold puzzle key according to random number
chosenKey = answersLines[rdmNumb-1]

#Convert puzzle key single string to list of strings 
chosenKeyList = convertStrToList(chosenKey)

####PRINTING THE PUZZLE####
#Make non-blank values from new sudoku bold in answer key
#to avoid conflict when comparing to user solution
bKey=boldKey(chosenList,chosenKeyList)

#Make non-blank values from new sudoku bold 
boldNum(chosenList)

#Show sudoku puzzle to user
printSudoku(chosenList)

#Run program until puzzle is completed
while isComplete(fillSudoku(chosenList)) == False:
    isComplete(fillSudoku(chosenList))

#Change solution numbers to string to avoid conflict when comparing to key
for i in range(81):
    if type(chosenList[i]) == int:
        chosenList[i] = str(chosenList[i])

#Check user solution against puzzle key
isSolved(chosenList,bKey)