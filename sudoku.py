import random
import numpy
from numpy import *

#Matrix sudoku
sudoku1=[[9,0,6,0,0,1,0,4,0],[7,0,1,2,9,0,0,6,0],[4,0,2,8,0,6,3,0,0],[0,0,0,0,2,0,9,8,0],[6,0,0,0,0,0,0,0,2],[0,9,4,0,8,0,0,0,0],[0,0,3,7,0,8,4,0,9],[0,4,0,0,1,3,7,0,6],[0,6,0,9,0,0,1,0,8]]
sudoku2=[[0,0,0,0,0,9,6,0,0],[7,2,0,0,6,0,5,1,0],[0,4,3,8,0,5,7,2,9],[0,5,0,0,0,7,8,6,0],[9,7,8,0,0,0,2,3,4],[0,6,1,3,0,0,0,5,0],[8,1,6,7,0,2,3,9,0],[0,9,2,0,3,0,0,7,6],[0,0,7,1,0,0,0,0,0]]
sudoku3=[[0,7,0,0,0,0,6,0,8],[9,0,0,7,0,8,2,5,3],[8,0,2,0,6,0,4,0,7],[4,0,3,1,7,0,9,0,0],[7,0,9,4,0,3,1,0,5],[0,0,1,0,2,6,7,0,4],[6,0,8,0,9,0,3,0,1],[2,1,4,8,0,7,0,0,9],[3,0,7,0,0,0,0,4,2]]
sudoku4=[[0,2,0,8,0,0,9,0,0],[0,8,1,5,0,2,0,3,7],[5,0,0,9,4,1,8,2,6],[0,0,5,0,1,6,0,0,0],[0,4,2,0,0,0,6,1,0],[0,0,0,7,9,0,5,0,0],[6,5,9,1,7,3,0,0,8],[3,7,0,4,0,9,1,6,0],[0,0,4,0,0,8,0,9,0]]
sudoku5=[[0,0,8,5,6,0,0,0,0],[1,5,6,2,4,9,3,0,7],[0,4,9,1,0,7,0,5,6],[4,2,0,0,1,0,0,0,0],[8,9,0,0,0,0,0,4,1],[0,0,0,0,7,0,0,2,8],[9,1,0,4,0,8,6,7,0],[7,0,2,3,5,6,1,9,0],[0,0,0,0,9,1,8,0,0]]

for i in range(9):
    print(sudoku1[i])

#Array sudoku
su1=[9,0,6,0,0,1,0,4,0,7,0,1,2,9,0,0,6,0,4,0,2,8,0,6,3,0,0,0,0,0,0,2,0,9,8,0,6,0,0,0,0,0,0,0,2,0,9,4,0,8,0,0,0,0,0,0,3,7,0,8,4,0,9,0,4,0,0,1,3,7,0,6,0,6,0,9,0,0,1,0,8]

def blankSudoku():
    count=0
    print("------------------------------------")
    for row in range(9):
        for column in range(9):
            print(su1[column+count],"|", end=" ")
        print()
        print("------------------------------------")
        count=count+9

blankSudoku()