from own_tools import get_strings

#getBoards
def readBoard(boardText):
    boards = []
    boardBuffer = []
    for row in boardText:
        if len(row) == 0:
            boards.append(boardBuffer.pop())
        else:
            boardBuffer.append(row.split())
    boards.append(boardBuffer)
    return boards

def checkPick(board,pick):
     for row in range(len(board)):
            for col in range(len(board)):
                print(pick)
                if board[row][col] == pick:
                    board[row][col] = '0'
        #[[number.replace(pick, '0') for number in row] for row in board]
      
def picking(boards,picks):
    for pick in picks:
        for board in boards:
            checkPick(board, pick)

boards = readBoard(get_strings("2021/input4_boards.txt"))
picks = list(get_strings("2021/input4_picks.txt")[0].split(','))

picking(boards, picks)
#print(boards)
#print(picks)         