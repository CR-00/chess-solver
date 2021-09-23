import chess

from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .models import ChessGame


def index(request):

	# Initialise a new game in the starting position then
	# store the representation as a string in the DB.
	board = chess.Board(fen=chess.STARTING_FEN)
	game = ChessGame(board.epd())

	context = {'game': game}
	return render(request, 'index.html', context)
