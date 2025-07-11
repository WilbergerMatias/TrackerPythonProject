# import numpy as np
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
 
def generar_imagen_tramo(seleccion, t_inicial, t_final, delta_t, E_cinetica_inicial, E_cinetica_final, Trabajo_frenador, Pot):
        # === Generar imagen con cuadro ===
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.axis('off')  # sin ejes

    texto = (
        r"$\mathrm{Tramo\ seleccionado}$: " + f"{seleccion + 1}\n"
        r"$t_{i,\ frenado}$: " + f"{t_inicial:.2f}~s\n"
        r"$t_{f,\ frenado}$: " + f"{t_final:.2f}~s\n"
        r"$\Delta t_{frenado}$: " + f"{delta_t:.2f}~s\n"
        r"$E_{cin,\ i}$: " + f"{E_cinetica_inicial:.2f}~J\n"
        r"$E_{cin,\ f}$: " + f"{E_cinetica_final:.2f}~J\n"
        r"$W_{frenado}$: " + f"{Trabajo_frenador:.2f}~J\n"
        r"$P_{dis,\ frenado}$: " + f"{Pot:.2f}~W"
    )


    ax.text(0.5, 0.5, texto,
            fontsize=12, ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.5", edgecolor='black', facecolor='lightgrey'))
    plt.show()