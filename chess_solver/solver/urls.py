from django.urls import path

from . import views

# Ordinarily would just have the pieces in static/images/ but using chessboard.js CDN
# means a path must be added to access the pieces.

urlpatterns = [
	path('', views.index, name='index'),
]
