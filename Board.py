def drawBoard(board, valid_moves=[]):
    # Console Output with A-H as X-axis labels
    print("    " + "   ".join(chr(i + 65) for i in range(8)))  # A to H as column labels
    print("   " + "+---" * 8 + "+")  # Adjusted for alignment
    for y in range(8):
        row_str = f"{y + 1:2} |"  # Row numbers (Y-axis) aligned
        for x in range(8):
            if [x, y] in valid_moves:
                row_str += " * |"  # Mark valid moves with an asterisk
            else:
                row_str += f" {board[x][y]} |"
        print(row_str)
        print("   " + "+---" * 8 + "+")  # Adjusted for alignment

def resetBoard(board):
    for x in range(8):
        for y in range(8):
            board[x][y] = " "
    board[3][3], board[3][4] = "X", "O"
    board[4][3], board[4][4] = "O", "X"

def getNewBoard():
    return [[" " for _ in range(8)] for _ in range(8)]