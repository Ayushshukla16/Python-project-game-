PROJECT STATEMENT

Project Title: Rock, Paper, Scissors Game Simulation
Language: Python

1. INTRODUCTION
The "Rock, Paper, Scissors" game is a widely known hand game usually played between two people, where each player simultaneously forms one of three shapes with an outstretched hand. This project aims to digitize this experience by creating a console-based application where a single user can play against an automated computer opponent.

2. PROBLEM STATEMENT
The objective is to design and develop a Python script that simulates the logic of the Rock, Paper, Scissors game. The system must generate a random choice for the computer, accept user input, and determine the winner based on the standard rules of the game (Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock). The program must also handle invalid inputs and allow the user to play multiple rounds continuously.

3. OBJECTIVES
- To implement the 'random' module for generating unpredictable computer moves.
- To utilize conditional statements (if-elif-else) to strictly enforce game rules and determine the winner.
- To implement input validation to ensure the program does not crash on incorrect user entries.
- To use loop structures (while loops) to enable replay functionality without restarting the application.

4. PROPOSED LOGIC (ALGORITHM)
Step 1: Start the application.
Step 2: Define the valid choices: Rock, Paper, Scissor.
Step 3: Initialize the game loop.
Step 4: The computer selects a random choice from the tuple.
Step 5: The user is prompted to enter their choice.
Step 6: Validation Check: If the input is not in the valid choices, prompt the user again.
Step 7: Comparison Logic:
    - If User == Computer: Result is Draw.
    - If User beats Computer (e.g., Rock vs. Scissor): Result is Win.
    - Otherwise: Result is Lose.
Step 8: Output the Computer's choice and the Game Result.
Step 9: Replay Check: Ask the user if they wish to play again (y/n).
    - If 'y', repeat from Step 4.
    - If 'n', exit the loop.
Step 10: End the application.

5. SYSTEM REQUIREMENTS
- Operating System: Windows, macOS, or Linux.
- Software: Python 3.x Interpreter.
- Interface: Command Line Interface (CLI) / Terminal.

6. CONCLUSION
This project successfully demonstrates the use of fundamental Python programming concepts such as loops, conditional branching, and module integration to create an interactive and bug-free game experience.
