import csv
import os

def guardar_csv(times, positions, velocities, accelerations, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Tiempo", "PosX", "PosY", "VelX", "VelY", "AcelX", "AcelY"])
        for i in range(len(times)):
            row = [times[i], *positions[i], *velocities[i], *accelerations[i]]
            writer.writerow(row)

def guardarTXT(times, positions, velocities, accelerations, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as file:
        for i in range(len(times)):
            file.write(f"t={times[i]:.2f}s -> Pos=({positions[i][0]:.2f},{positions[i][1]:.2f}) m, ")
            file.write(f"Vel=({velocities[i][0]:.2f},{velocities[i][1]:.2f}) m/s, ")
            file.write(f"Acel=({accelerations[i][0]:.2f},{accelerations[i][1]:.2f}) m/s^2\n")