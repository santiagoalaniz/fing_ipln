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
tags = ['<s>', 'PREP', 'DET', 'V', 'NN']

### Frase a analizar (tokenizada)
sentence_words = ['sobre', 'el', 'sobre']

### Definir las probabilidades de transición P(tag_i|tag_j)
trans_prob = np.array(
  [
    [ZERO, 0.2, 0.05, 0.1, 0.1],
    [ZERO, ZERO, 0.5, 0.1, 0.1],
    [ZERO, ZERO, ZERO, ZERO, 0.1],
    [0.3, 0.1, 0.1, 0.2, 0.2],
    [0.2, 0.2, 0.1, 0.1, 0.3]
  ]
)

### Definir las probabilidades de emisión P(palabra|tag)
emi_prob = {
  ("sobre", "PREP"): 0.07,
  ("sobre", "V"): 0.0012,
  ("sobre", "N"): 0.00062,
  ("el", "DET"): 0.4,
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
  
  end_column_index = len(sentence_words) - 1
  end_row_index = np.argmax(V[:, -1])
  sentence_tags = []

  while end_column_index >= 0:
    sentence_tags.append(tags[end_row_index])
    end_row_index = B[end_row_index, end_column_index]
    end_column_index -= 1

  print(list(zip(sentence_words,sentence_tags[::-1])))
  return 0

if __name__ == '__main__':
  main()

# La principal diferencia entre el algoritmo Viterbi y el algoritmo Forward es su propósito 
# y la información que proporcionan:

# - El algoritmo de Viterbi se utiliza para determinar la secuencia de estados ocultos más probable 
#   que produjo una secuencia dada de observaciones. En otras palabras, responde a la pregunta: 
#   "Dada esta secuencia de observaciones, ¿cuál es la secuencia de estados ocultos más probable 
#   que las produjo?".

# - El algoritmo Forward, por otro lado, se utiliza para calcular la probabilidad de una secuencia 
#   de observaciones sin tener en cuenta la secuencia específica de estados. Responde a la pregunta: 
#   "¿Cuál es la probabilidad de observar esta secuencia de observaciones con nuestro modelo actual,
#    sumando sobre todas las posibles secuencias de estados ocultos?".

# Por lo tanto, la principal diferencia radica en el tipo de pregunta que cada algoritmo está 
# diseñado para responder.