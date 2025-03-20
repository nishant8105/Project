# Stone Paper Scissor Game

This is a simple command-line game of Stone Paper Scissor. You play against the computer.

## How to Play

1.  **Run the script:** Save the code as a Python file (e.g., `game.py`) and run it from your terminal using the command: `python game.py`
2.  **Enter your choice:** The game will prompt you to enter your choice: "stone", "paper", or "scissor". Type your choice and press Enter.
3.  **Computer's turn:** The computer will randomly choose its option.
4.  **View the results:** The game will display your choice, the computer's choice, and the result of the round (you win, you lose, or it's a draw).
5.  **Keep playing:** The game will continue to prompt you for your choice until you type "quit".
6.  **Exit the game:** To end the game, type "quit" and press Enter. The game will then print "Exiting the game" and terminate.
7.  **Score:** The game keeps track of your score and the computer's score and displays the current score after each round.

## Code Explanation

* The script uses the `random` module to make the computer's choice unpredictable.
* It initializes the scores for both the user and the computer to 0.
* The game runs in a `while` loop that continues until the user enters "quit".
* Inside the loop:
    * It takes user input and converts it to lowercase.
    * It validates the user's input to ensure it's one of the valid options ("stone", "paper", "scissor", or "quit").
    * The computer makes a random choice from "stone", "paper", and "scissor".
    * The `check` function determines the winner of the round based on the classic Stone Paper Scissor rules.
    * The choices of both the user and the computer are printed.
    * The score is updated based on the result of the round.
    * The current score is displayed.

## Example Gameplay


Enter stone, paper,scissor (or 'quit' to exit)
stone
You:stone
comp:scissor
you win
Current score-->YOU:1|COMP:0
Enter stone, paper,scissor (or 'quit' to exit)
paper
You:paper
comp:paper
its draw
Current score-->YOU:1|COMP:0
Enter stone, paper,scissor (or 'quit' to exit)
scissor
You:scissor
comp:paper
you win
Current score-->YOU:2|COMP:0
Enter stone, paper,scissor (or 'quit' to exit)
paper
You:paper
comp:scissor
you lose
Current score-->YOU:2|COMP:1
Enter stone, paper,scissor (or 'quit' to exit)
quit
Exiting the game
