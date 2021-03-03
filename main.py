#! /usr/bin/env python3
"""
A fully playable game of sudoku written in python!
"""
from lib import Grid

def main():
    easy =  [   [' ',7,9,8,' ',2,' ',6,3],
                [6,' ',' ',9,' ',' ',' ',1,' '],
                [8,' ',3,' ',7,' ',' ',' ',2],
                [' ',9,' ',' ',' ',' ',3,7,1],
                [' ',6,8,7,' ',' ',' ',9,' '],
                [' ',3,1,' ',2,' ',5,8,' '],
                [2,8,6,5,' ',' ',1,3,' '],
                [' ',' ',' ',' ',' ',' ',' ',' ',' '],
                [9,' ',4,3,' ',' ',8,2,7]]
    grid = Grid(easy)
    grid.display()
    
    while True:
        if grid.isfull() == True: break
        print("Row, Col, value: ")
        row = input()
        col = input()
        val = input()
        grid.fillbox(row,col,val)

main()