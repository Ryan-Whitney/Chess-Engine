# Ryan Whitney
# Offical python-chess docs code was used
# https://python-chess.readthedocs.io/en/latest/pgn.html

# first_game.headers["Result"]
# can read header metadata

# has_castling_rights
# can see if a side can castle

import chess.pgn

# Open PGN
pgn = open("chessgames2.txt")
#print(first_game.headers["Result"])

# Lookup table for piece values
dict = {'r': 5, 'R': 5, 'n': 3,'N': 3, 'b': 3, 'B': 3, 'q': 9,'Q': 9, 'k': 0, 'K': 0, 'p': 1,'P': 1}
totalMaterialWhite = 0
totalMaterialBlack = 0

# Iterate through all moves and play them on a board.
game1 = chess.pgn.read_game(pgn)
board = game1.board()
for move in game1.mainline_moves():
    board.push(move)
    #print(board)
    #print()
    fen = board.fen()
    #print(fen)
    #print()


for i in fen:
    if not(i.isnumeric()) and i != "/":
        if i == ' ':
            break
        else:
            if str.islower(i):
                # Add to black material total
                totalMaterialBlack = totalMaterialBlack + dict[i]
            else:
                # Add to white material total
                totalMaterialWhite = totalMaterialWhite + dict[i]

        print(i) # prints the fen 1 by 1


print()
print(str(totalMaterialWhite))
print()
print(str(totalMaterialBlack))

#get total number of piece material