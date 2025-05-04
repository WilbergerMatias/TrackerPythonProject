import numpy as np
from scipy.signal import savgol_filter

def derivar(datos, tiempos):
    """Derivada numérica centrada."""
    datos = np.array(datos)
    tiempos = np.array(tiempos)
    derivada = np.zeros_like(datos)
    
    dt = np.diff(tiempos)
    # Derivada centrada para puntos intermedios
    derivada[1:-1] = (datos[2:] - datos[:-2]) / (tiempos[2:] - tiempos[:-2])[:, None]
    # Extremos con diferencia progresiva
    derivada[0] = (datos[1] - datos[0]) / dt[0]
    derivada[-1] = (datos[-1] - datos[-2]) / dt[-1]
    
    return derivada

def suavizar_savgol(datos, ventana=7, orden=3):
    """Aplica filtro Savitzky-Golay a datos 2D (x, y)."""
    datos = np.array(datos)
    if len(datos) < ventana:
        return datos  # Evita error si hay pocos datos
    suavizados = np.array([
        savgol_filter(datos[:, 0], ventana, orden),
        savgol_filter(datos[:, 1], ventana, orden)
    ]).T
    return suavizados

def analizar_movimiento(positions, times):
    """Calcula velocidad y aceleración suavizadas a partir de posiciones y tiempos."""
    positions = np.array(positions)
    times = np.array(times)
    
    velocities = derivar(positions, times)
    velocities = suavizar_savgol(velocities, ventana=7, orden=3)

    accelerations = derivar(velocities, times)
    accelerations = suavizar_savgol(accelerations, ventana=7, orden=3)
    
    return velocities, accelerations