import pandas as pd
import os
import tkinter as tk
from tkinter import ttk

def generar_cuadro_resultados(resultados, nombre_archivo="resultados_tramos_momento_lin_y_energia.xlsx", carpeta = "resultados"):
    """
    Convierte los resultados de los tramos en un DataFrame de pandas,
    redondea los valores a 4 decimales y los exporta a un archivo Excel.

    Parámetros:
    - resultados: Lista de tuplas con datos de los tramos.
    - nombre_archivo: Nombre del archivo Excel a generar (por defecto "resultados_tramos_momento_lin_y_energia.xlsx")

    Retorna:
    - El DataFrame generado.
    """
    # Crear el DataFrame
    df = pd.DataFrame(resultados, columns=[
        "Tramo",
        "Tiempo Inicial (s)",
        "Tiempo Final (s)",
        "Velocidad Promedio (m/s)",
        "Momento Lineal Promedio (kg·m/s)",
        "Energía Cinética Promedio (J)"
    ])

    # Redondear a 4 decimales
    df = df.round(4)

    full_path = os.path.join(carpeta, nombre_archivo)

    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    # Exportar a archivo Excel
    df.to_excel(full_path, index=False)

    print(f"✅ Archivo Excel guardado como: {nombre_archivo}")
    return df

def mostrar_tabla_momento_energia_por_tramo(tramos):
    ventana = tk.Tk()
    ventana.title("Momento lineal y Energía cinética promedio por tramo")

    columnas = ("Tramo", "Tiempo inicial (s)", "Tiempo final (s)",
                "Velocidad promedio (m/s)", "Momento lineal (kg·m/s)", "Energía cinética (J)")

    tabla = ttk.Treeview(ventana, columns=columnas, show="headings")

    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, anchor="center", width=150)

    for tramo in tramos:
        tabla.insert("", "end", values=(
            round(tramo[0], 4),         # número de tramo
            round(tramo[1], 4),         # Tiempo inicial
            round(tramo[2], 4),         # Tiempo final
            round(float(tramo[3]), 4),  # Velocidad promedio
            round(float(tramo[4]), 4),  # Momento lineal promedio
            round(float(tramo[5]), 4),  # Energia cinetica promedio
        ))

    tabla.pack(expand=True, fill="both", padx=10, pady=10)

    btn_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
    btn_cerrar.pack(pady=10)

    ventana.mainloop()
