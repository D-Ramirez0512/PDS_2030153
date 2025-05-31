# Visualización de Señales Continuas y Discretas

Este proyecto de Python permite visualizar y comparar versiones continuas y discretas de distintas señales básicas: senoidal, exponencial-escalón, triangular y cuadrada. Es ideal para quienes estudian o trabajan en procesamiento de señales, electrónica, comunicaciones o teoría de control.

## 📌 Características

- Genera y grafica señales **senoidales**, **exponenciales con escalón**, **triangulares** y **cuadradas**.
- Muestra cada señal en:
  - Versión continua
  - Versión discreta (muestreo)
  - Ambas superpuestas para comparación visual

## 🖼️ Ejemplo de salida

El programa genera gráficas como esta para cada señal:

```
Senoidal - Señal Continua  
Senoidal - Señal Discreta  
Senoidal - Ambas Señales  
```

*(Cada señal se grafica en una figura con tres subgráficas)*

## ⚙️ Requisitos

- Python 3.x
- `numpy`
- `matplotlib`

Puedes instalarlos con:

```bash
pip install numpy matplotlib
```

## ▶️ Cómo ejecutar

1. Clona este repositorio o copia el script `graficar_senales.py`.
2. Ejecuta el archivo en tu entorno de desarrollo o con Python desde consola:

```bash
python graficar_senales.py
```

Se abrirán ventanas con las gráficas para cada tipo de señal.

## 📁 Estructura del código

- `sin(t, f=2)`: Señal senoidal de frecuencia `f`
- `expostep(t)`: Señal exponencial multiplicada por un escalón unitario
- `trian(t, f=2)`: Señal triangular periódica
- `cuad(t, f=2)`: Señal cuadrada periódica
- `graphs(...)`: Función que genera las 3 gráficas por señal
- `graficar_senales()`: Función principal que organiza la visualización
