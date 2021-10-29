// I don't really know Javascript, this took a lot of time to make. (Around 2 and a half hours)
// To be honest, it was really hard!
// I looked thru the documentation for at least a hour,
// hopefully it wasn't against the rules 😅

// Waits for the page to load
window.addEventListener('DOMContentLoaded', () => {
   // Add all elements we need for the game
   const tiles = Array.from(document.querySelectorAll('.tile')); // Used an array so I don't repeat them again and again
   const playerDisplay = document.querySelector('.player'); // Show's which player's turn it is
   const resetButton = document.querySelector('#reset'); // Resets the game
   const announcer = document.querySelector('.announcer'); // Shows if the P1 or P2 has won or it's a tie

   let board = ['', '', '', '', '', '', '', '', '']; // Used an array again, just like python
   let currentPlayer = 'X'; // Set the first player to be with X
   let isGameActive = true; // Sets the game active

   const PLAYERX_WON = 'PLAYERX_WON';
   const PLAYERO_WON = 'PLAYERO_WON';
   const TIE = 'TIE';


   // Game Table:
   // 0 | 1 | 2
   // 3 | 4 | 5
   // 6 | 7 | 8

   const winningConditions = [
      // Horizontal
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      // Vertical
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      // Diagonal
      [0, 4, 8],
      [2, 4, 6]
   ];

   function resultValidation() {
      let roundWon = false;

      // If there are less than 8 moves, don't end the game yet
      for (let i = 0; i <= 7; i++) {
         const winCondition = winningConditions[i];
         const a = board[winCondition[0]];
         const b = board[winCondition[1]];
         const c = board[winCondition[2]];
         if (a === '' || b === '' || c === '') {
            continue;
         }
         if (a === b && b === c) {
            roundWon = true;
            break;
         }
      }

      // If the round is won, end the game and announce it
      if (roundWon) {
         announce(currentPlayer === 'X' ? PLAYERX_WON : PLAYERO_WON);
         isGameActive = false;
         return;
      }

      // If no one won, announce tie
      if (!board.includes('')) // Checks if there's empty tiles, if there aren't end the game and announce tie (if there's no winner)
      announce(TIE);
   }

   // Announcer
   const announce = (type) => {
      switch(type){
          case PLAYERO_WON: // If player 2 won, announce it
            announcer.innerHTML = 'Player <span class="playerO">O</span> Won! :D';
            break;
         case PLAYERX_WON: // If player 1 won, announce it
            announcer.innerHTML = 'Player <span class="playerX">X</span> Won! :D';
            break;
         case TIE: // If no one won, announce tie
            announcer.innerText = 'Tie :|';
       }
       announcer.classList.remove('hide');
   };

   // Checks if players clicked on already clicked tiles
   const isValidAction = (tile) => {
      if (tile.innerText === 'X' || tile.innerText === 'O'){
         return false;
      }

      return true;
   };

   // Updates the table so it shows the X/O
   const updateBoard =  (index) => {
      board[index] = currentPlayer;
   }

   // Switches between player 1 and 2
   const changePlayer = () => {
      playerDisplay.classList.remove(`player${currentPlayer}`);
      currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
      playerDisplay.innerText = currentPlayer;
      playerDisplay.classList.add(`player${currentPlayer}`);
   }

   // Executes all functions if everything is fine
   const userAction = (tile, index) => {
      if(isValidAction(tile) && isGameActive) { // Checks for the valid actions and for the game if its running
         tile.innerText = currentPlayer;
         tile.classList.add(`player${currentPlayer}`);

         // Update the game table
         updateBoard(index);

         // Validate the results
         resultValidation();
         
         // Change the turn
         changePlayer();
      }
   }
   
   // Reset the game
   const resetBoard = () => {
      // Sets all tiles to none, activates the game and hides the announcer
      board = ['', '', '', '', '', '', '', '', ''];
      isGameActive = true;
      announcer.classList.add('hide');

      // If the player from last game was O(2) change to X(1)
      if (currentPlayer === 'O') {
         changePlayer();
      }

      // Sets all tiles to none
      tiles.forEach(tile => {
         tile.innerText = '';
         tile.classList.remove('playerX');
         tile.classList.remove('playerO');
      });
   }

   // Listen for clicks on the tiles
   tiles.forEach( (tile, index) => {
      tile.addEventListener('click', () => userAction(tile, index));
   });

   // Listen for reset button
   resetButton.addEventListener('click', resetBoard);
});