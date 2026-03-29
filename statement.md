### Project Statement: AI-Powered TicTacToe (Project Oracle)
# Course: Fundamentals of AI & ML

1. Problem Statement

The objective of Project Oracle is to solve the "perfect play" problem in a 3x3 grid environment. While human players often make sub-optimal moves due to fatigue or oversight, this project implements an Adversarial Search agent using the Minimax Algorithm. The goal is to provide a robust demonstration of how AI can evaluate a complete state-space to reach a terminal state that is either a "Win" or a "Draw," never a "Loss."

2. Scope of the Project

- In-Scope:

Recursive Decision Making: Implementation of a depth-aware Minimax algorithm.

Game Engine: A state-management system that tracks board positions and validates moves.

Hybrid Interface: Support for both Command Line (CLI) and Graphical User Interface (GUI).

Instructional Logic: Code structure designed for academic auditing and algorithm transparency.

- Out-of-Scope:

Heuristic Pruning: Alpha-Beta pruning is omitted to allow evaluators to see the full breadth of the search tree.

Cloud Integration: The project is a standalone local application to ensure zero latency during evaluation.

3. Target Users

A. Academic Evaluators: Professors auditing the application of search algorithms in code.
B. CSE Students: Peers looking for a reference implementation of recursion in game theory.
C. Logic Enthusiasts: Users interested in testing human intuition against mathematical 
   certainty.

4. High-Level Features

Optimal Policy Execution: The AI never deviates from the statistically best move.

Dynamic Validation: The engine prevents "Illegal State" transitions (overlapping moves).

Instant Evaluation: Terminal state detection (Win/Loss/Draw) occurs in $O(1)$ time after each move.

**Educational Architecture: The code is modular, separating the AI "Brain" from the "Interface," following standard software engineering principles.**