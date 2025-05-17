GRAVEDAD = 9.81  # m/s²
MASA = 102 #sujeto + bici

def calcular_peso():
    """Devuelve el peso (en Newtons) del sistema sujeto+bici."""
    return MASA * GRAVEDAD

def fuerza_neta(aceleracion):
    """Calcula la fuerza neta aplicando segunda ley de Newton."""
    return MASA * aceleracion

def calcular_fuerza_x_promedio_por_tramo(times, ax, n_tramos=10):
    total = len(times)
    tramo_len = total // n_tramos
    resultados = []

    for i in range(n_tramos):
        inicio = i * tramo_len
        fin = (i + 1) * tramo_len if i < n_tramos - 1 else total

        t_inicio = times[inicio]
        t_fin = times[fin - 1]

        promedio_ax = sum(ax[inicio:fin]) / (fin - inicio)
        fx_promedio = MASA * promedio_ax

        resultados.append((
            i + 1,         # Número de tramo
            t_inicio,      # Tiempo inicial
            t_fin,         # Tiempo final
            promedio_ax,   # Aceleración promedio
            fx_promedio    # Fuerza promedio en X
        ))

    return resultados