import sys
from board import drawBoard, resetBoard, getNewBoard
from move import enterPlayerTile, getPlayerMove, getValidMoves, makeMove
from player import getComputerMove, whoGoesFirst
from score import getScoreOfBoard, printScore, playAgain  # Corrected import

def main():
    print("Welcome to Othello!") 
    print("""
         ___         ___                    ___         ___         ___                
        /  /\       /  /\        ___       /  /\       /  /\       /  /\      ___      
       /  /::\     /  /:/_      /__/\     /  /:/_     /  /::\     /  /:/_    /  /\     
      /  /:/\:\   /  /:/ /\     \  \:\   /  /:/ /\   /  /:/\:\   /  /:/ /\  /  /:/     
     /  /:/~/:/  /  /:/ /:/_     \  \:\ /  /:/ /:/_ /  /:/~/:/  /  /:/ /::\/__/::\     
    /__/:/ /:/__/__/:/ /:/ /\ ___  \__\:/__/:/ /:/ //__/:/ /:/__/__/:/ /:/\:\__\/\:\__  
     \  \:\/:::::\  \:\/:/ /:/__/\ |  |:\  \:\/:/ /:\  \:\/:::::\  \:\/:/~/:/  \  \:\/\\
      \  \::/~~~~ \  \::/ /:/\  \:\|  |:|\  \::/ /:/ \  \::/~~~~ \  \::/ /:/    \__\::/ 
       \  \:\      \  \:\/:/  \  \:\__|:| \  \:\/:/   \  \:\       \  \:\/:/      /__/:/  
        \  \:\      \  \::/    \__\::::/   \  \::/     \  \:\       \__\/       \__\/   
         \__\/       \__\/         @GWETHE     \__\/       \__\/                          
        """)

    print("In this game, you'll take turns placing pieces on the board.")
    print("The goal is to have the most pieces of your color on the board at the end of the game.")
    print("For example, A1 or C3.")
    print("You can play as 'X' or 'O'.")
    print("The board is 8x8, and you'll input your move as a letter (A-H) and a number (1-8).")
    print("Good luck!")

    while True:
        mainBoard = getNewBoard()
        resetBoard(mainBoard)
        playerTile, computerTile = enterPlayerTile()
        turn = whoGoesFirst()

        showHints = False

        while True:
            if turn == "player":
                valid_moves = getValidMoves(mainBoard, playerTile)

                if not valid_moves:
                    break

                drawBoard(mainBoard, valid_moves)

                move = getPlayerMove(mainBoard, playerTile)

                if move == "quit":
                    print("Thanks for playing!")
                    sys.exit()

                if move == "hints":
                    showHints = not showHints
                    continue

                if isinstance(move, list) and len(move) == 2:
                    makeMove(mainBoard, playerTile, move[0], move[1])

                turn = "computer"

            else:
                move = getComputerMove(mainBoard, computerTile)
                if move is None:
                    print("No valid moves for the computer. Skipping turn.")
                    turn = "player"
                else:
                    makeMove(mainBoard, computerTile, move[0], move[1])
                    turn = "player"

        drawBoard(mainBoard)

        scores = getScoreOfBoard(mainBoard)
        printScore(mainBoard, playerTile, computerTile)

        if not playAgain():
            break

if __name__ == "__main__":
    main()

