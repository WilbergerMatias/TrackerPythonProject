import cv2
import sys
import numpy as np

# --------------------------- Configuración Inicial ---------------------------- #

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
tracker_type = tracker_types[2]  # KCF por defecto

# --------------------------- Funciones Auxiliares ---------------------------- #

ref_points = []

def click_event(event, x, y, flags, param):
    global ref_points
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_points.append((x, y))
        cv2.circle(param, (x, y), 5, (0, 0, 255), -1)
        cv2.imshow("Seleccionar referencia", param)

def crear_tracker(tracker_type):
    if int(minor_ver) < 3:
        return cv2.Tracker_create(tracker_type)
    else:
        if tracker_type == 'BOOSTING':
            return cv2.TrackerBoosting_create()
        if tracker_type == 'MIL':
            return cv2.TrackerMIL_create()
        if tracker_type == 'KCF':
            return cv2.TrackerKCF_create()
        if tracker_type == 'TLD':
            return cv2.TrackerTLD_create()
        if tracker_type == 'MEDIANFLOW':
            return cv2.TrackerMedianFlow_create()
        if tracker_type == 'GOTURN':
            return cv2.TrackerGOTURN_create()
        if tracker_type == 'MOSSE':
            return cv2.TrackerMOSSE_create()
        if tracker_type == "CSRT":
            return cv2.TrackerCSRT_create()

# --------------------------- Código Principal ---------------------------- #

if __name__ == '__main__':

    # Abrir video
    # Pedir el video al usuario
    video_path = input("Ingrese la ruta o el nombre del video a analizar: ")
    video = cv2.VideoCapture(video_path)


    if not video.isOpened():
        print("No se pudo abrir el video")
        sys.exit()

    # Leer primer frame
    ok, frame = video.read()
    if not ok:
        print("No se pudo leer el video")
        sys.exit()

    # -------------------- Seleccionar referencia para la escala -------------------- #
    clone = frame.copy()
    print("Seleccioná dos puntos que representen una distancia conocida...")
    cv2.imshow("Seleccionar referencia", clone)
    cv2.setMouseCallback("Seleccionar referencia", click_event, clone)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if len(ref_points) != 2:
        print("Error: se necesitan exactamente dos puntos para calcular la escala.")
        sys.exit()

    (x1, y1), (x2, y2) = ref_points
    pixel_distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    real_distance_meters = float(input("¿Cuántos metros mide esa distancia? "))
    escala = real_distance_meters / pixel_distance  # metros por pixel
    print(f"Escala: {escala:.6f} metros por pixel")

    # -------------------- Seleccionar objeto a trackear -------------------- #
    bbox = cv2.selectROI("Seleccionar objeto", frame, False)
    cv2.destroyWindow("Seleccionar objeto")

    tracker = crear_tracker(tracker_type)
    ok = tracker.init(frame, bbox)

    # Variables para almacenar datos de movimiento
    positions = []
    times = []
    fps = video.get(cv2.CAP_PROP_FPS)

    positions = []
    times = []
    fps = video.get(cv2.CAP_PROP_FPS)

    object_points = []
    clicked = False
    frame_idx = 0

    def click_object(event, x, y, flags, param):
        global clicked
        if event == cv2.EVENT_LBUTTONDOWN:
            object_points.append((x, y))
            clicked = True

    while True:
        ok, frame = video.read()
        if not ok:
            break

        # Saltar frames que no sean múltiplos de 3
        if frame_idx % 3 != 0:
            frame_idx += 1
            continue

        clone = frame.copy()
        cv2.namedWindow("Haz clic en el objeto", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Haz clic en el objeto", 1280, 720)
        clicked = False
        cv2.setMouseCallback("Haz clic en el objeto", click_object)

        # Mostrar zoom del último punto (opcional)
        if object_points:
            zx, zy = object_points[-1]
            zoom = clone[max(zy-50, 0):zy+50, max(zx-50, 0):zx+50]
            if zoom.size > 0:
                zoom = cv2.resize(zoom, (200, 200))
                cv2.imshow("Zoom", zoom)

        while not clicked:
            cv2.imshow("Haz clic en el objeto", clone)
            key = cv2.waitKey(10) & 0xFF
            if key == 27:  # ESC para salir
                video.release()
                cv2.destroyAllWindows()
                exit()

        x, y = object_points[-1]
        cv2.circle(clone, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow("Haz clic en el objeto", clone)
        cv2.waitKey(300)

        # Convertir a metros
        center_x_m = x * escala
        center_y_m = y * escala

        positions.append((center_x_m, center_y_m))
        current_time = frame_idx / fps
        times.append(current_time)

        frame_idx += 1

    video.release()
    cv2.destroyAllWindows()
    """ # -------------------- Loop principal -------------------- #

    while True:
        ok, frame = video.read()
        if not ok:
            break

        timer = cv2.getTickCount()

        ok, bbox = tracker.update(frame)

        fps_calc = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

        if ok:
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)

            # Centro del objeto
            center_x = bbox[0] + bbox[2] / 2
            center_y = bbox[1] + bbox[3] / 2

            # Convertir a metros
            center_x_m = center_x * escala
            center_y_m = center_y * escala

            positions.append((center_x_m, center_y_m))
            current_time = len(positions) / fps
            times.append(current_time)

        else:
            cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

        # Mostrar info
        cv2.putText(frame, tracker_type + " Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)
        cv2.putText(frame, f"FPS : {int(fps_calc)}", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

        cv2.imshow("Tracking", frame)

        k = cv2.waitKey(1) & 0xff
        if k == 27:  # ESC para salir
            break

    video.release()
    cv2.destroyAllWindows()
    """
    # -------------------- Cálculos de velocidad y aceleración -------------------- #

    positions = np.array(positions)
    times = np.array(times)

    velocities = np.gradient(positions, times, axis=0)
    accelerations = np.gradient(velocities, times, axis=0)

    # Imprimir resultados (puede mejorarse para graficar)
    for i in range(len(times)):
        print(f"t = {times[i]:.2f} s | x = {positions[i,0]:.2f} m | y = {positions[i,1]:.2f} m | "
              f"Vx = {velocities[i,0]:.2f} m/s | Vy = {velocities[i,1]:.2f} m/s | "
              f"Ax = {accelerations[i,0]:.2f} m/s² | Ay = {accelerations[i,1]:.2f} m/s²")

    # Opcional: guardar a archivo CSV
    np.savetxt("datos_movimiento.csv", np.column_stack((times, positions, velocities, accelerations)),
               delimiter=",", header="time,x,y,vx,vy,ax,ay", comments='')


import matplotlib.pyplot as plt

# ----------------- Gráficas ----------------- #

# Posición
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(times, positions[:, 0], label='Posición X (m)')
plt.plot(times, positions[:, 1], label='Posición Y (m)')
plt.title('Movimiento')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.legend()
plt.grid(True)

# Velocidad
plt.subplot(3, 1, 2)
plt.plot(times, velocities[:, 0], label='Velocidad X (m/s)')
plt.plot(times, velocities[:, 1], label='Velocidad Y (m/s)')
plt.title('Velocidad')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.legend()
plt.grid(True)

# Aceleración
plt.subplot(3, 1, 3)
plt.plot(times, accelerations[:, 0], label='Aceleración X (m/s²)')
plt.plot(times, accelerations[:, 1], label='Aceleración Y (m/s²)')
plt.title('Aceleración')
plt.xlabel('Tiempo (s)')
plt.ylabel('Aceleración (m/s²)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()


