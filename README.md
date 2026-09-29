# Tic-Tac-Toe with Minimax AI

A command-line Tic-Tac-Toe game in Python where you play as **X** against an AI opponent (**O**) that picks its moves using the **Minimax algorithm**.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [How to Play](#how-to-play)
4. [How the Minimax AI Works](#how-the-minimax-ai-works)
5. [Installation & Usage](#installation--usage)
6. [Code Walkthrough](#code-walkthrough)
7. [Sample Gameplay](#sample-gameplay)
8. [Limitations](#limitations)
9. [Future Improvements](#future-improvements)
10. [Author](#author)

---

## Overview

Tic-Tac-Toe is a small, fully solvable game, which makes it a good way to learn adversarial search. This project implements the game in plain Python (no external libraries) and uses Minimax to let the computer choose its moves by looking ahead through possible game states.

---

## Features

- Play in the terminal against a computer opponent
- AI decision-making with the Minimax algorithm
- Simple 3x3 board rendered in text
- Detects wins for both sides and draws
- Pure Python, no dependencies

---

## How to Play

- You are **X**, the AI is **O**.
- The board positions are numbered **1 to 9**, left to right, top to bottom:

```
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

- Enter the number of the cell where you want to place your X.
- First to get three in a row (horizontal, vertical or diagonal) wins. If the board fills up, it's a draw.

---

## How the Minimax AI Works

Minimax is a recursive algorithm for two-player, turn-based games. It explores the game tree of possible moves and assumes both players play as well as they can.

- The AI (**O**) is the **maximizing** player: it wants the highest score.
- You (**X**) are the **minimizing** player: you want the lowest score.
- Terminal board states are scored:

| Outcome | Score |
|---|---|
| AI (O) wins | +1 |
| Draw | 0 |
| Human (X) wins | -1 |

For every empty cell, the AI tries a move, recursively simulates the rest of the game, undoes the move, and keeps the move with the best score.

---

## Installation & Usage

**Requirements:** Python 3.x (no extra packages)

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
python "TIC-TAC-TOE USING MINIMAX.py"
```

---

## Code Walkthrough

| Function / Section | Purpose |
|---|---|
| `b = [' '] * 9` | Board stored as a flat list of 9 cells |
| `show()` | Prints the board to the terminal |
| `win(p)` | Checks all 8 winning lines for player `p` |
| `minimax()` | Recursively scores board states |
| Main loop | Takes player input, checks results, and picks the AI's best move |

---

## Sample Gameplay

```
TIC-TAC-TOE
You = X   AI = O
  |   |
--+---+--
  |   |
--+---+--
  |   |
Enter position (1-9): 5
```

> Add your own terminal screenshot here.

---

## Limitations

- Terminal only, no graphical interface
- Basic input handling (expects a number from 1 to 9)
- Human always moves first
- No score tracking or replay option

---

## Future Improvements

- Input validation (occupied cells, non-numeric input)
- Option to choose X or O and who goes first
- Alpha-beta pruning to speed up the search
- Difficulty levels
- GUI version (Tkinter or a web page)
- Play-again loop with a score counter

---

## Author

**Rhamya Sri**
Second-year B.E. Computer Science and Engineering student, Hindusthan College of Technology
LinkedIn: [linkedin.com/in/rhamyasri-kathiravan](https://linkedin.com/in/rhamyasri-kathiravan)
