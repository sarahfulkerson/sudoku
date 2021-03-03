from collections.abc import MutableSequence

import copy, sys

class Grid(MutableSequence):
    def __init__(self, arg):
        self.arg = arg
        self.puzzle = copy.deepcopy(self.arg)
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
            row = 'R%s ||%s|%s|%s| |%s|%s|%s| |%s|%s|%s||' % (ind+1,x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],)
            if ind % 3 == 0:
                print(horizontal)
            print(row)

        print(horizontal)
    def fillbox(self,row,col,val):
        rowindex = int(row)-1
        colindex = int(col)-1
        values = ['1','2','3','4','5','6','7','8','9','erase']

        # Validates that the user provided an allowable value
        if str(val) not in values:
            print("Error: Not an allowable value!\n", file=sys.stderr)
            self.display()
            return

        # Validates the user input against the original puzzle
        if self.arg[rowindex][colindex] != ' ':
            print("Error: Can't change original puzzle!\n", file=sys.stderr)
            self.display()
            return
        
        # Either erase or place a number as requested by the user
        if str(val).lower() == 'erase':
            self.puzzle[rowindex][colindex] = ' '
            print("Erased value at R%s, C%s\n" % (row,col))
        else:
            self.puzzle[rowindex][colindex] = val
            print("%s placed in R%s, C%s\n" % (val,row,col))
        self.display()
    def isfull(self):
        for x in self.puzzle:
            for y in x:
                if y == ' ':
                    return False
        return True