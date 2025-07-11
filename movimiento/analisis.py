# imports
from config.constantes import Masa
from movimiento.graficos import generar_imagen_tramo

# constantes
MASA = Masa()

def calcular_momento_lineal_x_promedio_por_tramo(times, velocidades, n_tramos=10):
    total = len(times)
    tramo_len = total // n_tramos
    resul = []

    for i in range(n_tramos):
        inicio = i * tramo_len
        fin = (i + 1) * tramo_len if i < n_tramos - 1 else total

        t_inicio = times[inicio]
        t_fin = times[fin - 1]

        velocidad_prom = sum(velocidades[inicio:fin]) / (fin - inicio)
        promedio_momento_lineal = MASA * velocidad_prom
        promedio_energia_cinetica=0.5*MASA*(velocidad_prom**2)

        resul.append((                # Corrección aquí
            i + 1,                    # Número de tramo
            t_inicio,                 # Tiempo inicial
            t_fin,                    # Tiempo final
            velocidad_prom,           # Velocidad promedio
            promedio_momento_lineal,  # Momento lineal promedio
            promedio_energia_cinetica # Energia cinetica promedio
        ))

    return resul

def calcular_trabajo_pot_frenado(Resultados, indice_tramo_frenador):

    # Selección: índice del tramo en la lista
    seleccion = indice_tramo_frenador - 1  # ajustar a base 0

    # Extraer la tupla de datos del tramo de inicio y convertir a lista
    Datos_int_inicio_frenado = list(Resultados[seleccion])
    Datos_int_final_frenado = list(Resultados[-1])

    # Tiempos
    t_inicial = Datos_int_inicio_frenado[1]
    t_final = Datos_int_final_frenado[2]
    delta_t = t_final - t_inicial

    # Energía cinética
    E_cinetica_inicial = Datos_int_inicio_frenado[5]
    E_cinetica_final = Datos_int_final_frenado[5]

    # Trabajo de frenador
    Trabajo_frenador = E_cinetica_final- E_cinetica_inicial

    # Potencia disipada
    if delta_t != 0:
        Pot = Trabajo_frenador / delta_t
    else:
        Pot = None
    generar_imagen_tramo(seleccion, t_inicial, t_final, delta_t, E_cinetica_inicial, E_cinetica_final, Trabajo_frenador, Pot)
    return Trabajo_frenador, Pot

def pedir_indice_tramo():
    """
    Pide al usuario el número de tramo de frenado.
    Sigue pidiendo hasta que se ingrese un número entero válido.
    Devuelve el entero.
    """
    while True:
        try:
            indice = int(input("Ingrese el número de tramo de frenado: "))
            return indice
        except ValueError:
            print("Debe ingresar un número entero. Intente de nuevo.")

