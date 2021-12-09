from numpy.lib.function_base import append
from own_tools import get_strings
import numpy as np
import sys
sys.setrecursionlimit(5000)

offset = [(-1,0),(0,-1),(0,1),(1,0)]   

with open('2021/input9.txt') as f:
    inputlist = f.readlines()
inputlist = np.array(list(map(int,(map(lambda s: s.strip(), inputlist)))))

nIter = list(set())

def checkNeighbour(board, row, collumn):
    neighbours = []
    #print('currentPick: @ (',collumn,' | ',row,')')
    for offsets in offset:
        if 0 <= row+offsets[1] <= len(board)-1 and 0 <= collumn+offsets[0] <= len(board[0])-1:
            #print(offsets[0])
            newX = collumn+offsets[0]
            newY = row+offsets[1]
            #print('newX',newX)
            #print('newY',newY)
            if board[newY][newX] != 9:
                neighbours.append([board[newY][newX], newY, newX])
    #print('allNeighbours ',neighbours)
    if len(neighbours) != 0:
        newneighbours = []
        for n in neighbours:
                #print(n[2],'%',n[1])
                if n not in nIter:
                    print('recursion start')
                    nIter.append(n)
                    checkNeighbour(board,n[2], n[1])
                    print('recursion end')
                
        print('stop',newneighbours)        
        return newneighbours

def iterateBoard(inputlist):
    #candidates= []
    for row in range(0,len(inputlist)):
        for collumn in range(0,len(inputlist[0])):
            #candidates.append(checkNeighbour(inputlist,row,collumn))  
            checkNeighbour(inputlist,row,collumn)
            print(len(nIter))   
    #print(sum([i for i in candidates if i] ))
    

inputArray = []
for row in inputlist:
    inputArray.append(list(map(int, str(row))))
inputlist = np.array(inputArray)    

iterateBoard(inputlist)