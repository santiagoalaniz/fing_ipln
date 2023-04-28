import nltk
from nltk import CFG, parse

grammar_str = """
O -> GN GV
GN -> N | N GP | D GN
GV -> V | V GN | GV GP
GP -> P GN
D -> 'el' | 'la' | 'los' | 'las'
N -> 'bajo' | 'mesa' | 'bajos' | 'mesas' | 'madera'
V -> 'está' | 'están' | 'bajo' | 'baja'
P -> 'bajo' | 'de'
"""

grammar = CFG.fromstring(grammar_str)

def main():
  txt = 'el bajo está bajo la mesa de madera'
  CKY_algorithm(txt= txt)

def CKY_algorithm(txt: str):
  txt_tokenized = txt.split()
  parser = nltk.parse.ChartParser(grammar)
  chart = parser.chart_parse(txt_tokenized)
  parse_trees = list(chart.parses(grammar.start()))

  for tree in parse_trees:
    tree.pretty_print()

if __name__ == "__main__":
  main()

# Todos los posibles análisis sintácticos son recuperables a partir de la tabla correspondiente
# a la aplicación del algoritmo CKY, ya que el algoritmo CKY es completo y garantiza encontrar
# todos los análisis posibles para una oración dada, siempre que la gramática CNF.
