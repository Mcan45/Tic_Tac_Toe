#Tic Tac Toe
This is an unbeatable tic tac toe game.
This game is played by console
# How it works
Download the tic_tac_toe.py file and type python tic_tac_toe.py
on your terminal(You should have got to installed python).

Game is played on 3x3 square

 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
-----------


when you run the game firstly you should choose your sign(X or O) and your goal is to make a straight line on a row, column or on a diagonal and computers too.

You should press the number of square that you want to move

After you played computer checks if you win or tie and prints a message for the state of game

# How AI works

-computer firstly looks for if it can win on one move, it plays and prints computer win!

-then look for a move that can block for gamers win

-looks for appropirate corners[1, 3, 7, 9] and chooses one randomly and plays

-if all corners are full then looks for if middle[5] is empty and if it is empty it plays

-else looks for appropirate edges[2, 4, 6, 8] and if there is some plays one of them randomly

- if there isn't any appropirate move and the board is full prints tie! message
