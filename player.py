import random
from move import getValidMoves

def whoGoesFirst():
    return "computer" if random.randint(0, 1) == 0 else "player"

def getComputerMove(board, computerTile):
    validMoves = getValidMoves(board, computerTile)
    return random.choice(validMoves) if validMoves else None


