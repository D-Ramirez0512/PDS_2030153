import numpy as np
import matplotlib.pyplot as plt


def seno(tiempo, frecuencia=2):
    return np.sin(2 * np.pi * frecuencia * tiempo)


def exponencial_escalon(tiempo):
    return np.exp(-2 * tiempo) * (tiempo >= 0).astype(float)


def triangular(tiempo, frecuencia=2):
    periodo = 1 / frecuencia
    tiempo_mod = np.mod(tiempo, periodo)
    return 4 * np.abs(tiempo_mod / periodo - 0.5) - 1


def cuadrada(tiempo, frecuencia=2):
    periodo = 1 / frecuencia
    tiempo_mod = np.mod(tiempo, periodo)
    return np.where(tiempo_mod < periodo / 2, 1, -1)


def graficar_ambas_senales(t_continua, x_continua, t_discreta, x_discreta, titulo):
    plt.figure(figsize=(10, 8))

    # Señal continua
    plt.subplot(3, 1, 1)
    plt.plot(t_continua, x_continua, 'b')
    plt.title(f'{titulo} - Señal Continua')
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True, linestyle='--', alpha=0.6)

    # Señal discreta
    plt.subplot(3, 1, 2)
    plt.stem(t_discreta, x_discreta, basefmt="r")
    plt.title(f'{titulo} - Señal Discreta')
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True, linestyle='--', alpha=0.6)

    # Ambas señales
    plt.subplot(3, 1, 3)
    plt.plot(t_continua, x_continua, 'b', label="Señal Continua")
    plt.stem(t_discreta, x_discreta, linefmt='g-', markerfmt='go', basefmt='r', label="Señal Discreta")
    plt.title(f'{titulo} - Ambas Señales')
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()

    plt.tight_layout()
    plt.show()


def seno_continuo():
    # Esta función ahora se utiliza como punto de entrada para todas las señales continuas/discretas
    t_continua = np.linspace(-1, 5, 1000)
    ts = 0.025
    t_discreta = np.arange(-1, 5 + ts, ts)

    señales = {
        "Senoidal": seno,
        "Exponencial con Escalón": exponencial_escalon,
        "Triangular": triangular,
        "Cuadrada": cuadrada
    }

    for titulo, funcion in señales.items():
        x_cont = funcion(t_continua)
        x_disc = funcion(t_discreta)
        graficar_ambas_senales(t_continua, x_cont, t_discreta, x_disc, titulo)



