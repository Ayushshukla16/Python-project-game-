# Rock Paper Scissor Game 🎮

A Python-based console application that allows users to play the classic "Rock, Paper, Scissors" game against a computer opponent. The project demonstrates the use of random choices, conditional logic, and loops for continuous gameplay.

## 📄 Description

This program runs a simulation of the zero-sum hand game. The user inputs their choice (Rock, Paper, or Scissor), and the computer randomly selects a counter-move. The winner is determined by standard game rules:
* **Rock** beats Scissors
* **Scissors** beats Paper
* **Paper** beats Rock

The game runs inside a loop, allowing the user to play multiple rounds until they choose to exit.

## ✨ Key Features

* **Randomized AI:** Uses Python's `random` module to ensure the computer's moves are unpredictable.
* **Input Validation:** The program checks if the user's input is valid (`rock`, `paper`, or `scissor`). If the input is incorrect, it prompts the user again.
* **Replay Functionality:** After every round, the user is asked if they want to play again (`y/n`).
* **Case Handling:** User input is automatically converted to lowercase to prevent errors.

## 🛠️ Prerequisites

* **Python 3.x** installed on your system.

## 🚀 How to Run

1.  Download the file `rock papaer scissor.py`.
2.  Open your terminal or command prompt.
3.  Navigate to the folder where the file is saved.
4.  Run the script using the following command:

    ```bash
    python "rock papaer scissor.py"
    ```

## 🕹️ Usage Guide

1.  Launch the program.
2.  When prompted `enter rock, paper, or scissor:`, type your move.
3.  The computer will display its choice.
4.  The result (Win, Lose, or Draw) will be printed.
5.  Type `y` to play another round, or any other key to exit.

## 📂 Code Structure

* **Libraries:** Imports `random` for AI logic.
* **Variables:** * `choice`: Tuple containing the valid moves.
    * `akash`: Boolean flag used to control the main game loop.
* **Logic:**
    * `while` loops are used for the game session and input validation.
    * `if-elif-else` blocks handle the win/loss comparison logic.
