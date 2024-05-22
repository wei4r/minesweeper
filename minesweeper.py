import random

class Minesweeper:
	def __init__(self, grid_size, num_mines):
		self.grid_size = grid_size
		self.num_mines = num_mines
		self.board = [['' for _ in range(grid_size)] for _ in range(grid_size)]
		self.mines = set()

	def generate_board(self, first_click_row, first_click_col):
		positions = [(row, col) for row in range(self.grid_size) for col in range(self.grid_size)]
		positions.remove((first_click_row, first_click_col))

		mine_positions = random.sample(positions, self.num_mines)
		self.mines = set(mine_positions)

		for row, col in mine_positions:
			self.board[row][col] = 'M'

		self.calculate_adjacent_mines()
		return self.board

	def calculate_adjacent_mines(self):
		directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
		for row in range(self.grid_size):
			for col in range(self.grid_size):
				if self.board[row][col] == 'M':
					continue
				mine_count = 0
				for dr, dc in directions:
					r, c = row + dr, col + dc
					if 0 <= r < self.grid_size and 0 <= c < self.grid_size and self.board[r][c] == 'M':
						mine_count += 1
				self.board[row][col] = str(mine_count)

	def reveal(self, row, col):
		return self.board[row][col]

	def get_mine_positions(self):
		return self.mines

# Example Usage
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
