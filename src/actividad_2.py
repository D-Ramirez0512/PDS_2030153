import numpy as np
from src.utils.grapher import graficador_continuo


def entender_frecuencia(frecuencia_deseada):
    tiempo_inicial = 0
    tiempo_final = 5
    try:
        frecuencia = float(frecuencia_deseada)
    except ValueError:
        print("Frecuencia inválida. Debe ser un número.")
        return

    amplitud = 1
    puntos = 1000
    tiempo = np.linspace(tiempo_inicial, tiempo_final, puntos)
    señal = amplitud * np.sin(2 * np.pi * frecuencia * tiempo)

    graficador_continuo(
        tiempo, señal,
        titulo='Señal Senoidal Continua',
        etiqueta='Senoidal',
        etiqueta_x='Tiempo [s]', etiqueta_y='Amplitud'
    )
