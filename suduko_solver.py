"""
Suduko solver with recursive backtraking
(Algorith Only)

by @Fraol G.
    Email:fraolgela@gmail.com
    Tel: +251-920-36-42-95

"""

import numpy as np

class SudukoSolver:

    def __init__(self,board):
        
        self.board = board

    def __str__(self):
        return str(np.matrix(self.board))

    def isEmpty(self,y,x):
        ## Check if a cell is Empty(0)
        return self.board[y][x] == 0 
        
    def isValid(self,y,x,number):
        ## Check if the number doesn't exist along the X-axis (Columns)
        ## self.board[row][i]

        for i in range(len(self.board)):
            if self.board[y][i] == number:
                return False

        ## Check if the number doesn't exist along the Y-axis (rows)
        ## self.board[i][column]

        for i in range(len(self.board)):
            if self.board[i][x] == number:
                return False

        ## Check if the numbers doesn't exist inside 3x3  matrix

        x0 = (x // 3) * 3
        y0 = (y // 3) * 3

        for i in range(3):
            for j in range(3):
                if self.board[y0+i][x0+j] == number:
                    return False

        ##### Return true Otherwise
        return True

    def solve(self):
        for y in range(0,9):
            for x in range(0,9):
                if self.isEmpty(y,x):
                    for num in range(1,10):
                        if self.isValid(y,x,num):
                            self.board[y][x] = num
                            if self.solve():
                                return True
                            self.board[y][x] = 0
                    return False

        return True
       
if __name__ == "__main__":

    myboard =  [[8, 1, 0, 0, 3, 0, 0, 2, 7], 
              [0, 6, 2, 0, 5, 0, 0, 9, 0], 
              [0, 7, 0, 0, 0, 0, 0, 0, 0], 
              [0, 9, 0, 6, 0, 0, 1, 0, 0], 
              [1, 0, 0, 0, 2, 0, 0, 0, 4], 
              [0, 0, 8, 0, 0, 5, 0, 7, 0], 
              [0, 0, 0, 0, 0, 0, 0, 8, 0], 
              [0, 2, 0, 0, 1, 0, 7, 5, 0], 
              [3, 8, 0, 0, 7, 0, 0, 4, 2]]

    solver = SudukoSolver(myboard)

    print(solver)
    
    if solver.solve():
        print("-----------SOLUTION---------------",end="\n")
        print(np.matrix(solver.board))    
        
       