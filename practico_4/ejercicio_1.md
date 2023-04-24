# Ejercicio 1

## a) Construir gramaticas que generen las siguientes preposiciones:

i)
  - estudia musica
  - estudia musica con profesor particular
  - caminaba por la calle
  - tomo un vuelo

S -> NP VP
NP -> Det N | N
VP -> V NP | V NP PP | V PP
PP -> P NP
Det -> 'un'
N -> 'estudia' | 'musica' | 'profesor' | 'particular' | 'calle' | 'vuelo'
V -> 'caminaba' | 'tomo' | 'estudia'
P -> 'con' | 'por' | 'la'

S -> VP -> V NP PP -> 'estudia' NP PP -> 'estudia' N PP -> 'estudia música' PP -> 'estudia música' P NP -> 'estudia música con' NP -> 'estudia música con' N NP -> 'estudia música con profesor' N -> 'estudia música con profesor particular'


ii)
  - el auto azul
  - Rio de Janeiro
  - mañana sangrienta
  - un camion


S -> NA | NP
NA -> NP A
NP -> Det N | N
N -> 'Rio de Janeiro' | 'camion' | 'mañana'
A -> 'azul' | 'sangrienta'
Det -> 'el' | 'un'

S -> NA -> NP A -> Det N azul -> el auto azul
