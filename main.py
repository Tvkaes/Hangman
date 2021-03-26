
import random
import colorama
from words import plbrs, hngmn
from colorama import Fore, Style, init

# 1. Welcome
print("Bienvenido al juego del AHORCADO \n")
print("Tu palabra sera la siguiente\n")


def validacion(plbrs):
    word = random.choice(plbrs)
    while '-' in word or ' ' in word:
        word = random.choice(plbrs)
    return word

my_word = validacion(plbrs)
advn = []
errores = []

intnt = 6

while intnt > 0:
    plbr_out = ""
    for letter in my_word:
        if letter in advn:
            plbr_out = plbr_out + letter + " "
        else:
            init(autoreset=True)
            plbr_out = plbr_out + (Fore.CYAN + '_ ')


    if plbr_out == my_word:
         print("Ganaste Felicidades")
         break

    print("Adivina La Palabra\n" , plbr_out)
    print("Tienes 7 intentos, Te restan: ", intnt)
    letra = input()

    if letra in advn or letra in errores:
        print("Ya ingresaste la letra: ", letra)
    elif letra in my_word:
        print("Acertaste")
        advn.append(letra)
    else:
        print("No acertaste Intentalo otra vez")
        intnt = intnt - 1
        print(hngmn[intnt])
        errores.append(letra)

    if intnt == 0:
        print("Perdiste la palabra era: ", my_word)
