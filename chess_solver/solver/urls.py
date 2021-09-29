from django.urls import path

from . import views

# Ordinarily would just have the pieces in static/images/ but using chessboard.js CDN
# means a path must be added to access the pieces.

urlpatterns = [
	path('', views.index, name='index'),
	path('get/ajax/n_queens_problem/n=<int:id>', views.get_random_n_queens_problem, name='get_n_queens_problem'),
	path('get/ajax/n_queens_brute_force_solution/n=<int:id>', views.get_brute_force_solution, name='brute_force_solution'),
	path('get/ajax/check_solution/str=<str:id>', views.check_n_queens_solution, name='check_n_queens_solution')
]
