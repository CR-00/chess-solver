// Initial game state is loaded from input variable in HTML doc.
var gameState = document.querySelector('#game-state');

// Set up chess board.
var config = {
  pieceTheme: 'static/images/chesspieces/wikipedia/{piece}.png',
  position: gameState.value,
  draggable: true,
  dropOffBoard: 'snapback', 
}

var board = Chessboard('board', config);

// Make slider show value.
var slider = document.querySelector('.slider');

var numberOfQueens = document.querySelector('.number-of-queens');
numberOfQueens.innerHTML = 'Number of Queens: 50'; // Initial value is 50.

slider.addEventListener('input', function() {
  numberOfQueens.innerHTML = 'Number of Queens: ' + this.value;
});