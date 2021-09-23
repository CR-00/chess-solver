from django.db import models


class ChessGame(models.Model):
    """

    The state of the game is stored as a string representation in the database.

    For the front end representation the JS library 'chessboard.js' is used:
    https://chessboardjs.com/index.html

    For the backend we use the Python library python-chess:
    https://python-chess.readthedocs.io/en/latest/

    Luckily both log the state of the game in the same ASCII format (epd) so are compatible
    with one another.

    """

