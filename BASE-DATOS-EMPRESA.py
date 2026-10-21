#Registro de empresa:Tabla empleados: id, nombre y apellido, anios trabajados, asistencias, dni. CRUD. Asistencias, justificada o no.  bonificaciones o no
import sqlite3

import tkinter as tk

conexion_empleados = sqlite3.connect("Empleados.db")
cursor_empleados = conexion_empleados.cursor()

cursor_empleados.execute("""
    CREATE TABLE IF NOT EXISTS empleados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_apellido TEXT NOT NULL,
        anio_inicio TEXT NOT NULL,
        asistencias INTEGER,
        dni INTEGER,
    )
""")

conexion_empleados.commit()

def new_empleado():
    nom_ape=entry_nom_ape.get()
    anio=entry_anio.get()
    asist=entry_asistencias.get()
    dni=entry_dni.get()
    cursor_empleados.execute("INSERT INTO empleados (nombre_apellido,anio_inicio,asistencias,dni) VALUES (?,?,?,?)",(nom_ape,anio,asist,dni))
    conexion_empleados.commit()
    
def editar_empleado():
    p_id=entry_id.get()
    nom_ape=entry_nom_ape.get()
    anio=entry_anio.get()
    asist=entry_asistencias.get()
    dni=entry_dni.get()
    cursor_empleados.execute("UPDATE empleados SET nombre_apellido = ?, anio_inicio = ?, asistencias = ?, dni = ? WHERE id = ?",(nom_ape,anio,asist,dni,p_id))
    conexion_empleados.commit()

def eliminar_empleado():
    p_id=entry_id.get()
    cursor_empleados.execute("DELETE FROM empleados WHERE id = ?",(p_id,))
    conexion_empleados.commit()

def ver():
    lista.delete(0, tk.END)
    cursor_empleados.execute("SELECT * FROM empleados")
    for i in cursor_empleados.fetchall():
        lista.insert(tk.END, i)
        
def limpiar_entry():
    entry_id.delete(0,tk.END)
    entry_nom_ape.delete(0,tk.END)
    entry_anio.delete(0,tk.END)
    entry_asistencias.delete(0,tk.END)
    entry_dni.delete(0,tk.END)


ventana = tk.Tk()
ventana.title("Prueba Multiprocessing")
ventana.geometry("400x650")

label_id=tk.Label(ventana, text="ID")
label_id.pack()
entry_id=tk.Entry(ventana)
entry_id.pack()

label_nom_ape=tk.Label(ventana, text="nombre_apellido")
label_nom_ape.pack()
entry_nom_ape=tk.Entry(ventana)
entry_nom_ape.pack()

label_anio=tk.Label(ventana, text="anio")
label_anio.pack()
entry_anio=tk.Entry(ventana)
entry_anio.pack()

label_asistencias=tk.Label(ventana, text="asistencias")
label_asistencias.pack()
entry_asistencias=tk.Entry(ventana)
entry_asistencias.pack()

label_dni=tk.Label(ventana, text="asistencias")
label_dni.pack()
entry_dni=tk.Entry(ventana)
entry_dni.pack()

lista=tk.Listbox(ventana)
lista.pack()

ventana.mainloop()