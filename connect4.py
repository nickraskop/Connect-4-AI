import numpy

ROW_COUNT = 6
COL_COUNT = 7

def createBoard():
    board = numpy.zeros((6,7))
    return board

def dropPiece(board, row, col, piece):
    board[row][col] = piece

def isValidLocation(board, col):
    return board[5][col] == 0

def getNextOpenRow(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def printBoard():
    print(numpy.flip(board, 0))
board = createBoard()
gameOver = False
turn = 0

while not gameOver:
    printBoard()
    # Ask for player 1 input
    if turn % 2 == 0:
        col = int(input("Player 1 make your selection (0-6): "))
        if isValidLocation(board, col):
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 1)
    # Ask for player 2 input
    else:
        col = int(input("Player 2 make your move (0-6): "))
        if isValidLocation(board, col):
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 2)
    turn += 1

