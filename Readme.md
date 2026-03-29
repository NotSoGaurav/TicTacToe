### 🕹️ Project Oracle: The Unbeatable TicTacToe

## A Fundamentals of AI & ML Project | Gaurav Tiwari, VIT Bhopal

Welcome to Project Oracle, a high-performance TicTacToe implementation designed to demonstrate Adversarial Search. This isn't just a game; it is a recursive engine that evaluates every possible future to ensure the AI never loses.

## 🌟 Project Overview

How does a machine "think" steps ahead? This project uses the Minimax Algorithm to simulate perfect decision-making. Whether you use the lightweight Terminal interface or the modern GUI, you are playing against a mathematically optimized opponent.

The AI Core

Algorithm: Minimax (Recursive State-Space Search)

Optimization: Depth-based scoring (The AI wins as fast as possible)

Performance: Real-time evaluation of ~500,000 potential board states.

## 🚀 Setup & Execution (Step-by-Step)

1. Prerequisites

Ensure you have Python 3.x installed. You can check this by running:

python --version


2. Installation

Clone the repository to your local machine:

git clone [https://github.com/NotSoGaurav/TicTacToe.git](https://github.com/NotSoGaurav/TicTacToe.git)
cd TicTacToe


3. Running the Project

The project offers two ways to play. Choose the one that suits your environment:

. Option A: Terminal Interface (Recommended for speed)

python main.py


How to play: Enter a number from 1 to 9 corresponding to the grid position. Type q to exit.

. Option B: GUI Interface (Best for UX)

python main_gui.py


How to play: Simply click the squares to place your 'X'. The AI ('O') will respond instantly.

## 🧪 Testing Scenarios for Evaluators

- To verify the AI's "Intelligence," try the following:

- The Stalemate: Play your best game. If you play perfectly, the AI will force a Draw.

- The Trap: Try to set up a "double-win" (a fork). Watch as the AI detects and blocks it before you can finish.

- Input Validation: In the terminal, try entering a letter or a number already taken. The system will prevent the move and ask for a valid one.

## 📂 Tech Stack

**Language:** Python 3.10

**Framework:** Standard Library (No external dependencies required)

**GUI:** Tkinter
=======
GUI Library: Tkinter (Standard Python Library)
