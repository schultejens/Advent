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
    for pick in picks:
        for board in boards:
            checkPick(board, pick)
            if(checkWin(board) is not None):
                return board, pick
                               
boards = readBoard(get_strings("2021/input4_boards.txt"))
picks = list(map(int,get_strings("2021/input4_picks.txt")[0].split(',')))

winningboard = picking(boards, picks)
print(np.sum(winningboard[0])*winningboard[1])    