# Minesweeper Module

This repository contains a Minesweeper module implemented in Python. The module handles the core logic of the Minesweeper game, including board generation and mine placement.

## Requirements

- Python 3.x

## Installation

To run the Minesweeper module, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/wei4r/minesweeper.git
    cd minesweeper-module
    ```

2. Run the script:
    ```sh
    python minesweeper.py
    ```

## Usage

The Minesweeper module can be used to generate a Minesweeper board and place mines while ensuring the first clicked cell is safe. Below is an example usage:

```python
from minesweeper import Minesweeper

grid_size = 10
num_mines = 20
first_click_row = 0
first_click_col = 0

minesweeper = Minesweeper(grid_size, num_mines)
board = minesweeper.generate_board(first_click_row, first_click_col)
mine_positions = minesweeper.get_mine_positions()

print("Board:")
for row in board:
    print(" ".join(row))

print("\nMine Positions:")
print(mine_positions)
