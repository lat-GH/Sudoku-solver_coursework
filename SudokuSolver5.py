
from SudokuState5 import SudokuSate5
import time
import numpy as np

#finds the next position to try on the grid with the least number of unknonw values
def find_next_unknown(hieght,width, poss_Vs):
    smallest = 9
    pos = [-1,-1]
    for n in range(hieght):
        for m in range(width):
            if len(poss_Vs[n][m]) < smallest and len(poss_Vs[n][m])>0:
                smallest = len(poss_Vs[n][m])
                pos = [n,m]
    return pos

"""def find_next_unknown2(poss_Vs, unknowns):
    smallest = 9
    pos = [-1,-1]
    for pos in unknowns:
        n = pos[0]
        m = pos[1]
        if len(poss_Vs[n][m]) < smallest :
            smallest = len(poss_Vs[n][m])
            pos = [n,m]
    return pos"""

def depthFirst_Search (oldGrid, possibleValues, unknown_positions):

    currState = SudokuSate5(oldGrid, possibleValues, unknown_positions)
    if currState.is_invalid2() == True:
        return None

    position = find_next_unknown(currState.gh, currState.gw, currState.possibleVals)
    if position == [-1,-1]:
        if not currState.is_invalid2():
            return currState
        else:
            return None

    poss_vals = currState.get_possibleVals(position[0],position[1])
    #newState = SudokuSate5(currState.get_grid(), currState.get_ALlpossibleVals(), currState.get_unknonws())

    for v in poss_vals:
        #newState = SudokuSate5(currState.get_grid(), None, None)
        #newState = SudokuSate5(currState.get_grid(), currState.get_ALlpossibleVals(), currState.get_unknonws())
        newState = SudokuSate5(currState.get_grid(), possibleValues, unknown_positions)
        newState.set_value2(int(position[0]), int(position[1]), v)

        if newState.is_goal():
            return newState
        if not newState.is_invalid2():
            consequenceState = depthFirst_Search(newState.get_grid(), newState.possibleVals, newState.unknown_pos)
            if (consequenceState is not None) and (consequenceState.is_goal()):
                return consequenceState

    return None

#grid = np.load("C:/Users/latma/OneDrive/Documents/ComputerScience_Yr2/AI/sudoku/data/very_easy_puzzle.npy")
#solutions = np.load("C:/Users/latma/OneDrive/Documents/ComputerScience_Yr2/AI/sudoku/data/very_easy_solution.npy")

#grid = np.load("C:/Users/latma/OneDrive/Documents/ComputerScience_Yr2/AI/sudoku/data/easy_puzzle.npy")
#solutions = np.load("C:/Users/latma/OneDrive/Documents/ComputerScience_Yr2/AI/sudoku/data/easy_solution.npy")

#grid = np.load("C:/Users/latma/OneDrive/Documents/ComputerScience_Yr2/AI/sudoku/data/medium_puzzle.npy")
#solutions = np.load("C:/Users/latma/OneDrive/Documents/ComputerScience_Yr2/AI/sudoku/data/medium_solution.npy")

"""grid = np.load("C:/Users/latma/OneDrive/Documents/ComputerScience_Yr2/AI/sudoku/data/hard_puzzle.npy")
solutions = np.load("C:/Users/latma/OneDrive/Documents/ComputerScience_Yr2/AI/sudoku/data/hard_solution.npy")
g = 0

#print("original: \n", grid[g])
#print("actual: \n",solutions[g])

mySolution = depthFirst_Search(grid[g], None, None)"""
grid = np.array([[3,8, 4, 1, 7, 0, 5, 9, 2],
 [6, 7, 5, 2, 3, 0, 8, 4, 1],
 [1, 9, 2, 8, 4, 5, 3, 7, 6],
 [8, 2, 6, 4, 9, 7, 1, 5, 3],
 [7, 5, 1, 6, 8, 3, 9, 2, 4],
 [1, 4, 3, 0, 1, 2, 7, 6, 8],
 [2, 6, 9, 3, 5, 8, 4, 1, 7],
 [0, 1, 8, 7, 2, 4, 6, 3, 9],
 [0, 3, 7, 9, 6, 1, 2, 8, 5]])

mySolution = depthFirst_Search(grid, None, None)
if mySolution != None:
    mySolution = mySolution.get_grid()
else:
    mySolution = [ [-1] * 9 for _ in range(9)]

#print("original: \n", grid[g])
print("original: \n", grid)
print("solution: \n", mySolution)
#print("actual: \n",solutions[g])



test = SudokuSate5(grid, None, None)
print("correctGrid: ",test.correctGrid())
print("is_invalid2: ", test.is_invalid2())
"""

for i in range(15):
    g=i
    startTime = time.time()
    mySolution = depthFirst_Search(grid[g],None,None)
    executionTime = time.time() - startTime
    print(executionTime)
    if mySolution != None:
        mySolution = mySolution.get_grid()
    else:
        broke = [[-1] * 9 for _ in range(9)]
        mySolution = np.asarray(broke)
        #print("broke\n",grid[g])

    #if solutions[g].all() == mySolution.all():
    if (solutions[g]==mySolution).all():
        print("correct solution = True")
    else:
        print("correct solution = False")
        print("original: \n", grid[g])
        print("solution: \n", mySolution)
        print("actual: \n", solutions[g])
"""