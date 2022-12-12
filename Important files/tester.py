# Ryan Whitney

import chess.pgn
import csv

# To clear file on run
with open('../garbage/totalMaterial.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

with open('../garbage/gameResult.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

with open('chessData.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

# Open PGN
pgn = open("chessgames4.txt")

# Lookup table for piece values
dict = {'r': 5, 'R': 5, 'n': 3, 'N': 3, 'b': 3, 'B': 3, 'q': 9, 'Q': 9, 'k': 0, 'K': 0, 'p': 1, 'P': 1}

# returns game result
def getGameResult(currentGameResult):
    if currentGameResult == '0-1':  # Black wins
        return 0
    elif currentGameResult == '1-0':  # White wins
        return 1
    else:  # Draw
        return -1  # Add error/draw compatibility later


# lines of code below from https://github.com/niklasf/python-chess/issues/814
def attackedSquares(board, color):
    attacked = chess.SquareSet()
    for k in chess.SquareSet(board.occupied_co[color]):
        attacked |= board.attacks(k)
    #print(attacked)
    #print("\n")
    return len(attacked)

# Writes all data to single master file
def writeToChessDataCSV():
    with open('chessData.csv', 'a', newline='') as f:
        # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        writer.writerow(currentListRow)

totalMaterialWhite = 0
totalMaterialBlack = 0
currentListRow = []
whiteTurn = True
whiteQueenExists = False
blackQueenExists = False
numberOfGamesInPGN = 500  # 3000  #10000

#  Iterate through all games
for i in range(numberOfGamesInPGN):

    currentGameData = chess.pgn.read_game(pgn)
    board = currentGameData.board()

    #  Iterate through all moves on current game
    for move in currentGameData.mainline_moves():

        # Omit draws from totalMaterial CSV
        if currentGameData.headers["Result"] == '1/2-1/2':
            break

        board.push(move)
        fen = board.fen()
        totalMaterialWhite = 0
        totalMaterialBlack = 0

        # Iterate through game to get total material
        for i in fen:
            if not (i.isnumeric()) and i != "/" and i != "[" and i != "]" and i != "~":
                if i == ' ':
                    break
                else:
                    # print(i)
                    if str.islower(i):  # If its lowercase it is a black piece
                        totalMaterialBlack = totalMaterialBlack + dict[i]  # Add to black material total
                    else:  # If its uppercase it is a white piece
                        totalMaterialWhite = totalMaterialWhite + dict[i]  # Add to white material total
                    if i == 'Q':
                        whiteQueenExists = True
                    if i == 'q':
                        blackQueenExists = True
        # Iterated through this positions FEN, add to array -- array of total material at each move -- only add when
        # it's the given player (colour white/black) moved
        if whiteTurn:
            if len(board.move_stack) > 20:  # remove first 10 moves (20 ply)
                currentListRow.append(getGameResult(currentGameData.headers["Result"]))  # appends game result, 1=white win, 0=black win
                currentListRow.append(int(totalMaterialWhite - totalMaterialBlack))  # appends total material difference
                currentListRow.append(int(totalMaterialWhite))  # appends total material
                currentListRow.append(int(totalMaterialBlack))  # appends total material
                currentListRow.append(1)  # appends player colour data (1=white)
                currentListRow.append(len(board.move_stack))  # appends ply move number
                if board.is_check():  # if in check append 1 to black
                    currentListRow.append(0)  # append 0 white not in check
                    currentListRow.append(1)  # append 1 if black in check
                else:
                    currentListRow.append(0)  # append 0 white not in check
                    currentListRow.append(0)  # append 0 black not in check
                if whiteQueenExists:  # if white queen exists append 1, if not, append 0
                    currentListRow.append(1)
                else:
                    currentListRow.append(0)
                if blackQueenExists:  # if black queen exists append 1, if not, append 0
                    currentListRow.append(1)
                else:
                    currentListRow.append(0)

                currentListRow.append(attackedSquares(board, chess.WHITE))  # appends number of squares white attacks
                currentListRow.append(attackedSquares(board, chess.BLACK))  # appends number of squares black attacks

                writeToChessDataCSV()  # update data file
            else:
                pass
        else:  # black turn
            if len(board.move_stack) > 20:  # remove first 10 moves (20 ply)
                currentListRow.append(getGameResult(currentGameData.headers["Result"]))  # appends game result, 1=white win, 0=black win
                currentListRow.append(int(totalMaterialWhite - totalMaterialBlack))  # appends total material difference
                currentListRow.append(int(totalMaterialWhite))  # appends total material
                currentListRow.append(int(totalMaterialBlack))  # appends total material
                currentListRow.append(0)  # appends player colour data (0=black)
                currentListRow.append(len(board.move_stack))  # appends ply move number
                if board.is_check():  # if in check append 1 to white
                    currentListRow.append(1)  # append 1 if white in check
                    currentListRow.append(0)  # append 0 black not in check
                else:
                    currentListRow.append(0)  # append 0 white not in check
                    currentListRow.append(0)  # append 0 black not in check
                if whiteQueenExists:  # if white queen exists append 1, if not, append 0
                    currentListRow.append(1)
                else:
                    currentListRow.append(0)
                if blackQueenExists:  # if black queen exists append 1, if not, append 0
                    currentListRow.append(1)
                else:
                    currentListRow.append(0)

                currentListRow.append(attackedSquares(board, chess.WHITE))  # appends number of squares white attacks
                currentListRow.append(attackedSquares(board, chess.BLACK))  # appends number of squares black attacks

                writeToChessDataCSV()  # update data file
            else:
                pass

        whiteTurn = not (whiteTurn)  # Change turns white/black
        whiteQueenExists = False  # Resets temp queenExist flag variable
        blackQueenExists = False  # Resets temp queenExist flag variable
        currentListRow = []  # clears temp variable
    # Write to CSV and erase current total since its for each game

    totalMaterialWhiteArray = []
    totalMaterialBlackArray = []

print("done running tester.py")
