from curses import tparm
from operator import truediv
import random

from art import *

tprint("RANDOM MATH QUIZ")

def nivelGod():
    contadorLVLGod = 0
    while contadorLVLGod < 5:
        numeroUnoLVLGod = random.randint(500,1000)
        numeroDosLVLGod = random.randint(500,1000)
        sumaLVLGod = int(input(f"{numeroUnoLVLGod} + {numeroDosLVLGod}?\n------\n"))
        if (sumaLVLGod) == (numeroDosLVLGod + numeroUnoLVLGod):
            contadorLVLGod += 1
        elif (sumaLVLGod) != (numeroDosLVLGod + numeroUnoLVLGod):
            contadorLVLGod -= 1
        print("Tu puntaje: ", contadorLVLGod)
    if contadorLVLGod == 5:
        tprint("YOU WIN!")


def nivelDos():
    contadorLVL2 = 0
    while contadorLVL2 < 5:
        numeroUnoLVL2 = random.randint(100,500)
        numeroDosLVL2 = random.randint(100,500)
        sumaLVL2 = int(input(f"{numeroUnoLVL2} + {numeroDosLVL2}?\n------\n"))
        if (sumaLVL2) == (numeroDosLVL2 + numeroUnoLVL2):
            contadorLVL2 += 1
        elif (sumaLVL2) != (numeroDosLVL2 + numeroUnoLVL2):
            contadorLVL2 -= 1
        print("Tu puntaje: ", contadorLVL2)
    if contadorLVL2 == 5:
        nivelGod()



def nivelUno():
    contadorLVL1 = 0
    while contadorLVL1 < 5:
        numeroUnoLVL1 = random.randint(1,50)
        numeroDosLVL1 = random.randint(1,50)
        sumaLVL1 = int(input(f"{numeroUnoLVL1} + {numeroDosLVL1}?\n------\n"))
        if (sumaLVL1) == (numeroDosLVL1 + numeroUnoLVL1):
            contadorLVL1 += 1
        elif (sumaLVL1) != (numeroDosLVL1 + numeroUnoLVL1):
            contadorLVL1 -= 1
        print("Tu puntaje: ", contadorLVL1)
    if contadorLVL1 == 5:
        nivelDos()

nivelUno()

