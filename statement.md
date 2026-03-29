# Project Statement: AI-Powered TicTacToe
> **Course:** Fundamentals of AI & ML  
> **Author:** Gaurav Tiwari (First-Year CSE, VIT Bhopal)

## 1. Problem Statement
The goal of this project is to bridge the gap between simple game logic and **Adversarial Search**. While a standard Tic Tac Toe game follows basic "if-else" rules, this project implements a **Minimax-based AI** to demonstrate how an agent can evaluate the entire state space of a problem to make optimal decisions. The "problem" being solved is creating a digital opponent that can simulate human foresight and never lose a game.

## 2. Scope of the Project

### In-Scope:
* **Core Logic:** A fully functional, terminal-based Tic Tac Toe engine.
* **Human vs. AI:** A seamless gameplay loop allowing a human player to challenge the computer.
* **Minimax Integration:** Implementation of the Minimax algorithm for optimal, "unbeatable" gameplay.
* **Game State Management:** Real-time detection of wins, losses, draws, and illegal moves.
* **UX:** Basic input validation (1–9) and a quit option for a smooth user experience.

### Out-of-Scope:
* **Advanced Optimization:** Heuristic pruning (Alpha-Beta pruning) is excluded to keep the "Fundamentals" focus clear.
* **Network Play:** No online multiplayer or socket programming.
* **Cross-Platform Apps:** This project is focused on the logic (Terminal/GUI) rather than mobile or web deployment.

## 3. Target Users
* **Beginners:** Those looking to understand how Recursion and State-Trees work in Python.
* **Educators:** Professors looking for a clean, well-documented example of Adversarial Search.
* **Gamers:** Anyone looking to test their skills against a mathematically perfect opponent.

## 4. High-Level Features
* **Optimal Play:** The AI uses a recursive search to ensure it always picks the best possible move.
* **Terminal Interface:** A lightweight, numbers-based (1–9) input system for quick gameplay.
* **Smart Validation:** Prevents players from picking occupied spots or entering invalid data.
* **Instant Evaluation:** Automatic detection of terminal states (Win/Loss/Draw) immediately after a move is made.
* **Code Clarity:** Written with a focus on readability and "beginner-friendly" structure, making it easy to audit for academic purposes.

---
*This project serves as a practical application of search algorithms studied in the series of AI & ML fundamentals.*
