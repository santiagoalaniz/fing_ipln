# Ejercicio 2

En general tienden a ser lo mismo (palabra y token). La diferencia pasa porque en algunos casos, 2 o más palabras pueden ser consideradas como un token, como es el caso por ejemplo de Buenos Aires, Las Piedras, etc. Esto puede ser útil en aquellos casos en que estemos queriendo reconocer por ejemplo lo que se conoce como Entidades con Nombre como lo comentamos en clase. En esos 2 ejemplos son 2 palabras y 1 token.

Por otro lado y siguiendo con el ejemplo de hoy, si aparece Buenos Aires y buenos amigos, la palabra buenos aparece 2 veces (ahí en principio no distinguimos mayúscula y minúscula), sin embargo se cuenta como 1 solo tipo, ya que es la misma secuencia de símbolos (la palabra aparece repetida). Por otro lado, Buenos Aires es un solo token como ya vimos mientras que buenos amigos serían 2 tokens.

También pueden estar los casos de secuencias de palabras que pueden juntas tener un significado propio, como es el ejemplo de “estado del arte” donde queremos tomarlas como un solo token, sin embargo son 3 palabras. Ya el ejemplo de “mesa de casino” es como más raro que lo quieran identificar como un token, pero podría ser… es mas discutible. Pero de eso se trataba este ejercicio, más que tener una solución única, discutir y analizar los problemas.
Sin dudas es uno de los aspectos que los tokenizadores debieran considerar al hacer su trabajo.


## Parte I

"Rocha ni siquiera tiene un hotel cuatro estrellas, ni una rambla, ni un shopping, ni un cine, ni una mesa de casino, ni una piscina termal marina."

Palabras: 18
Tokens: 28, 22(NI SIQUIERA, NI UNA, NI UN, NI UN, NI UNA, NI UNA)
Word-Types: 18

## Parte II
"Con el incendio grande del año pasado salieron de los montes de Punta Rubia cientos de personas."

Palabras: 15
Tokens: 17, 16 (PUNTA RUBIA)
Word-Types: 15

## Parte III

El estado del arte es una modalidad de la investigación documental que permite el estudio del conocimiento acumulado (escrito en textos) dentro de un área específica.

Palabras: 25
Tokens: 27, 25(ESTADO DEL ARTE)
Word-Types: 25
