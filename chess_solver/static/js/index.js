gameState = document.querySelector('#starting-game-state');
console.log(gameState);

var config = {
  draggable: true,
  dropOffBoard: 'snapback', 
  position: 'start'
}

var board1 = Chessboard('board1', config)
