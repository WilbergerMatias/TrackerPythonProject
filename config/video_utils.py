import cv2
from tkinter import filedialog, Tk

def seleccionar_video():
    root = Tk()
    root.withdraw()
    ruta = filedialog.askopenfilename(title="Seleccionar video", filetypes=[("Archivos de video", "*.mp4 *.avi")])
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