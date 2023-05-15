# **Ejercicio 6**

Considera el problema de identificar el alcance de una especulación en un texto. Para abordar este problema, lo modelamos como un caso de clasificación secuencial utilizando el esquema FOL (First-Last-Other).

Tomemos, por ejemplo, la siguiente oración: "Los resultados indican que existe una relación entre A y B". En esta oración, "indican" es una marca de especulación.

Bajo el esquema FOL, cada token de la oración se anota con una clase. La clase "F" se asigna si el token es el comienzo del alcance de la especulación. La clase "L" se asigna si el token es el final del alcance de la especulación. Todos los demás tokens se anotan con la clase "O".

## **Parte a)**
`Muestre las clase asociada a cada token de la oración:`

```
Los: O
resultados: O
indican: F
que: O
existe: O
una: O
relación: O
entre: O
A: O
y: O
B: L
```

## **Parte b)**
`¿Como es la relacion entre Accuracy, Precision y Recall para este Problema?`

- **Accuracy** mide la proporción de predicciones correctas entre todas las predicciones realizadas. En este problema, sería la proporción de tokens que se clasificaron correctamente como F, O o L.

- **Precision** mide la proporción de predicciones positivas que son verdaderamente positivas. En este caso, si consideramos, por ejemplo, "F" como la clase positiva, la precisión sería la proporción de tokens clasificados como "F" que verdaderamente deberían ser "F".

- **Recall** mide la proporción de casos verdaderamente positivos que fueron identificados correctamente. En el mismo ejemplo, sería la proporción de todos los tokens que deberían ser "F" que fueron correctamente identificados como "F".