from django.test import TestCase
import chess
import os

board = chess.Board(fen=chess.STARTING_FEN)
print(chess.STARTING_BOARD_FEN)