import nltk
from nltk import CFG, parse

grammar = nltk.CFG.fromstring("""
O -> GN GV
GV -> V GN | V
GN -> Det Nom | Nom
Nom -> 'Juan' | 'perro' | 'galletas'
Det -> 'el' | 'la'
V -> 'come' | 'salta'
""")

def main():
  txt = "Juan come galletas"
  Earley_algorithm(txt= txt)

def Earley_algorithm(txt: str):
  txt_tokenized = txt.split()
  parser = nltk.parse.EarleyChartParser(grammar)
  parses = parser.parse(txt_tokenized)

  for tree in parses:
    tree.pretty_print()

if __name__ == "__main__":
  main()
