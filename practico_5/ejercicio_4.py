import nltk
from nltk import CFG, parse

grammar = nltk.CFG.fromstring("""
O -> GV
GV -> V GN | V GN GP
GN -> N | N GP
GP -> P GN
N -> 'tomo' | 'agua' | 'manzana' | 'manzanas' | 'Pepe' | 'María'
V -> 'tomo' | 'toma' | 'tomamos' | 'toman'
P -> 'de' | 'con' | 'para'
""")

def main():
  txt = "tomo agua de manzana"
  Earley_algorithm(txt= txt)

def Earley_algorithm(txt: str):
  txt_tokenized = txt.split()
  parser = nltk.parse.EarleyChartParser(grammar)
  parses = parser.parse(txt_tokenized)

  for tree in parses:
    tree.pretty_print()

if __name__ == "__main__":
  main()

# b) Analicemos las posibles ambigüedades sintácticas de la oración dada.
# En este caso, no hay ambigüedades sintácticas en la oración "Tomo agua de manzana".
# El algoritmo de Earley encuentra un solo árbol de análisis válido para esta oración,
# utilizando la gramática dada.
# Al igual que el algoritmo CKY, el algoritmo de Earley es capaz de detectar ambigüedades
# en las oraciones si existen.

# c) Si se agrega la regla O → GN GV a la gramática, no se reconocerían oraciones
# agramaticales adicionales. La nueva regla simplemente permite que las oraciones comiencen
# con un grupo nominal seguido de un grupo verbal. Todas las oraciones generadas por la
# gramática con esta regla adicional seguirán siendo gramaticales, ya que la gramática
# original ya permite la generación de oraciones gramaticales. La adición de esta regla no
# introduce ninguna estructura inválida o agramatical.
