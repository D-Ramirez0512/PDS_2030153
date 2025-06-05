import sys
from src.actividad_1 import seno_continuo, seno_discreto
from src.actividad_2 import entender_frecuencia


def main(opciones):
    if opciones[1] == "act_1":
        seno_continuo()
        seno_discreto()
    elif opciones[1] == "act_2":
        if len(opciones) > 2:
            entender_frecuencia(opciones[2])
        else:
            print("Por favor, proporciona una frecuencia. Ejemplo: python main.py act_2 2")


if __name__ == '__main__':
    argumentos = sys.argv
    if len(argumentos) > 1:
        main(argumentos)
    else:
        print("Por favor, proporciona un argumento.")
        print("Ejemplo (ejecutar actividad 1): python main.py act_1")
        print("Ejemplo (ejecutar actividad 2): python main.py act_2 1")
