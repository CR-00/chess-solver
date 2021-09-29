import chess
import random
import itertools

WHITE_QUEEN = chess.Piece(piece_type=chess.QUEEN, color=True)
SAMPLE_SOLUTION = r'3Q4/1Q6/6Q1/2Q5/5Q2/7Q/4Q3/Q7 w - -'  # Useful for debugging.


# Solution Algorithms:

def solve_by_brute_force(n: int = 8) -> str:
    """
    Returns a solution to the n-queens-problem via brute force.
    Generates all permutations, then one rank (i) is given to each queen,
    since no two queens can be on the same rank and/or file.
    Then the file of each queen is determined by permutation[i].
    """
    if n > 8:  # Max supported board size in client is 8x8.
        raise ValueError(f"No solution exists for %s queens on an 8x8 board." % (n))

    permutations = list(itertools.permutations(range(0, n)))
    for permutation in permutations:
        board = chess.Board().empty()
        queen_squares = []
        for i in range(n):
            square = 8 * i + permutation[i]  # 8 * rank + file = Square Number
            queen_squares.append(square)
        for i in queen_squares:
            board.set_piece_at(i, WHITE_QUEEN)
        if is_solution(board):
            return board.epd()

    raise ValueError("No solution was found.")


# Utility functions:


def get_empty_squares(board: chess.Board) -> list:
    """
    Returns a list of all the empty squares on the board.
    """
    empty_squares = []
    for i in chess.SQUARES:
        if not board.piece_at(i):
            empty_squares.append(i)
    return empty_squares


def get_pieces_squares(board: chess.Board, piece_type: chess.Piece) -> list:
    """
    Returns a list of all the squares on the board with a piece on them.
    """
    squares = []
    for i in chess.SQUARES:
        if board.piece_at(i) == piece_type:
            squares.append(i)
    return squares


def generate_random_n_queens_problem(n: int = 8) -> str:
    """
    https://en.wikipedia.org/wiki/Eight_queens_puzzle
    Sets up a new board with n queens in a random allocation using
    selection without replacement, default is 8.
    """
    board = chess.Board().empty()
    empty_squares = get_empty_squares(board)
    for i in range(n):
        random_empty_square = random.choice(empty_squares)
        board.set_piece_at(random_empty_square, WHITE_QUEEN)
        empty_squares.remove(random_empty_square)
    return board.epd()


def queen_is_attacking_other_queen(board: chess.Board, queen: chess.Square) -> bool:
    """
    Since all queen's are the same colour, we can't just use the built
    in function to check what a piece is attacking, so we check if there is
    another piece in the same file/rank/diagonal as a piece on a square.
    """
    other_queens = get_pieces_squares(board, WHITE_QUEEN)
    for q in other_queens:
        if q != queen:  # Not referring to the same piece.
            if (squares_on_same_rank(q, queen) or
                    squares_on_same_file(q, queen) or
                    squares_on_same_diagonal(q, queen) or
                    squares_on_same_anti_diagonal(q, queen)):
                return True
    return False


def is_solution(board: chess.Board) -> bool:
    """
    Checks whether any queen is attacking another, if it is then the problem is not solved.
    """
    queens = get_pieces_squares(board, WHITE_QUEEN)
    for queen in queens:
        if queen_is_attacking_other_queen(board, queen):
            return False
    return True


def get_square_diagonal(square: chess.Square) -> int:
    """
    https://www.chessprogramming.org/Diagonals
    Returns the number of the diagonal, with this we can
    check whether two squares are on the same diagonal.
    """
    rank = chess.square_rank(square)
    file = chess.square_file(square)
    return rank - file


def squares_on_same_rank(square_one: chess.Square, square_two: chess.Square) -> bool:
    """
    Check whether two squares are on the same rank/row.
    """
    rank_one = chess.square_rank(square_one)
    rank_two = chess.square_rank(square_two)
    return (rank_one - rank_two) == 0


def squares_on_same_file(square_one: chess.Square, square_two: chess.Square) -> bool:
    """
    Check whether two squares are on the same file/column.
    """
    file_one = chess.square_file(square_one)
    file_two = chess.square_file(square_two)
    return (file_one - file_two) == 0


def squares_on_same_diagonal(square_one: chess.Square, square_two: chess.Square) -> bool:
    """
    Check whether two squares are on the same (left-right) diagonal.
    """
    if square_diagonal(square_one) == square_diagonal(square_two):
        return True
    return False


def squares_on_same_anti_diagonal(square_one: chess.Square, square_two: chess.Square) -> bool:
    """
    Checks whether two squares are on the same (right-left) diagonal / anti_diagonal.
    """
    if square_anti_diagonal(square_one) == square_anti_diagonal(square_two):
        return True
    return False


def convert_square_number_to_x_y_coordinates(square: chess.Square) -> list:
    """
    Converts an integer value for a square on the board to an (x, y) coordinate
    of the form [rank, file].
    """
    rank = square >> 3  # Divide by 8
    file = square & 7  # Mod 8
    return [rank, file]


def square_diagonal(square: chess.Square) -> int:
    """
    Returns the diagonal (left-to-right) index of an integer representation of a
    square on the board.
    """
    rank = square >> 3  # Divide by 8
    file = square & 7  # Mod 8
    return (rank - file) & 15  # 16 diagonals on an 8x8 board.


def square_anti_diagonal(square: chess.Square) -> int:
    """
    Returns the anti-diagonal (right-to-left) index of an integer representation of a
    square on the board.
    """
    rank = square >> 3  # Divide by 8
    file = square & 7  # Mod 8
    return (rank + file) ^ 7


def solved_board() -> str:
    """
    Useful for testing in development, returns an EPD string of a board that is
    a known solution of the 8-queens problem.
    """
    board = chess.Board().empty()
    queens = [0, 12, 23, 29, 34, 46, 49, 59]
    for i in queens:
        board.set_piece_at(i, WHITE_QUEEN)
    return board.epd()


if __name__ == '__main__':
    solution = solve_by_brute_force(n=8)
    board = chess.Board(solution)
    print(board)
