import numpy as np
import matplotlib.pyplot as plt

def sin(t, f=2):
    return np.sin(2 * np.pi * f * t)

def expostep(t):
    return np.exp(-2 * t) * (t >= 0).astype(float)

def trian(t, f=2):
    T = 1 / f
    t_mod = np.mod(t, T)
    return 4 * np.abs(t_mod / T - 0.5) - 1

def cuad(t, f=2):
    T = 1 / f
    t_mod = np.mod(t, T)
    return np.where(t_mod < T/2, 1, -1)

def graphs(t_cont, x_cont, t_disc, x_disc, title):
    plt.figure(figsize=(10, 8))

    # Señal continua
    plt.subplot(3, 1, 1)
    plt.plot(t_cont, x_cont, 'b')
    plt.title(f'{title} - Señal Continua')
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True, linestyle='--', alpha=0.6)

    # Señal discreta
    plt.subplot(3, 1, 2)
    plt.stem(t_disc, x_disc, basefmt="r")
    plt.title(f'{title} - Señal Discreta')
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True, linestyle='--', alpha=0.6)

    # Ambas señales
    plt.subplot(3, 1, 3)
    plt.plot(t_cont, x_cont, 'b', label="Señal Continua")
    plt.stem(t_disc, x_disc, linefmt='g-', markerfmt='go', basefmt='r', label="Señal Discreta")
    plt.title(f'{title} - Ambas Señales')
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()

    plt.tight_layout()
    plt.show()

def graficar_senales():
    t_cont = np.linspace(-1, 5, 1000)
    Ts = 0.025
    t_disc = np.arange(-1, 5 + Ts, Ts)

    signals = {
        "Senoidal": sin,
        "Exponencial y Escalón": expostep,
        "Triangular": trian,
        "Cuadrada": cuad
    }

    for title, func in signals.items():
        x_cont = func(t_cont)
        x_disc = func(t_disc)
        graphs(t_cont, x_cont, t_disc, x_disc, title)

graficar_senales()

