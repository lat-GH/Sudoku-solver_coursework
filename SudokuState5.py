import collections

import numpy as np
import copy

class SudokuSate5:

    def __init__(self, original_grid,possibleValues, unknown_positions):
        self.grid = copy.deepcopy(original_grid)
        dimensions = self.grid.shape
        self.gh = dimensions[0]
        self.gw = dimensions[1]

        #only recalculates the grid if None is passed, otherwise it will use the same values that are passed in
        if possibleValues == None:
            static_possibleVals = np.empty([self.gh, self.gw, 9])
            static_possibleVals.fill(-1)
            self.possibleVals = static_possibleVals.tolist()
            self.unknown_pos = []
            self.calc_AllPossibles()
        else:
            self.possibleVals = copy.deepcopy(possibleValues)
            self.unknown_pos = copy.deepcopy(unknown_positions)

    #calcultes all the possible values for a given grid
    def calc_AllPossibles(self):
        for i in range(self.gh):
            for j in range(self.gw):
                if self.grid[i][j] == 0:
                    self.possibleVals[i][j] = self.calc_PossibleVals(i, j, self.grid)
                    self.unknown_pos.append([i,j])
                else:
                    self.possibleVals[i][j] = []

    #calcultes the possible values after setting a new value,
    #so only alters the row col and square it affceted
    def calc_PossibleVals(self, x,y,grid):
        p = [1,2,3,4,5,6,7,8,9]
        #removing from the row
        for j in range(self.gw):
            if grid[x][j] in p:
                p.remove(grid[x][j])
        #removing from the column
        for i in range(self.gh):
            if grid[i][y] in p:
                p.remove(grid[i][y])

        s = 3 #sqaure size, 3 by 3 for a 9x9
        x_offset = s * (x//s)
        y_offset = s * (y // s)
        for i in range(s):
            for j in range(s):
                if grid[i+x_offset][j+y_offset] in p:
                    p.remove(grid[i+x_offset][j+y_offset])
        return p

    #once has set a value this is called to tidy up the possible values
    def remove_possibles(self,x,y,val):
        for j in range(self.gw):
            if val in self.possibleVals[x][j]:
                self.possibleVals[x][j].remove(val)
        for i in range(self.gh):
            if val in self.possibleVals[i][y]:
                self.possibleVals[i][y].remove(val)
        #square ise = s
        s = 3
        x_offset = s * (x//s)
        y_offset = s * (y // s)
        for i in range(s):
            for j in range(s):
                if val in self.possibleVals[i+x_offset][j+y_offset]:
                    self.possibleVals[i + x_offset][j + y_offset].remove(val)

    #automatiocaly assigns any values that only have one possible value
    def fix_Singletons(self):
        for i in range(self.gh):
            for j in range(self.gw):
                if len(self.possibleVals[i][j]) == 1:
                    self.set_value(i,j,self.possibleVals[i][j][0])

    #sets the value in the grid based on its possible values
    def set_value(self, i, j, val):
        #assigning the value
        self.grid[i][j] = val
        self.possibleVals[i][j] = []
        try:
            self.unknown_pos.remove([i,j])
        except:
            print("You just set a value that wasn't unknonw... need to fix code")

        self.remove_possibles(i,j,val)

    #call this when want to set a value AND sort out any singletons
    def set_value2(self, x, y, val):
        self.set_value(x,y,val)
        self.fix_Singletons()

    #checks if the state is invalid or not
    def is_invalid(self):
        for pos in self.unknown_pos:
            if len(self.possibleVals[pos[0]][pos[1]]) == 0:
                return True
        return False

    # checks if the state is invalid or not
    def is_invalid2(self):
        for pos in self.unknown_pos:
            if len(self.possibleVals[pos[0]][pos[1]]) == 0:
                return True
        for row in self.grid:
            counts = collections.Counter(row)
            for x in range(1,9):
                if counts[x] > 1:
                    return True
        return False

    #checks the grid if it contains the value x
    def gridContains(self, x):
        for i in range(self.gh):
            if x in self.grid[i]:
                return True
        return False

    #checks if you have every number in every row
    def correctGrid(self):
        nums = np.arange(1,9)
        nums = nums.tolist()
        for i in range(self.gh):
            for j in range(self.gw):
                if self.grid[i][j] in nums:
                    nums.remove(self.grid[i][j])
            #checks each row to make sure that it only has one of each value, if not then not a corrrect grid
            if len(nums) == 0:
                nums = np.arange(1,9)
                nums = nums.tolist()
            else:
                return False
        return True

    #checks if grid is solved
    def is_goal(self):
        if(len(self.unknown_pos) == 0) and (self.gridContains(0)==False):
            if self.correctGrid():
                return True
        else:
            return False

    #getters-----
    def get_possibleVals(self, x,y):
        return self.possibleVals[x][y]

    def get_ALlpossibleVals(self):
        return self.possibleVals

    def get_grid(self):
        return self.grid

    def get_unknonws(self):
        return self.unknown_pos
