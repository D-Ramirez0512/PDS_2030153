import numpy as np
from src.utils.grapher import graficador_continuo, graficador_discreto


def seno_continuo():
    frecuencia = 1
    amplitud = 1
    puntos = 1000
    tiempo_inicial = 0
    tiempo_final = 4
    tiempo = np.linspace(tiempo_inicial, tiempo_final, puntos)
    señal = amplitud * np.sin(2 * np.pi * frecuencia * tiempo)

    graficador_continuo(
        tiempo, señal,
        titulo='Señal Senoidal Continua',
        etiqueta='Senoidal',
        etiqueta_x='Tiempo [s]', etiqueta_y='Amplitud'
    )


def seno_discreto():
    frecuencia = 1
    amplitud = 1
    fs = 20
    ts = 1 / fs
    muestras = 100
    n = np.arange(muestras)
    señal = amplitud * np.sin(2 * np.pi * frecuencia * n * ts)

    graficador_discreto(
        n, señal,
        titulo='Señal Senoidal Discreta',
        etiqueta='Senoidal',
        etiqueta_x='Tiempo [n = índice de muestra]', etiqueta_y='Amplitud'
    )
