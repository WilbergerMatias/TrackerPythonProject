import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def graficar_resultados(times, positions, velocities, accelerations):
    def is_2d(arr):
        return isinstance(arr[0], (list, tuple, np.ndarray))

    pos = list(zip(*positions)) if len(positions) > 0 and is_2d(positions) else [positions]
    vel = list(zip(*velocities)) if len(velocities) > 0 and is_2d(velocities) else [velocities]
    acc = list(zip(*accelerations)) if len(accelerations) > 0 and is_2d(accelerations) else [accelerations]

    fig = make_subplots(rows=3, cols=1, shared_xaxes=True,
                        subplot_titles=("Movimiento (X)", "Velocidad (X)", "Aceleración (X)"))

    # Solo eje X
    fig.add_trace(go.Scatter(x=times, y=pos[0], mode='lines', name='Posición X (m)'), row=1, col=1)
    fig.add_trace(go.Scatter(x=times, y=vel[0], mode='lines', name='Velocidad X (m/s)'), row=2, col=1)
    fig.add_trace(go.Scatter(x=times, y=acc[0], mode='lines', name='Aceleración X (m/s²)'), row=3, col=1)

    fig.update_layout(
        height=800,
        width=900,
        title_text="Análisis del Movimiento - Eje X",
        showlegend=True
    )

    fig.update_xaxes(title_text="Tiempo (s)", row=3, col=1)
    fig.update_yaxes(title_text="Posición X (m)", row=1, col=1)
    fig.update_yaxes(title_text="Velocidad X (m/s)", row=2, col=1)
    fig.update_yaxes(title_text="Aceleración X (m/s²)", row=3, col=1)

    fig.show()
