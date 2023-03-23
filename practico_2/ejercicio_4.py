from ejercicio_3 import edit_distance

CANDIDATES = ['MAREO', 'APAREO']
TYPO = 'AAREOO'

def main():
  result = correction(TYPO, CANDIDATES)
  print(f"{result}")


def correction(typo, candidates):
  # Initialize the result
  edit_distances = []

  # Iterate over the candidates
  for candidate in candidates:
    edit_distances.append(edit_distance(typo, candidate))

  # Get the index of the candidate with the minimum edit distance
  candidate_index = edit_distances.index(min(edit_distances))

  result = {
    'typo': typo,
    'candidate': candidates[candidate_index],
    'edit_distance': edit_distances[candidate_index],
    'candidates': candidates,
    'edit_distances': edit_distances
  }

  return result



if __name__ == "__main__":
  main()
