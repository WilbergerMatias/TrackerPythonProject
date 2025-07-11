# imports
import cv2
import os
from tkinter import filedialog, Tk

#constantes
NOMBRE_VIDEO = None

def seleccionar_video():
    root = Tk()
    root.withdraw()
    ruta = filedialog.askopenfilename(title="Seleccionar video", filetypes=[("Archivos de video", "*.mp4 *.avi")])
    if ruta:
        base_name = os.path.splitext(os.path.basename(ruta))[0]  # e.g. 'video_01'
        set_nombre_video(base_name)

    return ruta

def abrir_video(ruta):
    cap = cv2.VideoCapture(ruta)
    fps = cap.get(cv2.CAP_PROP_FPS)
    ret, frame = cap.read()
    return frame, cap, fps

def seleccionar_objeto(frame):
    bbox = cv2.selectROI("Seleccionar objeto", frame, fromCenter=False, showCrosshair=True)
    cv2.destroyWindow("Seleccionar objeto")
    return bbox

def set_nombre_video(nombre):
    global NOMBRE_VIDEO
    NOMBRE_VIDEO = nombre
    
def get_nombre_video():
    return NOMBRE_VIDEO