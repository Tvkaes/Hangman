# Ahorcado - Consola
#### Practica en python 
En este código se simula el juego ahorcado , entrando en la primera fase donde se eligen las palabras de manera aleatoria dentro de un diccionario de palabras .


## Teoria

El ahorcado es un juego de adivinanzas de lápiz y papel para dos o más jugadores. Un jugador piensa en una palabra, frase u oración y el otro trata de adivinarla según lo que sugiere por letras o números.

## Expresiones
##### >> Se importa la funcion random y se importa de nuestro otro archivo llamado "words" la lista de palabras y con la funcion random se escoge una palabra dentro de la lista y se verifica que la palabra no tenga espacios o guiones 
```python
import random
from words import plbrs

def  validacion(plbrs):
  word = random.choice(plbrs)
  while  '-'  in word or  ' '  in word:
    word = random.choice(plbrs)
  return word
```
##### >> Guardamos nuestra validacion en una variable para almacenar las palabras verificadas y las que usaremos para jugar al ahorcado, dentro de un ciclo for imprimimos el numero de espacios disponibles para adivinar la palabra segun el numero de letras que contenga
```python

plbr_out = ""
    for letter in my_word:
        if letter in advn:
            plbr_out = plbr_out + letter + " "    
        else:
            plbr_out = plbr_out + "_ "

```
