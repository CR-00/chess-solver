import chess

from django.shortcuts import render


def index(request):
	"""
	Page will always load with a default board, this way if we want to make a full-fledged
	engine rather than solving specific problems like n-queens problem, the game is already there.
	"""
	start_position = chess.STARTING_BOARD_FEN  # String representation of start position.
	context = {'game_state': start_position}
	return render(request, 'index.html', context)
