import matplotlib.pyplot as plt


def graficador_continuo(
        var_indep, var_dep,
        titulo: str = "", etiqueta: str = "",
        etiqueta_x: str = "", etiqueta_y: str = ""):
    plt.plot(var_indep, var_dep, label=etiqueta)
    plt.title(titulo)
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()


def graficador_discreto(
        var_indep, var_dep,
        titulo: str = "", etiqueta: str = "",
        etiqueta_x: str = "", etiqueta_y: str = ""):
    plt.stem(var_indep, var_dep, label=etiqueta)
    plt.title(titulo)
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()
