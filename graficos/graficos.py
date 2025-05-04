import matplotlib.pyplot as plt

def graficar_resultados(times, positions, velocities, accelerations):
    times = times
    pos = list(zip(*positions))
    vel = list(zip(*velocities))
    acc = list(zip(*accelerations))

    fig, axs = plt.subplots(3, 1, figsize=(10, 8))

    axs[0].plot(times, pos[0], label="Posición X (m)")
    axs[0].plot(times, pos[1], label="Posición Y (m)")
    axs[0].set_title("Movimiento")
    axs[0].set_ylabel("Posición (m)")
    axs[0].legend()

    axs[1].plot(times, vel[0], label="Velocidad X (m/s)")
    axs[1].plot(times, vel[1], label="Velocidad Y (m/s)")
    axs[1].set_title("Velocidad")
    axs[1].set_ylabel("Velocidad (m/s)")
    axs[1].legend()

    axs[2].plot(times, acc[0], label="Aceleración X (m/s²)")
    axs[2].plot(times, acc[1], label="Aceleración Y (m/s²)")
    axs[2].set_title("Aceleración")
    axs[2].set_ylabel("Aceleración (m/s²)")
    axs[2].legend()

    for ax in axs:
        ax.set_xlabel("Tiempo (s)")
        ax.grid(True)

    plt.tight_layout()
    plt.show()