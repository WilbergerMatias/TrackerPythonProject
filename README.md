# Tracker de Movimiento en Video

Este proyecto permite analizar el movimiento de un objeto en un video para calcular posición, velocidad, aceleración y fuerzas (promedios).

## ¿Cómo se usa?

1. Ejecutá `main.py`.
2. Elegí un video MP4 (se recomienda que tenga 30 FPS o menos).
3. Hacé clic en dos puntos conocidos del video para definir una referencia de escala.
4. Ingresá por consola la distancia real entre esos puntos (en metros).
5. Seleccioná el objeto a trackear con clic y arrastre, y presioná Enter cuando estés conforme.
6. El sistema hará el seguimiento y mostrará:
   - Un replay del video con una flecha de velocidad.
   - Gráficos de posición, velocidad y aceleración.
   - Una tabla con fuerzas promedio en 10 segmentos.

## Requisitos

- Python 3
- Librerías:
  - `opencv-python`
  - `numpy`
  - `matplotlib`
  - `tkinter` (incluida por defecto)

Instalación rápida:

```bash
pip install opencv-contrib-python numpy matplotlib
