# Ejercicio 3

S -> GN GV [1.0]
GN -> Det N [0.3] | N Adv [0.1] | GP GN [0.2] | NProp [0.2] | N [0.2]
GV -> V GN [0.5] | V [0.2] | GV GP [0.3]
GP -> P GN [0.8] | P [0.2]
Det -> 'el' [0.5] | 'los' [0.5]
N -> 'hombre' [0.2] | 'amigos' [0.2] | 'café' [0.2] | 'leche' [0.2] | 'música' [0.2]
NProp -> 'Ana' [0.5] | 'Juan' [0.5]
V -> 'toma' [0.5] | 'escucha' [0.5]
P -> 'con' [0.5] | 'de' [0.5]
Adv -> 'solo' [1.0]

## Juan escucha musica solo

(S (GN (NProp Juan)) (GV (V escucha)(GN (N música)(Adv solo))))
= 1.0 * 0.5 * 0.5 * 0.2 * 1.0 * 0.1 * 0.5 = 0.005

## El hombre toma café con los amigos

(S (GN (Det el) (N hombre)) (GV (V toma) (GN (N café)) (GP (P con) (GN (Det los)(N amigos)))))
= 1.0 * 0.5 * 0.2 * 0.5 * 0.2 * 0.5 * 0.5 * 0.2 * 0.3 * 0.3 * 0.3 * 0.8 = 0.000054
