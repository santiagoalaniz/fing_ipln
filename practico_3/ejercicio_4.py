import numpy as np
from numpy import log, exp
import math
import pdb

# Constantes del algoritmo

## Funciones de numpy (ln y exp)
ln = log
e = exp
ZERO = 1e-15

## Constantes del algoritmo de Viterbi
### Tags (etiquetas) del modelo
tags = ['<s>', 'DET', 'V', 'ADJ', 'N']

### Frase a analizar (tokenizada)
sentence_words = ['unas', 'blancas', 'velas']

### Definir las probabilidades de transición P(tag_i|tag_j)
trans_prob  = np.array(
  [
    [ZERO, 0.32, 0.03, 0.01, 0.12],
    [ZERO, 0.03, ZERO, 0.09, 0.8],
    [0.05, 0.25, 0.15, 0.05, 0.06],
    [0.19, 0.02, 0.05, 0.03, 0.21],
    [0.53, 0.01, 0.08, 0.15, 0.02]
  ]
)

### Definir las probabilidades de emisión P(palabra|tag)
emi_prob = {
  ('unas', 'DET'): 0.0020,
  ('unas', 'V'): 0.000045,
  ('blancas', 'ADJ'): 0.00029,
  ('blancas', 'N'): 0.000023,
  ('velas', 'N'): 0.000029,
  ('velas', 'V'): 0.000045
}

def main():
  # Uno de los algoritmos ampliamente utilizados para determinar las etiquetas (tags)
  # de una frase en procesamiento del lenguaje natural es el algoritmo de Viterbi.
  # El algoritmo de Viterbi es un algoritmo de programación dinámica que se utiliza para encontrar
  # la secuencia más probable de estados ocultos en un modelo de Markov oculto (HMM).
  viterbi_algorithm()
  return 0

def viterbi_algorithm():
  V = np.full((len(tags), len(sentence_words)), 0.0)
  B = np.full((len(tags), len(sentence_words)), 0)

  # Inicialización
  # Se calcula la probabilidad de que la primera palabra de la frase sea de cada una de 
  # las etiquetas
  for i in range(len(tags)):
    if (sentence_words[0], tags[i]) in emi_prob:
      V[i, 0] = ln(trans_prob[0, i]) + ln(emi_prob[(sentence_words[0], tags[i])])
    else:
      V[i, 0] = ln(trans_prob[0, i]) + ln(ZERO)
    
    B[i, 0] = i
  
  # Recursión
  for t in range(1, len(sentence_words)):
    for i in range(len(tags)):
      max_value = -math.inf
      max_index = -1
      for j in range(len(tags)):
        if (sentence_words[t], tags[i]) in emi_prob:
          value = V[j, t-1] + ln(trans_prob[j, i]) + ln(emi_prob[(sentence_words[t], tags[i])])
        else:
          value = V[j, t-1] + ln(trans_prob[j, i]) + ln(ZERO)
        if value > max_value:
          max_value = value
          max_index = j
      V[i, t] = max_value
      B[i, t] = max_index
  
  print(V)
  print(B)
  return 0

if __name__ == '__main__':
  main()
