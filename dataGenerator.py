"""
Runs KNN model on chosen number of chess games. Includes all positions during the game after starting move number
offset. It ignores draws.
"""

import chess.pgn
import csv

# To clear file on run
with open('chessData.csv', 'w') as f:
    writer = csv.writer(f)

# Open PGN
pgn = open("chessGames.txt")

# Lookup table for piece values
conversion_table = {'r': 5, 'R': 5, 'n': 3, 'N': 3, 'b': 3, 'B': 3, 'q': 9, 'Q': 9, 'k': 0, 'K': 0, 'p': 1, 'P': 1}


def get_game_result(current_game_result):
    """
    Converts string of game result into numeric value
    :param current_game_result:
    :return: 0 if black wins, 1 if white wins
    """
    if current_game_result == '0-1':  # Black wins
        return 0
    elif current_game_result == '1-0':  # White wins
        return 1
    else:  # Draw
        return -1  # Add error/draw compatibility later


def attacked_squares(board, colour):
    """
    Gets number of attacked squares by given colour
    Inspired by: https://github.com/niklasf/python-chess/issues/814
    :param board:
    :param colour:
    :return: Number of attacked squares
    """
    attacked = chess.SquareSet()
    for k in chess.SquareSet(board.occupied_co[colour]):
        attacked |= board.attacks(k)
    return len(attacked)


# Writes all data to single master file
def write_to_chess_data_CSV(data):
    """
    Writes to CSV file
    :param data:
    :return:
    """
    with open('chessData.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)


total_material_white = 0
total_material_black = 0
data = []
header_tags = ["result", "materialDifference", "totalWhiteMaterial", "totalBlackMaterial", "colour", "plyNumber",
               "whiteInCheck", "blackInCheck", "white_queen_exists", "black_queen_exists", "numSquaresWhiteAttacks",
               "numSquaresBlackAttacks"]
white_turn = True
white_queen_exists = False
black_queen_exists = False
number_of_games_in_PGN = 1000
starting_ply_offset = 20  # remove first x ply (0.5*x moves) from start of chess game

write_to_chess_data_CSV(header_tags)  # Add labels to data file

#  Iterate through all games
for game in range(number_of_games_in_PGN):

    current_game_data = chess.pgn.read_game(pgn)
    board = current_game_data.board()

    #  Iterate through all moves on current game
    for move in current_game_data.mainline_moves():

        # Omit draws from totalMaterial CSV
        if current_game_data.headers["Result"] == '1/2-1/2':
            break

        board.push(move)
        fen = board.fen()
        total_material_white = 0
        total_material_black = 0

        # Iterate through game to get total material
        for char in fen:
            if not (char.isnumeric()) and char != "/" and char != "[" and char != "]" and char != "~":
                if char == ' ':
                    break
                else:
                    if str.islower(char):  # If it's lowercase it's a black piece
                        total_material_black = total_material_black + conversion_table[char]  # Add to black material total
                    else:  # If it's uppercase it's a white piece
                        total_material_white = total_material_white + conversion_table[char]  # Add to white material total
                    if char == 'Q':
                        white_queen_exists = True
                    if char == 'q':
                        black_queen_exists = True
        if white_turn:
            if len(board.move_stack) > starting_ply_offset:  # remove first few moves
                data.append(get_game_result(current_game_data.headers["Result"]))  # appends game result
                data.append(int(total_material_white - total_material_black))  # appends total material difference
                data.append(int(total_material_white))  # appends total material
                data.append(int(total_material_black))  # appends total material
                data.append(1)  # appends player colour data (1=white)
                data.append(len(board.move_stack))  # appends ply move number
                if board.is_check():  # if in check append 1 to black
                    data.append(0)  # append 0 white not in check
                    data.append(1)  # append 1 if black in check
                else:
                    data.append(0)  # append 0 white not in check
                    data.append(0)  # append 0 black not in check
                if white_queen_exists:  # if white queen exists append 1, if not, append 0
                    data.append(1)
                else:
                    data.append(0)
                if black_queen_exists:  # if black queen exists append 1, if not, append 0
                    data.append(1)
                else:
                    data.append(0)

                data.append(attacked_squares(board, chess.WHITE))  # appends number of squares white attacks
                data.append(attacked_squares(board, chess.BLACK))  # appends number of squares black attacks

                write_to_chess_data_CSV(data)

        else:  # black turn
            if len(board.move_stack) > starting_ply_offset:  # remove first few moves
                data.append(get_game_result(current_game_data.headers["Result"]))  # appends game result
                data.append(int(total_material_white - total_material_black))  # appends total material difference
                data.append(int(total_material_white))  # appends total material
                data.append(int(total_material_black))  # appends total material
                data.append(0)  # appends player colour data (0=black)
                data.append(len(board.move_stack))  # appends ply move number
                if board.is_check():  # if in check append 1 to white
                    data.append(1)  # append 1 if white in check
                    data.append(0)  # append 0 black not in check
                else:
                    data.append(0)  # append 0 white not in check
                    data.append(0)  # append 0 black not in check
                if white_queen_exists:  # if white queen exists append 1, if not, append 0
                    data.append(1)
                else:
                    data.append(0)
                if black_queen_exists:  # if black queen exists append 1, if not, append 0
                    data.append(1)
                else:
                    data.append(0)

                data.append(attacked_squares(board, chess.WHITE))  # appends number of squares white attacks
                data.append(attacked_squares(board, chess.BLACK))  # appends number of squares black attacks

                write_to_chess_data_CSV(data)

        white_turn = not white_turn  # Change turns
        white_queen_exists = False  # Resets flag variable
        black_queen_exists = False  # Resets flag variable
        data = []  # clears data after each position

print("done running dataGenerator.py")
