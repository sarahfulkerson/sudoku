from collections.abc import MutableSequence

import copy, sys

class gcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Grid(MutableSequence):
    def __init__(self, arg):
        self.arg = arg
        self.puzzle = copy.deepcopy(self.arg)
        self.values = [1,2,3,4,5,6,7,8,9,'erase']
    def __delitem__(self, index):
        return self.arg.__delitem__(index)
    def __getitem__(self, index):
        return self.arg.__getitem__(index)
    def __len__(self):
        return self.arg.__len__(self)
    def __setitem__(self, index, value):
        return self.arg.__setitem__(self, index, value)
    def insert(self, index, value):
        return self.arg.insert(index, value)
    def display(self):
        horizontal = '     =====   =====   =====  '
        cols = """     C C C   C C C   C C C  
     1 2 3   4 5 6   7 8 9"""

        print(cols)
        for x in self.puzzle:
            ind = self.puzzle.index(x)
            if ind % 3 == 0:
                print(horizontal)
            print(f"R{ind+1}  |",end='')
            for y in range(len(x)):
                item = self.puzzle[ind][y]
                formatted = ''
                if item == self.arg[ind][y]:
                    formatted = f"{gcolors.OKBLUE}{item}{gcolors.ENDC}"
                    print(formatted,end='|')
                else:
                    formatted = f"{gcolors.WARNING}{item}{gcolors.ENDC}"
                    print(formatted,end='|')
                
                if y % 3 == 2 and y != 8: print(' |',end='')
            print('')
        if ind % 3 == 0:
            print(horizontal)
        print(horizontal)
    def fillbox(self,row,col,val):
        # Validates that the user provided an allowable row
        if int(row) not in self.values[:-1]:
            print(int(row), self.values[:-1])
            print(f"\n{gcolors.FAIL}Error: Not a valid row!{gcolors.ENDC}\n", file=sys.stderr)
            self.display()
            return

        # Validates that the user provided an allowable col
        if int(col) not in self.values[:-1]:
            print(f"\n{gcolors.FAIL}Error: Not a valid column!{gcolors.ENDC}\n", file=sys.stderr)
            self.display()
            return

        rowindex = int(row)-1
        colindex = int(col)-1        

        # Validates that the user provided an allowable value
        if int(val) not in self.values:
            print(f"\n{gcolors.FAIL}Error: Not an allowable value!{gcolors.ENDC}\n", file=sys.stderr)
            self.display()
            return

        # Validates the user input against the original puzzle
        if self.arg[rowindex][colindex] != ' ':
            print(f"\n{gcolors.FAIL}Error: Can't change original puzzle!{gcolors.ENDC}\n", file=sys.stderr)
            self.display()
            return
        
        # Either erase or place a number as requested by the user
        if str(val).lower() == 'erase':
            self.puzzle[rowindex][colindex] = ' '
            print(f"\n{gcolors.OKCYAN}Erased value at R{row}, C{col}\n{gcolors.ENDC}")
        else:
            self.puzzle[rowindex][colindex] = int(val)
            print(f"\n{gcolors.OKCYAN}{val} placed in R{row}, C{col}\n{gcolors.ENDC}")
        self.display()
    def isfull(self):
        # Determine if every box in the grid has a value
        if set(map(lambda x: ' ' in x, self.puzzle)) != {False}: return False
        return True
    def isCorrect(self):
        # Validate each row in self.puzzle; return false if a row does not contain all values
        if self.validate(self.puzzle) == False:
            print('False: Row')
            return False
        
        # Create list of column values in self.puzzle and validate each column
        cols = self.getCols()
        if self.validate(cols) == False: 
            return False

        # Create list of square values in self.puzzle and validate each square
        squares = self.getSquares()
        if self.validate(squares) == False: 
            return False

        # If all validation has passed then you have the solution!
        return True
    def validate(self, item):
        seq = set(self.values[:-1])
        if set(map(lambda row: set(row) == seq,item)) != {True}: 
            print(list(map(lambda row: set(row) == seq,item)))
            return False
        return True
    def getCols(self):
        cols = [[],[],[],[],[],[],[],[],[]]
        for x in range(len(self.puzzle)):
            cols[0].extend([self.puzzle[0][x]])
            cols[1].extend([self.puzzle[1][x]])
            cols[2].extend([self.puzzle[2][x]])
            cols[3].extend([self.puzzle[3][x]])
            cols[4].extend([self.puzzle[4][x]])
            cols[5].extend([self.puzzle[5][x]])
            cols[6].extend([self.puzzle[6][x]])
            cols[7].extend([self.puzzle[7][x]])
            cols[8].extend([self.puzzle[8][x]])
        return cols
    def getSquares(self):
        squares = [[],[],[],[],[],[],[],[],[]]
        place = [0,1,2]
        counter = 0
        for row in self.puzzle:
            squareA, squareB, squareC = row[:3], row[3:6], row[6:]
            squares[place[0]].extend(squareA)
            squares[place[1]].extend(squareB)
            squares[place[2]].extend(squareC)

            if counter % 3 == 2:
                place = [x + 3 for x in place]
            counter += 1
        return squares
    def reset(self):
        self.puzzle = copy.deepcopy(self.arg)