import numpy

def createBoard():
    board = numpy.zeros((6,7))
    return board

board = createBoard()
gameOver = False
turn = 0

print(board)

while not gameOver:
    # Ask for player 1 input
    if turn % 2 == 0:
        selection = int(input("Player 1 make your selection (0-6): "))
    # Ask for player 2 input
    else:
        selection = int(input("Player 2 make your move (0-6): "))
    turn += 1

