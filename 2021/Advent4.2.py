from own_tools import get_strings
import numpy as np

def readBoard(boardText):
    boards = []
    boardBuffer = []
    for row in boardText:
        if len(row) == 0:
            boards.append(boardBuffer)
            boardBuffer = []
        else:
            boardBuffer.append(list(map(int,row.split())))
    return boards

def checkPick(board,pick):
    for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == pick:
                   board[row][col] = 0
    return board
      
def checkRowWin(board):
    numpyArray = np.array(board)
    return min(np.sum(numpyArray, axis=1))==0

    
def checkColWin(board):
    numpyArray = np.array(board)
    return min(np.sum(numpyArray, axis=0)) == 0

def checkWin(board):
    if(checkRowWin(board)):
        return board
    if(checkColWin(board)):
        return board
    return None



                      
def picking(boards,picks):
    winningBoard= []  
    amountOfBoards=len(boards)
    for pick in picks:
        #print(pick)
        tempBoard=[]
        
        for board in boards:
            tempBoard.append(checkPick(board, pick))
        
        for i in reversed(range(len(tempBoard))):
            thisBoard = tempBoard[i]        
            if(checkWin(thisBoard) is not None):
                print('1996')
                winningBoard.append(thisBoard)
                del thisBoard
            if(len(winningBoard) == amountOfBoards):
                return winningBoard.pop(),pick   
        tempboard = []
    print(winningBoard)    
                
                               
boardRead = readBoard(get_strings("2021/input4_boards.txt"))
pickRead = list(map(int,get_strings("2021/input4_picks.txt")[0].split(',')))

winningBoard = picking(boardRead, pickRead)
#print(winningBoard[0],'pick: ',winningBoard[1])
print("npsum:",np.sum(winningBoard[0]),'result: ',np.sum(winningBoard[0])*winningBoard[1])    
#2634