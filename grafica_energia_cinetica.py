import numpy as np
import matplotlib.pyplot as plt

def graf_energia_cinetica(resul):
    # Crear los arrays desde la lista de tuplas
    intervalo = [tupla[0] for tupla in resul]
    T_prom = [tupla[5] for tupla in resul]

    # Graficar
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(intervalo, T_prom, marker='o')
    ax.set_title("Energía Cinética Promedio por Tramo")
    ax.set_xlabel("Tramo")
    ax.set_ylabel("Energía Cinética Promedio (J)")
    plt.savefig('Energia_cinetica.png', dpi=100)
    plt.show()
 
