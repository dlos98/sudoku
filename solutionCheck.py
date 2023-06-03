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