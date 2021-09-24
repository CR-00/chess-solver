import chess
import random

WHITE_QUEEN = chess.Piece(piece_type=chess.QUEEN, color=True)


def get_empty_squares(board: chess.Board) -> list:
    empty_squares = []
    for i in chess.SQUARES:
        if not board.piece_at(i):
            empty_squares.append(i)
    return empty_squares


def get_pieces_squares(board: chess.Board, piece_type: chess.Piece) -> list:
    squares = []
    for i in chess.SQUARES:
        if board.piece_at(i) == piece_type:
            squares.append(i)
    return squares


def generate_n_queens_problem(n: int) -> str:
    board = chess.Board().empty()
    empty_squares = get_empty_squares(board)
    for i in range(n):
        random_empty_square = random.choice(empty_squares)
        board.set_piece_at(random_empty_square, WHITE_QUEEN)
        empty_squares.remove(random_empty_square)
    return board.epd()


def main() -> None:
    board = chess.Board(generate_n_queens_problem(8))
    print(board)
    print('\n')
    queen_squares = get_pieces_squares(board, WHITE_QUEEN)
    print(queen_squares)


if __name__ == '__main__':
    main()
