from numpy.lib.function_base import append
from own_tools import get_strings
import numpy as np

offset = [(-1,0),(0,-1),(0,1),(1,0)]   

with open('2021/input9.txt') as f:
    inputlist = f.readlines()
inputlist = np.array(list(map(int,(map(lambda s: s.strip(), inputlist)))))

def checkNeighbour(board, row, collumn):
    neighbours = []
    for offsets in offset:
        if 0 <= row+offsets[1] <= len(board)-1 and 0 <= collumn+offsets[0] <= len(board[0])-1:
             neighbours.append(board[row+offsets[1]][collumn+offsets[0]])
    if min(neighbours) > board[row][collumn]:
        return board[row][collumn]+1

def iterateBoard(inputlist):
    candidates= []
    for row in range(0,len(inputlist)):
        for collumn in range(0,len(inputlist[0])):
            candidates.append(checkNeighbour(inputlist,row,collumn))     
    print(sum([i for i in candidates if i] ))

inputArray = []
for row in inputlist:
    inputArray.append(list(map(int, str(row))))
inputlist = np.array(inputArray)    

iterateBoard(inputlist)