#Check puzzle completion
def isComplete(sol):
    """This function is to know if the puzzle is completely answered.
    The whole list is checked and if a space (' ') is found "False" is returned.
    This indicated the puzzle is not complete because it has blank spaces.

    Args:
        sol (list): List that has the user's inputs

    Returns:
        boolean: Indicates weather the puzzle is complete or not.
    """

    for i in range(81):
        if sol[i] == ' ':
            return False

#Solution check
def isSolved(filled, key):
    """This function is to know if the solution given by the user is the correct answer.
    One by one the value from the user's solution is compared to the key, if all values match,
    the solution is correct and a congratulatiory message is displayed.
    If 1 value is different for the key a message is displayed to let the user know their solution is incorrect.

    Args:
        filled (list): List of the user's solution to the puzzle.
        key (list): List of the answer key corresponding to the puzzle being solved.
    """

    isSol = True
    for i in range(81):
        if filled[i] != key[i]:
            isSol = False
    if isSol == False:
        print('Sorry, the solution is incorrect. Try again')
    else:
        print('Congratulations!')     