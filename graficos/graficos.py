import plotly.graph_objects as go
from plotly.subplots import make_subplots

def graficar_resultados(times, positions, velocities, accelerations):
    pos = list(zip(positions))
    vel = list(zip(velocities))
    acc = list(zip(*accelerations))

    fig = make_subplots(rows=3, cols=1, shared_xaxes=True,
                        subplot_titles=("Movimiento", "Velocidad", "Aceleración"))

    # Posición
    fig.add_trace(go.Scatter(x=times, y=pos[0], mode='lines', name='Posición X (m)'), row=1, col=1)
    fig.add_trace(go.Scatter(x=times, y=pos[1], mode='lines', name='Posición Y (m)'), row=1, col=1)

    # Velocidad
    fig.add_trace(go.Scatter(x=times, y=vel[0], mode='lines', name='Velocidad X (m/s)'), row=2, col=1)
    # fig.add_trace(go.Scatter(x=times, y=vel[1], mode='lines', name='Velocidad Y (m/s)'), row=2, col=1)

    # Aceleración
    fig.add_trace(go.Scatter(x=times, y=acc[0], mode='lines', name='Aceleración X (m/s²)'), row=3, col=1)
    # fig.add_trace(go.Scatter(x=times, y=acc[1], mode='lines', name='Aceleración Y (m/s²)'), row=3, col=1)

    fig.update_layout(
        height=800,
        width=900,
        title_text="Análisis del Movimiento",
        showlegend=True
    )

    fig.update_xaxes(title_text="Tiempo (s)", row=3, col=1)
    fig.update_yaxes(title_text="Posición (m)", row=1, col=1)
    fig.update_yaxes(title_text="Velocidad (m/s)", row=2, col=1)
    fig.update_yaxes(title_text="Aceleración (m/s²)", row=3, col=1)

    fig.show()