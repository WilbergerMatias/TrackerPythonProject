import cv2, os

def dibujar_velocidad(
    ruta_video, positions_m, escala,
    output_path=None, arrow_color=(0,255,0), arrow_thickness=2, tip_length=0.3,
    step=3  # ahora configurable
):
    cap = cv2.VideoCapture(ruta_video)
    fps = cap.get(cv2.CAP_PROP_FPS)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    writer = None
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        writer = cv2.VideoWriter(output_path, fourcc, fps, (w, h))

    pts = [ (int(x_m/escala), int(y_m/escala)) for x_m,y_m in positions_m ]

    idx = 1
    frame_idx = 0
    while True:
        ret, frame = cap.read()
        if not ret or idx >= len(pts):
            break

        # Mostrar solo los frames que corresponden al step usado en el tracking
        if frame_idx % step == 0:
            p0, p1 = pts[idx - 1], pts[idx]
            cv2.arrowedLine(frame, p0, p1, arrow_color, arrow_thickness, tipLength=tip_length)
            idx += 1

        cv2.imshow("Tracking con flechas", frame)
        if writer:
            writer.write(frame)

        if cv2.waitKey(int(1000/fps)) & 0xFF == 27:
            break

        frame_idx += 1

    cap.release()
    if writer:
        writer.release()
    cv2.destroyAllWindows()