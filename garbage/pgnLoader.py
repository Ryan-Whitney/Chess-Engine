import chess
import chess.pgn

# creating a virtual chessboard
board = chess.Board()

print(board)

print("\n")

pgn = open("lichess_test_pgn.pgn")
game = chess.pgn.read_game(pgn)

# The move number for which we want the FEN
move_number = 100

# Go through each move in the game until
# we reach the required move number
for number, move in enumerate(game.mainline_moves()):

    # It copies the move played by each
    # player on the virtual board
    board.push(move)

    # Remember that number starts from 0
    if number == move_number:
        break

fen = board.fen()
print(fen)


print(board)

#%%
