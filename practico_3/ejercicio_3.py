from numpy import log
from math import exp
import pdb

ln = log

WORDS_COUNT = 192685
PHRASES_COUNT = 6030
VOCABULARY_COUNT = 1320

UNIGRAMS = {
    '<s>': PHRASES_COUNT,
    'Me': 5,
    'pegué': 0,
    'en': 4340,
    'la': 6412,
    'cabeza': 28,
    'las': 1832,
    'oreja': 0,
    '.': 5866,
    '</s>': PHRASES_COUNT,
}

BIGRAMS = {
    '<s> Me': 5,
    'Me pegué': 0,
    'pegué en': 0,
    'en la': 703,
    'la cabeza': 13,
    'en las': 190,
    'las cabeza': 0,
    'la oreja': 0,
    'oreja .': 0,
    'cabeza .': 0,
    '. </s>': 5842,
}

TEST_PHRASES = [
    'Me pegué en la cabeza .',
    'Me pegué en la oreja .',
    'Me pegué en las cabeza .',
]
# MODEL = UNIGRAMS + BIGRAMS + CONSTANTS
# P(MODEL | Me pegue en la cabeza .):   0.30,
# P(MODEL | Me pegue en la oreja .):    0.20,
# P(MODEL | Me pegue en las cabeza .):  0.50,
CERTAINTY = [
    0.30,
    0.20,
    0.50,
]

def main():
    most_probable_phrase()

# Parte b)
# Bayesian rule:
#   P(TEST_PHRASE|MODEL) = P(MODEL|TEST_PHRASE) * ln(P(TEST_PHRASE)) / P(MODEL)
#   ln(TEST_PHRASE|MODEL) = ln(MODEL|TEST_PHRASE) + ln(P(TEST_PHRASE)) - ln(MODEL)
#       - ln(x) is an always decreasing function in [0, 1], so it doesn't affect the result
#       - P(MODEL) is the same for all phrases, so we can ignore it
#   ln(TEST_PHRASE|MODEL) ~= ln(MODEL|TEST_PHRASE) + ln(P(TEST_PHRASE))
#       - P(MODEL|TEST_PHRASE) is given in the dictionary CERTAINTY
#       - ln(P(TEST_PHRASE)) is calculated in the function laplace_smoothing
def most_probable_phrase():
    laplace_results = [laplace_smoothing(phrase) for phrase in TEST_PHRASES]
    pharse_score = [
        laplace_result + ln(CERTAINTY[i]) for i, laplace_result in enumerate(laplace_results)
    ]

    for i, score in enumerate(pharse_score):
        print(f'ln(P(MODEL | "{TEST_PHRASES[i]}"))    = {score}')
        print(f'    ln(P("{TEST_PHRASES[i]}"))        = {laplace_results[i]}')

    max_score_pharse = TEST_PHRASES[pharse_score.index(max(pharse_score))]
    print(f'\nLa frase más probable es: "{max_score_pharse}"')

# Parte a)
# El suavizado de Laplace soluciona el problema de los bigramas nulos
# Calculamos la probabilidad de la frase
    # Sean wi-1 y wi dos palabras consecutivas (un bigrama)
    # TEST_PHRASE = w0 w1 w2 ... wn
    # P(TEST_PHRASE) = PROD(P(wi|wi-1)) = (count(wi-1, wi) + 1) / (count(wi-1) + V)
    #   PROD(P(wi|wi-1)) ~> 0, usamos logaritmo para evitar underflow
    #   count(wi-1, wi) = BIGRAMS[wi-1 wi]
    #   count(wi-1) = UNIGRAMS[wi-1]
def laplace_smoothing(text: str) -> float:
    bigrams_list = bigrams_split(text)
    P_text = 0

    for bigram in bigrams_list:
        x = {'wi-1 wi': bigram[0], 'wi-1': bigram[1], 'wi': bigram[2]}
        P_text += ln((BIGRAMS[x['wi-1 wi']] + 1) / (UNIGRAMS[x['wi-1']] + VOCABULARY_COUNT))

    return P_text

# Dividimos el texto en bigramas
def bigrams_split(text: str) -> list:
    text = '<s> ' + text + ' </s>'
    words = text.split(' ')
    bigrams = []

    for i in range(len(words) - 1):
        bigrams.append((words[i] + ' ' + words[i + 1], words[i], words[i + 1]))

    return bigrams

if __name__ == '__main__':
    main()
