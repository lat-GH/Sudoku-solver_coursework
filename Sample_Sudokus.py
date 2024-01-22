import numpy as np

# Load sudokus
#sudoku = np.load("data/very_easy_puzzle.npy")

"""
sudoku = np.load("C:/Users/latma/OneDrive/Documents/ComputerScience_Yr2/AI/sudoku/data/very_easy_puzzle.npy")
print("very_easy_puzzle.npy has been loaded into the variable sudoku")
print(f"sudoku.shape: {sudoku.shape}, sudoku[0].shape: {sudoku[0].shape}, sudoku.dtype: {sudoku.dtype}")

# Load solutions for demonstration
solutions = np.load("C:/Users/latma/OneDrive/Documents/ComputerScience_Yr2/AI/sudoku/data/very_easy_solution.npy")
print()

# Print the first 9x9 sudoku...
print("First sudoku:")
print(sudoku[0], "\n")

# ...and its solution
print("Solution of first sudoku:")
print(solutions[0])
"""

sudoku = np.load("C:/Users/latma/OneDrive/Documents/ComputerScience_Yr2/AI/sudoku/data/hard_puzzle.npy")
print("hard_puzzle.npy has been loaded into the variable sudoku")
print(f"sudoku.shape: {sudoku.shape}, sudoku[0].shape: {sudoku[0].shape}, sudoku.dtype: {sudoku.dtype}")

# Load solutions for demonstration
solutions = np.load("C:/Users/latma/OneDrive/Documents/ComputerScience_Yr2/AI/sudoku/data/hard_solution.npy")
print()

# Print the first 9x9 sudoku...
print("First sudoku:")
print(sudoku[0], "\n")

# ...and its solution
print("Solution of first sudoku:")
print(solutions[0])