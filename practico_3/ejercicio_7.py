import numpy as np
from numpy import log, exp

#Constantes del Ejercicio
tags = ['<s>', 'DET', 'NOM', 'ADJ', '</s>']

counts = {
  ('<s>', 'DET'): 18,
  ('<s>', 'NOM'): 9,
  ('<s>', 'ADJ'): 3,

  ('DET', 'NOM'): 21,
  ('DET', 'ADJ'): 18,
  ('DET', 'DET'): 0,
  ('DET', '</s>'): 0,

  ('NOM', 'NOM'): 9,
  ('NOM', 'ADJ'): 9,
  ('NOM', 'DET'): 0,
  ('NOM', '</s>'): 0,

  ('ADJ', 'NOM'): 21,
  ('ADJ', 'ADJ'): 0,
  ('ADJ', 'DET'): 0,
  ('ADJ', '</s>'): 9,
}

# parte a)
def naive_bayes_classfier(ant:str, tags:List(str), sig:str) -> List(float): 
  # El clasificador de Naive Bayes asume eventos independientes, en este caso,
  # la etiqueta POS de una palabra es independiente de las demas.
  # La probabilidad de una etiqueta dadas la siguiente y anterior es:
  # P(tag_i|tag_j, tag_k) = P(tag_i|tag_j) * P(tag_i|tag_k) * P(tag_i)
  # Buscamos maximizar con tag_j = ant y tag_k = sig fijos.
  # max P(tag_i|ant, sig) para todo tag_i en una lista de tags.
  # Asumiendo equiprobabilidad de las etiquetas, P(tag_i) = 1/len(tags) = CTE
  # P(tag_i|ant, sig) = P(tag_i|ant) * P(tag_i|sig) * CTE
  # max P(tag_i|ant, sig) ~= max P(tag_i|ant) * P(tag_i|sig)

  result = []
  for tag in tags:
    p_tag

  return 0

def main():
  # parte b)
  result = naive_bayes_classfier(
    ant='DET',
    tags=['NOM', 'ADJ', 'DET'],
    sig='NOM'
  )
  return 0

if __name__ == '__main__':
  main()
