import tkinter as tk
from tkinter import ttk

def mostrar_tabla_fuerza_x_por_tramo(tramos):
    ventana = tk.Tk()
    ventana.title("Fuerza en X promedio por tramo")

    columnas = (
    "Segmento",
    "Tiempo inicial (s)",
    "Tiempo final (s)",
    "Aceleración promedio en X (m/s²)",
    "Fuerza promedio en X (N)"
)
    tabla = ttk.Treeview(ventana, columns=columnas, show="headings")

    for col in columnas:
        tabla.heading(col, text=col)

    for fila in tramos:
        fila_formateada = [f"{v:.2f}" if isinstance(v, float) else v for v in fila]
        tabla.insert("", "end", values=fila_formateada)

    tabla.pack(expand=True, fill="both", padx=20, pady=20)
    ttk.Button(ventana, text="Cerrar", command=lambda: (ventana.destroy(), ventana.quit())).pack(pady=10)
    ventana.protocol("WM_DELETE_WINDOW", lambda: (ventana.destroy(), ventana.quit()))
    ventana.mainloop()