import re

ENTRY = 'Este es un texto de prueba para el ejercicio 1 del practico 2'

def main():
    tagged_text = hashtag_generator()
    print(tagged_text)

    substituted_text = hashtag_matcher(text=tagged_text)
    print(substituted_text)


def hashtag_generator(text=ENTRY):
  result = re.sub(r'(\w+)', r'#\1', text)
  return result

def hashtag_matcher(text=str):
  result = re.sub(r'#', 'HASHTAG_', text)
  return result


if __name__ == "__main__":
    main()
