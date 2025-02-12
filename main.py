#! /usr/bin/env python3
"""
A fully playable game of sudoku written in python!
"""
from lib import Grid, gcolors

import shelve, sys

helpString = """
How to play:

- Type 'help' for game instructions.
- Type 'reset' to erase all squares on the board.
- Type 'save' to save your current progress.
- Type 'quit' to quit (will automatically save your progress).
- To fill in a box, type the row number, column number, and value separated by commas.
- To erase a previously filled in box, type 'erase' in place of a value.
"""
def saveGrid(grid,dbName,gridName):
    db = shelve.open(dbName)
    db[gridName] = grid
    db.close()           
    print(f"\n{gcolors.OKCYAN}Grid has been saved!{gcolors.ENDC}\n")
def main():
    """easy =  [   [' ',7,9,8,' ',2,' ',6,3],
                [6,' ',' ',9,' ',' ',' ',1,' '],
                [8,' ',3,' ',7,' ',' ',' ',2],
                [' ',9,' ',' ',' ',' ',3,7,1],
                [' ',6,8,7,' ',' ',' ',9,' '],
                [' ',3,1,' ',2,' ',5,8,' '],
                [2,8,6,5,' ',' ',1,3,' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [9,' ',4,3,' ',' ',8,2,7]]"""
    """easy2 =  [[' ',' ',7,1,5,4,3,9,6],
                [9,6,5,3,2,7,1,4,8],
                [3,4,1,6,8,9,7,5,2],
                [5,9,3,4,6,8,2,7,1],
                [4,7,2,5,1,3,6,8,9],
                [6,1,8,9,7,2,4,3,5],
                [7,8,6,2,3,5,9,1,4],
                [1,5,4,7,9,6,8,2,3],
                [2,3,9,8,4,1,5,6,7]]"""
    dbName = 'appDB'
    gridName = 'currentGridV3'

    db = shelve.open(dbName)
    grid = db[gridName]
    db.close()
    
    print('\n%s\n%s' % ("Welcome to Sudoku by Sarah!",helpString))
    grid.display()

    while True:
        if grid.isfull() == True: 
            if grid.isCorrect() == True:
                print(f"\n{gcolors.OKCYAN}YAY YOU DID IT!{gcolors.ENDC}\n")
            else:
                print(f"\n{gcolors.FAIL}Oh no! Something's wrong!{gcolors.ENDC}\n", file=sys.stderr)
        text = str(input("\nRow, Col, value: ")).lower()
        if text == 'quit':
            saveGrid(grid,dbName,gridName)
            print(f"\n{gcolors.OKCYAN}See ya!{gcolors.ENDC}\n")
            break
        if text == 'save':
            saveGrid(grid,dbName,gridName)
            grid.display()
            continue
        if text == 'help':
            print(helpString)
            grid.display()
            continue
        if text == 'reset':
            grid.reset()
            grid.display()
            continue
        
        try:
            row, col, val = [x.lstrip().rstrip() for x in text.split(sep=',')]
        except ValueError:
            continue
        
        grid.fillbox(row,col,val)   # This will fail with a ValueError if not properly handling inputs in lib.py
        grid.display()

main()