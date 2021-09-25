import chess
import random

WHITE_QUEEN = chess.Piece(piece_type=chess.QUEEN, color=True)


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


def generate_random_n_queens_problem(n: int) -> str:
    """
    https://en.wikipedia.org/wiki/Eight_queens_puzzle
    Sets up a new board with n queens in a random allocation using
    selection without replacement.
    """
    board = chess.Board().empty()
    empty_squares = get_empty_squares(board)
    for i in range(n):
        random_empty_square = random.choice(empty_squares)
        board.set_piece_at(random_empty_square, WHITE_QUEEN)
        empty_squares.remove(random_empty_square)
    return board.epd()


def queen_is_attacking_other_queen(board: chess.Board, queen_square: chess.Square) -> bool:
    """
    Since all queen's are the same colour, we can't just use the built
    in function to check what a piece is attacking, so we check if here is
    another piece in the same file/rank/diagonal as a piece on a square.
    """
    is_attacking_other_queen = False
    other_queens = get_pieces_squares(board, WHITE_QUEEN)
    for other_queen in other_queens:
        is_attacking_other_queen = (squares_on_same_rank(queen_square, other_queen) or
                                    squares_on_same_file(queen_square, other_queen) or
                                    squares_on_same_diagonal(queen_square, other_queen))
    return is_attacking_other_queen


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
    file_one = chess.square_rank(square_one)
    file_two = chess.square_rank(square_two)
    return (file_one - file_two) == 0


def squares_on_same_diagonal(square_one: chess.Square, square_two: chess.Square) -> bool:
    """
    Check whether two squares are on the same diagonal.
    """
    diagonal_one = get_square_diagonal(square_one)
    diagonal_two = get_square_diagonal(square_two)
    return (diagonal_one - diagonal_two) == 0


if __name__ == '__main__':
    board = chess.Board(generate_random_n_queens_problem(8))
    print(is_solution(board))