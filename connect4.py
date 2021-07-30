import numpy

ROW_COUNT = 6
COL_COUNT = 7

def createBoard():
    board = numpy.zeros((ROW_COUNT,COL_COUNT))
    return board

def dropPiece(board, row, col, piece):
    board[row][col] = piece

def isValidLocation(board, col):
    return board[ROW_COUNT - 1][col] == 0

def getNextOpenRow(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def printBoard():
    print(numpy.flip(board, 0))
board = createBoard()
gameOver = False
turn = 0

def winningMove(board, piece):
    # Check horizontal locations for win
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    # Check vertical locations for win


while not gameOver:
    printBoard()
    # Ask for player 1 input
    if turn % 2 == 0:
        col = int(input("Player 1 make your selection (0-6): "))
        if isValidLocation(board, col):
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 1)
            if winningMove(board, 1):
                print("PLAYER 1 WINS")
                gameOver = True
    # Ask for player 2 input
    else:
        col = int(input("Player 2 make your move (0-6): "))
        if isValidLocation(board, col):
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 2)
            if winningMove(board, 2):
                print("PLAYER 2 WINS")
                gameOver = True
    turn += 1

