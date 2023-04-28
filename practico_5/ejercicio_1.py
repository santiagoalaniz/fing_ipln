import nltk
from nltk import CFG, parse

grammar_str = """
O   -> GV
GV   -> V GN | V GN GP
GN   -> N | N GP
GP   -> P GN
N    -> 'tomo' | 'agua' | 'manzana' | 'manzanas' | 'Pepe' | 'María'
V    -> 'tomo' | 'toma' | 'tomamos' | 'toman'
P    -> 'de' | 'con' | 'para'
"""

grammar = CFG.fromstring(grammar_str)

def main():
  txt = 'tomamos agua con María'
  CKY_algorithm(txt= txt)

def CKY_algorithm(txt: str):
  txt_tokenized = txt.split()
  parser = nltk.parse.ChartParser(grammar)
  chart = parser.chart_parse(txt_tokenized)
  parse_trees = list(chart.parses(grammar.start()))

  for tree in parse_trees:
    tree.pretty_print()
    print("Matrix (chart):")
    for edge in sorted(chart.edges(), key=lambda edge: (edge.start(), edge.end())):
      print(edge)

if __name__ == "__main__":
  main()
