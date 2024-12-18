def getScoreOfBoard(board):
    xScore = sum(row.count("X") for row in board)
    oScore = sum(row.count("O") for row in board)
    return {"X": xScore, "O": oScore}

def printScore(board, playerTile, computerTile):
    scores = getScoreOfBoard(board)
    print(f"Score - You: {scores[playerTile]}, Computer: {scores[computerTile]}")

def playAgain():
    return input("Do you want to play again? (yes or no): ").lower().startswith("y")

