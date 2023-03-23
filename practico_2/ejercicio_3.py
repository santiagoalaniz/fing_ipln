import numpy as np
import pdb

WORD_1 = 'REDUCCION'
WORD_2 = 'DURACION'

def main():
  print(f"Distancia de edicion entre {WORD_1} y {WORD_2}: {edit_distance(WORD_1, WORD_2)}")

def edit_distance(word_1, word_2):
  return levenstein_matrix(word_1, word_2)[-1][-1]

def levenstein_matrix(word_1, word_2):
  # Initialize the matrix
  matrix = np.zeros((len(word_1) + 1, len(word_2) + 1), dtype=int)

  # Fill the first row and column
  for i in range(len(word_1) + 1): matrix[i, 0] = i
  for j in range(len(word_2) + 1): matrix[0, j] = j

  # Fill the rest of the matrix
  for i in range(1, len(word_1) + 1):
    for j in range(1, len(word_2) + 1):
      substitution_cost = 0 if word_1[i - 1] == word_2[j - 1] else 2

      matrix[i, j] = min(
        matrix[i - 1, j - 1] + substitution_cost,
        matrix[i - 1, j] + 1,
        matrix[i, j - 1] + 1,
      )

  return matrix

if __name__ == "__main__":
  main()
