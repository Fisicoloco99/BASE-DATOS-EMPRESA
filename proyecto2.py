# tabla empleados, nombre, apellido , ID, asistencias , alos trabajados, DNI,todo lo que hace un CRUD , asistencias justificada o no, bonificaciones o no
# ver,agregar, funcion que hace de las asistencias, faltas justificadas o no,actualizar, eliminar
#Registro de empresa:Tabla empleados: id, nombre y apellido, anios trabajados, asistencias, dni. CRUD. Asistencias, justificada o no.  bonificaciones o no
import os
import sqlite3
import tkinter as tk
from tkinter import Label, Button, Entry, Listbox, Frame
from PIL import Image, ImageTk 

# Ruta segura para encontrar la imagen sin importar desde dónde ejecutes el script
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
RUTA_IMAGEN = os.path.join(DIRECTORIO_ACTUAL, "empresa.png")

conexion_empleados = sqlite3.connect("Empleados.db")
cursor_empleados = conexion_empleados.cursor()
cursor_empleados.execute("""
    CREATE TABLE IF NOT EXISTS empleados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_apellido TEXT NOT NULL,
        anio_inicio TEXT NOT NULL,
        asistencias INTEGER,
        dni INTEGER
    )
""")
conexion_empleados.commit()

def comprobar(empleado, entry_, orden):
    variable = entry_.get()
    if variable == "":
        return empleado[orden]
    else:
        return variable

def new_empleado():
    nom_ape = entry_nom_ape.get()
    anio = entry_anio.get()
    asist = entry_asistencias.get()
    dni = entry_dni.get()
    cursor_empleados.execute("INSERT INTO empleados (nombre_apellido, anio_inicio, asistencias, dni) VALUES (?,?,?,?)", (nom_ape, anio, asist, dni))
    conexion_empleados.commit()
    ver()
    limpiar_entry()
    
def editar_empleado():
    p_id = entry_id.get()
    cursor_empleados.execute("SELECT * FROM empleados")
    empleados = cursor_empleados.fetchall()
    for empleado in empleados:
        if int(p_id) == empleado[0]:
            nom_ape = comprobar(empleado, entry_nom_ape, 1)
            anio = comprobar(empleado, entry_anio, 2)
            asist = comprobar(empleado, entry_asistencias, 3)
            dni = comprobar(empleado, entry_dni, 4)
            cursor_empleados.execute("UPDATE empleados SET nombre_apellido = ?, anio_inicio = ?, asistencias = ?, dni = ? WHERE id = ?", (nom_ape, anio, asist, dni, p_id))
            conexion_empleados.commit()
            ver()
            limpiar_entry()

def eliminar_empleado():
    p_id = entry_id.get()
    cursor_empleados.execute("DELETE FROM empleados WHERE id = ?", (p_id,))
    conexion_empleados.commit()
    ver()
    limpiar_entry()

def ver():
    lista.delete(0, tk.END)
    cursor_empleados.execute("SELECT * FROM empleados")
    for i in cursor_empleados.fetchall():
        lista.insert(tk.END, i)
        
def limpiar_entry():
    entry_id.delete(0, tk.END)
    entry_nom_ape.delete(0, tk.END)
    entry_anio.delete(0, tk.END)
    entry_asistencias.delete(0, tk.END)
    entry_dni.delete(0, tk.END)

COLOR_FONDO = "#FBFBFB"
COLOR_FONDO_II = "#bee8e2"

# VENTANA
ventana = tk.Tk()
ventana.title("Empresa")
ventana.geometry("880x800")
ventana.resizable(False, False)

# Creamos el lienzo para poder poner la imagen de fonde
canvas_fondo = tk.Canvas(ventana, width=880, height=800, highlightthickness=0)
canvas_fondo.place(x=0, y=0, relwidth=1, relheight=1)

img_original = Image.open(RUTA_IMAGEN)
img_redimensionada = img_original.resize((880, 800))
fondo = ImageTk.PhotoImage(img_redimensionada)

# La dibujamos en el lienzo
canvas_fondo.create_image(0, 0, image=fondo, anchor="nw")
canvas_fondo.image = fondo


# ==========================================
# TUS WIDGETS
# ==========================================
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(6, weight=1)

# ETIQUETAS FILA 0
label_id = Label(ventana, text="ID", bg=COLOR_FONDO)
label_id.grid(row=0, column=1, padx=10, pady=5)
label_nom_ape = Label(ventana, text="Apellido nombre", bg=COLOR_FONDO)
label_nom_ape.grid(row=0, column=2, padx=10, pady=5)
label_anios = tk.Label(ventana, text="Anios trabajados", bg=COLOR_FONDO)
label_anios.grid(row=0, column=3, padx=10, pady=5)
label_asistencias = Label(ventana, text="Asistencias", bg=COLOR_FONDO)
label_asistencias.grid(row=0, column=4, padx=10, pady=5)
label_dni = Label(ventana, text="DNI", bg=COLOR_FONDO)
label_dni.grid(row=0, column=5, padx=10, pady=5)

# ENTRADAS FILA 1
entry_id = Entry(ventana, bg=COLOR_FONDO_II)
entry_id.grid(row=1, column=1, padx=10)
entry_nom_ape = Entry(ventana, bg=COLOR_FONDO_II)
entry_nom_ape.grid(row=1, column=2, padx=10)
entry_anio = tk.Entry(ventana, bg=COLOR_FONDO_II)
entry_anio.grid(row=1, column=3, padx=10)
entry_asistencias = Entry(ventana, bg=COLOR_FONDO_II)
entry_asistencias.grid(row=1, column=4, padx=10)
entry_dni = Entry(ventana, bg=COLOR_FONDO_II)
entry_dni.grid(row=1, column=5, padx=10)

# LISTBOX FILA 2
lista = Listbox(ventana, width=80, height=15)
lista.grid(row=2, column=1, columnspan=5, pady=20)
ver()

label_asistencias_justificadas = Label(ventana, text="Asistencias justificadas o no", bg=COLOR_FONDO)
label_asistencias_justificadas.grid(row=4, column=2, padx=10)
label_bonificaciones = Label(ventana, text="Bonificaciones o no", bg=COLOR_FONDO)
label_bonificaciones.grid(row=4, column=4, padx=10)

# FRAME INFERIOR (Botones)
frame_botones = Frame(ventana, bg=COLOR_FONDO) 
frame_botones.grid(row=5, column=1, columnspan=5, pady=20)

boton_agregar = Button(frame_botones, text="AGREGAR EXPEDIENTE", command=new_empleado, font=("Arial", 12), bg="green", fg="white")
boton_agregar.grid(row=0, column=1, padx=20)

boton_editar = Button(frame_botones, text="EDITAR EMPLEADO", command=editar_empleado, font=("Arial", 12), bg="blue", fg="white")
boton_editar.grid(row=0, column=2, padx=20)

boton_eliminar = Button(frame_botones, text="ELIMINAR ARCHIVOS", command=eliminar_empleado, font=("Arial", 12), bg="red", fg="white")
boton_eliminar.grid(row=0, column=3, padx=20)

frame_botones.grid_columnconfigure(0, weight=1) 
frame_botones.grid_columnconfigure(4, weight=1) 

ventana.mainloop()
