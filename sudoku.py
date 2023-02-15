
sudoku1=[9,0,6,0,0,1,0,4,0,7,0,1,2,9,0,0,6,0,4,0,2,8,0,6,3,0,0,0,0,0,0,2,0,9,8,0,6,0,0,0,0,0,0,0,2,0,9,4,0,8,0,0,0,0,0,0,3,7,0,8,4,0,9,0,4,0,0,1,3,7,0,6,0,6,0,9,0,0,1,0,8]



def blankSudoku():
    count=0
    for row in range(9):
        for column in range(9):
            print(sudoku1[column+count],' ', end=" ")
        print()
        count=count+9

blankSudoku()