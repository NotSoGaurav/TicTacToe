## 🕹️ TicTacToe: The Unbeatable Brain

A "Fundamentals of AI & ML" Project | Gaurav Tiwari, VIT Bhopal

Welcome to TicTacToe AI, a project that turns a childhood game into a demonstration of Adversarial Search. Built for my first-year course, this project explores how a computer "thinks" steps ahead to ensure it never loses.

## 🌟 Overview

Have you ever wondered if a machine can truly "outsmart" a human in a game of logic? This project answers that with a Minimax-powered AI. Whether you're playing in the classic Terminal or the sleek GUI, you're up against an algorithm that calculates every possible future move in milliseconds.

The "Real-World" Connection

In our daily lives—from navigating traffic to playing sports—we constantly use predictive logic. I built this to observe how Recursive AI can mimic this human behavior to achieve a "Perfect Play" state.

# 🚀 Key Features

- 🧠 God-Mode AI: Powered by the Minimax Algorithm. It doesn't just play; it calculates your defeat.

- 🎮 Dual Interface: * main.py: For the classic, hacker-style Terminal experience.

main_gui.py: A modern Graphical User Interface for better UX.

- 🛡️ Fool-Proof Logic: Built-in validation to handle invalid inputs or occupied positions gracefully.

- ⚡ Lightweight: Written in pure Python—no heavy external libraries required.

# 🛠️ How the AI "Thinks"

This isn't just a set of *"if-else"* rules. It uses *State-Space* Search:

- Evaluation:  The AI looks at the board and assigns a score (+10 for an AI win, -10 for a Human win).

- Minimaxing: It recursively simulates every possible game outcome to Maximize its own score while Minimizing yours.

- Recursion: It plays thousands of "mental games" before making a single move on your screen!

### 📥 Getting Started

1. Clone the Brain

git clone [https://github.com/NotSoGaurav/TicTacToe.git](https://github.com/NotSoGaurav/TicTacToe.git)
cd TicTacToe


2. Choose Your Battle

For the Terminal version:

python main.py


For the GUI version:

python main_gui.py


# 🧪 Can You Beat It?

The AI is designed to be unbeatable. Here is how you can test its "Intelligence":

The Center Trap: Does it always prioritize the middle square (Position 5)?

The Fork Test: Can you create two ways to win? (Spoiler: The AI will block you before you can!)

Robustness: Try typing "10", "abc", or choosing an occupied spot to see the error handling.

# 📂 Tech Stack

Language: Python 3.x

Core Logic: Minimax Algorithm (Adversarial Search)

GUI Library: Tkinter (Standard Python Library)

Created by Gaurav Tiwari, a first-year CSE student at VIT Bhopal.