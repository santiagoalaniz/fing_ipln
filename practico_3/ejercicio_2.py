
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Lista de clasificaciones y comentarios
reviews = [
  "Buenísima.",
  "Escenas traídas de los pelos.",
  "No me gustó la película.",
  "Horrible. Me aburrí como un hongo.",
  "Muy buena la película. La super recomiendo.",
  "Muy linda película.",
  "Me gustó. La recomiendo totalmente.",
  "No la recomiendo. Es un divague.",
  "Una historia que es un mamarracho.",
]
puntuaciones = ["+", "-", "-", "-", "+", "+", "+", "-", "-"]

nltk.download('stopwords')
stopwords_es = set(stopwords.words('spanish'))
nltk.download('punkt')

def preprocess(text: str) -> str:
  text = text.lower()
  text = re.sub(r"[^\w\s]", "", text)
  text = word_tokenize(text)
  text = [word for word in text if word not in stopwords_es]
  return text

def analysis(text: str, bag_of_words: dict) -> None:
  print(f"Análisis de la frase: {text}")
  text = preprocess(text)
  print(f"Palabras: {text}")

  n = len(bag_of_words) + 1
  pos = 1
  neg = 1
  for word in text:
    if word not in bag_of_words:
      continue
    pos += bag_of_words[word]["+"]
    neg += bag_of_words[word]["-"]

  pos = pos / n
  neg = neg / n

  print(f"Probabilidad de que sea positiva: {pos}")
  print(f"Probabilidad de que sea negativa: {neg}")

  if pos > neg:
    print("La frase es positiva")
  elif pos < neg:
    print("La frase es negativa")
  else:
    print("La frase es neutra")


def main():
  reviews_preprocessed = [preprocess(review) for review in reviews]
  vocabulary = set([word for review in reviews_preprocessed for word in review])
  reviews_preprocessed = list(zip(reviews_preprocessed, puntuaciones))
  bag_of_words = {}

  for word in vocabulary:
    positive = 0
    negative = 0

    for review in reviews_preprocessed:
      if word in review[0]:
        if review[1] == "+":
          positive += 1
        else:
          negative += 1
    entry = {
      word: {
        "+": positive,
        "-": negative
      }
    }
    bag_of_words.update(entry)

  analysis("Muy buena, la recomiendo", bag_of_words)
  analysis("jaaa un mamarracho", bag_of_words)
  analysis("Una verdadera pérdida de tiempo. Linda para dormir la siesta", bag_of_words)
  analysis("Fui con mi familia, pasamos genial", bag_of_words)





if __name__ == "__main__":
  main()
