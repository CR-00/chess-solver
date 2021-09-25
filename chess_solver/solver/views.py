import chess

from django.shortcuts import render
from django.http import HttpResponse

from .n_queens_problem_solver import generate_random_n_queens_problem


def index(request):
	context = {
		'game_state': chess.Board().empty().epd()  # Always start with empty board.
	}
	return render(request, 'index.html', context)


def get_random_n_queens_problem(request, id):
	if request.method == 'GET':
		number_of_queens = id
		board = generate_random_n_queens_problem(number_of_queens)
		return HttpResponse(board)