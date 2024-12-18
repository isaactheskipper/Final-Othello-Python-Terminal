def isValidMove(board, tile, xstart, ystart):
    if board[xstart][ystart] != " " or not isOnBoard(xstart, ystart):
        return False

    otherTile = "O" if tile == "X" else "X"
    tilesToFlip = []

    for xdir, ydir in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
        x, y = xstart + xdir, ystart + ydir
        while isOnBoard(x, y) and board[x][y] == otherTile:
            x, y = x + xdir, y + ydir
        if isOnBoard(x, y) and board[x][y] == tile:
            while True:
                x -= xdir
                y -= ydir
                if x == xstart and y == ystart:
                    break
                tilesToFlip.append([x, y])

    return tilesToFlip if tilesToFlip else False

def isOnBoard(x, y):
    return 0 <= x <= 7 and 0 <= y <= 7

def getValidMoves(board, tile):
    validMoves = []
    for x in range(8):
        for y in range(8):
            if isValidMove(board, tile, x, y):
                validMoves.append([x, y])
    return validMoves

def makeMove(board, tile, xstart, ystart):
    tilesToFlip = isValidMove(board, tile, xstart, ystart)
    if not tilesToFlip:
        return False
    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def enterPlayerTile():
    tile = ""
    while tile not in ("X", "O"):
        tile = input("Do you want to be X or O? ").upper()
    return ["X", "O"] if tile == "X" else ["O", "X"]

def getPlayerMove(board, playerTile):
    digits = "A B C D E F G H".split()  # Changed to letter columns (A-H)
    while True:
        print("Enter your move, or type 'quit' to end the game.")
        move = input().lower()
        if move == "quit":
            return "quit"
        if move == "hints":
            return "hints"
        if len(move) == 2 and move[0].upper() in digits and move[1] in "12345678":
            x = ord(move[0].upper()) - 65  # Convert letter (A-H) to column index (0-7)
            y = int(move[1]) - 1  # Convert number to row index (0-7)
            if isValidMove(board, playerTile, x, y):
                return [x, y]
        print("Invalid move. Enter column (A-H) and row (1-8).")

def getBoardCopy(board):
    return [row[:] for row in board]
