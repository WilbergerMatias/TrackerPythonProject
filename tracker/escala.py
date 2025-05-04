import cv2
import numpy as np

def seleccionar_escala(frame):
    puntos = []

    def click(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            puntos.append((x, y))

    cv2.imshow("Seleccionar dos puntos para escala", frame)
    cv2.setMouseCallback("Seleccionar dos puntos para escala", click)
    while len(puntos) < 2:
        cv2.waitKey(1)
    cv2.destroyAllWindows()

    distancia_pixel = np.linalg.norm(np.array(puntos[0]) - np.array(puntos[1]))
    escala_real = float(input("Ingrese la distancia real entre los puntos seleccionados (en metros): "))
    escala = escala_real / distancia_pixel
    return escala
