from config.video_utils import abrir_video, seleccionar_objeto, seleccionar_video
from tracker.escala import seleccionar_escala
from tracker.tracker_automatico import trackear
from cinematica.analisis import analizar_movimiento
from cinematica.visualizar import dibujar_velocidad
from graficos.utils import guardar_csv, guardarTXT
from graficos.graficos import graficar_resultados


def main():
    ruta = seleccionar_video()
    frame, video, fps = abrir_video(ruta)
    escala = seleccionar_escala(frame)
    bbox = seleccionar_objeto(frame)
    
    positions, times = trackear(video, bbox, escala, fps, 3)
    velocities, accelerations = analizar_movimiento(positions, times)
    dibujar_velocidad(ruta, positions, times, escala)
    guardar_csv(times, positions, velocities, accelerations, "resultado.csv")
    guardarTXT(times, positions, velocities, accelerations, "resultados/datos_ultimo_movimiento.txt")
    graficar_resultados(times, positions, velocities, accelerations)
    

if __name__ == "__main__":
    main()
