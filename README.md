# Tower-of-Hanoi

A program that solves and lets you play the Tower of Hanoi mathematical puzzle. The traditional Tower of Hanoi puzzle involves moving a number of different sized rings onto 3 different pegs. In this augemented version, the game is played with 4 pegs and its solution was an open problem for quite some time. The objective is to move the rings is to:

- Move all pegs from the first to the last peg;
- Ensure each ring is always sitting on top of a smaller ring;
- Use the least number of moves.

## How to Play

To play the game on the console run the command:

> python3 console_controller.py

To play the game using the graphical user interface run:

> python3 gui_controller.py

To determine the optimal solution you can run:

> python3 tour.py

In the tour.py file to determine the solution to a game with `r` rings and `p` pegs:

- On line 104 set `num_cheeses = r`; this sets the cheese count.
- On line 107 set `four_stools = TOAHModel(p)`; this sets the peg count (the default is 4).

## Screenshots

![Start of game screenshot](https://github.com/MichaelDeLisio/Tower-of-Hanoi/blob/main/screenshots/start_of_game.png)
