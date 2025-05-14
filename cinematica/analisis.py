"""eliminar la velocidad y a aceleracion de la componente y"""
import numpy as np
from scipy.signal import savgol_filter
from scipy.ndimage import uniform_filter1d

def suavizar_datos(arr, metodo="combinado", reps=1):
    res = arr.copy()
    for i in range(reps):
        print("Suavizado filtro: "+str(i))
        if metodo == "media_movil":
            res = uniform_filter1d(arr, size=5, mode='nearest')
        elif metodo == "savgol":
            res = savgol_filter(arr, window_length=7, polyorder=2, mode='nearest')
        elif metodo == "combinado":
            intermedio = uniform_filter1d(arr, size=5, mode='nearest')
            res = savgol_filter(intermedio, window_length=7, polyorder=2, mode='nearest')
    return res    
            


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
    
    print("Calculando datos de velocidad")
    velocities = derivar(positions, times)

    print("suavizando picos extremos")
    velocities[:, 0] = suavizar_datos(velocities[:, 0],"combinado",reps = 1)
    # velocities[:, 1] = suavizar_datos(velocities[:, 1],reps = 2)
    
    # soft_v = suavizar_savgol(velocities, ventana=7, orden=3)
    print("Calculando datos aceleracion")
    accelerations = derivar(velocities, times)
    # accelerations = suavizar_savgol(accelerations, ventana=7, orden=3)
    print("suavizando curva de aceleracion")
    accelerations[:, 0] = suavizar_datos(accelerations[:, 0], reps = 4)
    # accelerations[:, 1] = suavizar_datos(accelerations[:, 1], reps = 4)
    
    return velocities, accelerations
