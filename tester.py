# Ryan Whitney
# Offical python-chess docs code was used
# https://python-chess.readthedocs.io/en/latest/pgn.html

# has_castling_rights
# can see if a side can castle

import chess.pgn
import csv
import numpy as np

# To clear file on run
with open('totalMaterial.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

with open('gameResult.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

with open('chessData.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

# Open PGN
pgn = open("chessgames3.txt")

# Lookup table for piece values
dict = {'r': 5, 'R': 5, 'n': 3, 'N': 3, 'b': 3, 'B': 3, 'q': 9, 'Q': 9, 'k': 0, 'K': 0, 'p': 1, 'P': 1}
totalMaterialWhite = 0
totalMaterialBlack = 0


# Code section to get result of game
def gameResult(currentGameResult):
    if currentGameResult == '0-1':  # Black wins
        with open('gameResult.csv', 'a', newline='') as f:
            # create the csv writer
            writer = csv.writer(f)

            # write a row to the csv file
            writer.writerow(str(0))
    elif currentGameResult == '1-0':  # White wins
        with open('gameResult.csv', 'a', newline='') as f:
            # create the csv writer
            writer = csv.writer(f)

            # write a row to the csv file
            writer.writerow(str(1))
    else:  # Draw
        pass  # Add error/draw compatibility later


def getGameResult(currentGameResult):
    if currentGameResult == '0-1':  # Black wins
        return 0
    elif currentGameResult == '1-0':  # White wins
        return 1
    else:  # Draw
        return -1  # Add error/draw compatibility later


def attacked_squares(board, color):
    attacked = chess.SquareSet()
    answer = 0;
    for attacker in chess.SquareSet(board.occupied_co[color]):
        answer = answer + 1;
        attacked |= board.attacks(attacker)
    print(attacked)
    print("\n")
    return attacked


# Code section to write array of total material throughout game to csv file
def writeToTotalMaterialCSV():
    with open('totalMaterial.csv', 'a', newline='') as f:
        # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        writer.writerow(totalMaterialWhiteArray)  # Odd rows white
        writer.writerow(totalMaterialBlackArray)  # Even rows black


def writeToChessDataCSV():
    with open('chessData.csv', 'a', newline='') as f:
        # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        writer.writerow(currentListRow)


currentListRow = []
totalMaterialWhiteArray = []
totalMaterialBlackArray = []
whiteTurn = True
numberOfGamesInPGN = 10000  # 3000  #10000

#  Iterate through all games
for i in range(numberOfGamesInPGN):

    currentGameData = chess.pgn.read_game(pgn)
    board = currentGameData.board()

    gameResult(currentGameData.headers["Result"])
    #  print(currentGameData.headers["Result"])

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
        # Iterated through this positions FEN, add to array -- array of total material at each move -- only add when
        # it's the given player (colour white/black) moved
        if whiteTurn:
            totalMaterialWhiteArray.append(int(totalMaterialWhite))
            if len(board.move_stack) > 20:  # remove first 5 moves
                # attacked_squares(board, chess.WHITE)
                currentListRow.append(int(totalMaterialWhite - totalMaterialBlack))  # appends total material
                #currentListRow.append(1)  # appends player colour data (1=white)
                #currentListRow.append(len(board.move_stack))  # appends ply move number
                currentListRow.append(getGameResult(currentGameData.headers["Result"]))  # appends game result, 1=white win, 0=black win
                writeToChessDataCSV()
            else:
                pass
        else:
            totalMaterialBlackArray.append(int(totalMaterialBlack))
            if len(board.move_stack) > 20:  # remove first 5 moves
                currentListRow.append(int(totalMaterialWhite - totalMaterialBlack))  # appends total material
                #currentListRow.append(0)  # appends player colour data (0=black)
                #currentListRow.append(len(board.move_stack))  # appends ply move number
                currentListRow.append(getGameResult(currentGameData.headers["Result"]))  # appends game result, 1=white win, 0=black win
                writeToChessDataCSV()
            else:
                pass

        whiteTurn = not (whiteTurn)  # Change turns white/black
        currentListRow = []  # clears temp variable
    # Write to CSV and erase current total since its for each game

    # Omit draws from totalMaterial CSV
    if currentGameData.headers["Result"] != '1/2-1/2':
        writeToTotalMaterialCSV()
    totalMaterialWhiteArray = []
    totalMaterialBlackArray = []

print("done running tester.py")
