// Initial game state is loaded from input variable in HTML doc.
var gameState = document.querySelector('#game-state');

// Set up chess board.
var config = {
  pieceTheme: 'static/images/chesspieces/wikipedia/{piece}.png',
  position: gameState.value,
  moveSpeed: 'slow',
  draggable: true,
  dropOffBoard: 'snapback', 
}

var board = Chessboard('board', config);

// Make slider show value.
var slider = document.querySelector('.slider');
var numberOfQueens = document.querySelector('.number-of-queens');
numberOfQueens.innerHTML = 'Number of Queens: 8'; // Initial value is 50.

slider.addEventListener('input', function() {
  numberOfQueens.innerHTML = 'Number of Queens: ' + this.value;
});

// Get a random position of n-queens from the server on click.
var refreshButton = document.querySelector('.reload-button');
var nQueensProblem;

refreshButton.addEventListener('click', function() {
  randomiseBoard(slider.value);
  startTimer(); // Reset timer.
});

// Awaits random board state then sets the board position on success.
async function randomiseBoard(number_of_queens) {
  await getRandomNQueensPosition(number_of_queens).then((value) =>{
    board.position(nQueensProblem);
  });
}

// Gets a random board state from the server.
async function getRandomNQueensPosition(number_of_queens) {
  $.ajax({
    url: 'get/ajax/n_queens_problem/n=' + number_of_queens,
    type: 'GET',
    success: function(response) {
      nQueensProblem = response;
    },
  });
}

// Set timer to track how long the solution takes to find.
var timeTaken = 0;
var timerStarted = false;
var timer = document.querySelector('.time-taken');

function startTimer() {
  timeTaken = 0;
  if (!timerStarted) {
    interval = setInterval(incrementTimer, 1000); // Add 1 to timer every 1 sec.
    timerStarted = true;
  }
}

function incrementTimer() {
  timeTaken += 1;
  timer.innerHTML = mintutesAndSecondsFormat(timeTaken);
}

// https://stackoverflow.com/questions/3733227
function mintutesAndSecondsFormat(s){
  return(s-(s%=60))/60+(9<s?':':':0')+s
}


// Solution algorithms:

function solveByBruteForce() {
    $.ajax({
    url: 'get/ajax/n_queens_brute_force_solution/n=' + slider.value,
    type: 'GET',
    success: function(response) {
      board.position(response);
    },
  });
}