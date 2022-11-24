# Ryan Whitney
# Offical python-chess docs code was used
# https://python-chess.readthedocs.io/en/latest/pgn.html

# has_castling_rights
# can see if a side can castle

import chess.pgn
import csv

# To clear file on run
with open('totalMaterial.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

with open('gameResult.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

# Open PGN
pgn = open("chessgames2.txt")

# Lookup table for piece values
dict = {'r': 5, 'R': 5, 'n': 3,'N': 3, 'b': 3, 'B': 3, 'q': 9,'Q': 9, 'k': 0, 'K': 0, 'p': 1,'P': 1}
totalMaterialWhite = 0
totalMaterialBlack = 0


# Code section to get result of game
def gameResult(currentGameResult):
    if currentGameResult == '0-1': # Black wins
        with open('gameResult.csv', 'a', newline='') as f:
            # create the csv writer
            writer = csv.writer(f)

            # write a row to the csv file
            writer.writerow(str(0))
    elif currentGameResult == '1-0': # White wins
        with open('gameResult.csv', 'a', newline='') as f:
            # create the csv writer
            writer = csv.writer(f)

            # write a row to the csv file
            writer.writerow(str(1))
    else:  # Draw
        pass  # Add error/draw compatibility


# Code section to write array of total material throughout game to csv file
def writeToCSV():
    with open('totalMaterial.csv', 'a', newline='') as f:
        # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        writer.writerow(totalMaterialWhiteArray)
        writer.writerow(totalMaterialBlackArray)

totalMaterialWhiteArray = []
totalMaterialBlackArray = []
whiteTurn = True
numberOfGamesInPGN = 1

#  Iterate through all games
for i in range(numberOfGamesInPGN):

    currentGameData = chess.pgn.read_game(pgn)
    board = currentGameData.board()

    gameResult(currentGameData.headers["Result"])
    #  print(currentGameData.headers["Result"])

    #  Iterate through all moves on current game
    for move in currentGameData.mainline_moves():
        board.push(move)
        fen = board.fen()
        totalMaterialWhite = 0
        totalMaterialBlack = 0

        # Iterate through game to get total material
        for i in fen:
            if not (i.isnumeric()) and i != "/":
                if i == ' ':
                    break
                else:
                    if str.islower(i): # If its lowercase it is a black piece
                        totalMaterialBlack = totalMaterialBlack + dict[i]  # Add to black material total
                    else: # If its uppercase it is a white piece
                        totalMaterialWhite = totalMaterialWhite + dict[i] # Add to white material total
        # Iterated through this positions FEN, add to array -- array of total material at each move -- only add when
        # it's the given player (colour white/black) moved
        if whiteTurn:
            totalMaterialWhiteArray.append(int(totalMaterialWhite))
        else:
            totalMaterialBlackArray.append(int(totalMaterialBlack))

        whiteTurn = not(whiteTurn) # Change turns white/black

    # Write to CSV and erase current total since its for each game
    writeToCSV()
    totalMaterialWhiteArray = []
    totalMaterialBlackArray = []


#  get total number of piece material




import numpy as np
def euclidean_distance(x1, x2):
    distance = np.sqrt(np.sum((x1 - x2) ** 2))
    return distance



gameResultTemp = []

with open('gameResult.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        # process each line
        #print(line)
        gameResultTemp.append(line)
        var1 = ([list(map(int, i)) for i in gameResultTemp])
        var2 = sum(var1, [])

print(var2)

totalMaterialTemp = []

with open('totalMaterial.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        # process each line
        #print(line)
        totalMaterialTemp.append(line)
        var3 = ([list(map(int, i)) for i in totalMaterialTemp])

print(var3)

#  var is the game result, 1 or 0
#print(var[5])



