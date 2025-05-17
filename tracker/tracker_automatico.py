import cv2

def trackear(video, bbox, escala, fps, step = 1):
    tracker = cv2.legacy.TrackerCSRT_create()
    tracker.init(video.read()[1], bbox)

    positions, times = [], []
    t = 0
    frame_index = 0
    print("Trackeando...")
    while True:
        ret, frame = video.read()
        if not ret:
            break

        if frame_index % step == 0:
            success, newbox = tracker.update(frame)
            if success:
                x, y, w, h = map(int, newbox)
                cx, cy = x + w / 2, y + h / 2
                positions.append((cx * escala, cy * escala))
                times.append(t)
        t += 1 / fps
        frame_index += 1

    return positions, times
    
