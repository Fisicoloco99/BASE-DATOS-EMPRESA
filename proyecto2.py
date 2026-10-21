# tabla empleados, nombre, apellido , ID, asistencias , alos trabajados, DNI,todo lo que hace un CRUD , asistencias justificada o no, bonificaciones o no
# ver,agregar, funcion que hace de las asistencias, faltas justificadas o no,actualizar, eliminar
#Registro de empresa:Tabla empleados: id, nombre y apellido, anios trabajados, asistencias, dni. CRUD. Asistencias, justificada o no.  bonificaciones o no
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
        dni INTEGER
    )
""")

conexion_empleados.commit()


def comprobar(empleado,entry_,orden):
    variable=entry_.get()
    if variable=="":
        return empleado[orden]
    else:
        return variable

def new_empleado():
    nom_ape=entry_nom_ape.get()
    anio=entry_anio.get()
    asist=entry_asistencias.get()
    dni=entry_dni.get()
    cursor_empleados.execute("INSERT INTO empleados (nombre_apellido,anio_inicio,asistencias,dni) VALUES (?,?,?,?)",(nom_ape,anio,asist,dni))
    conexion_empleados.commit()
    ver()
    limpiar_entry()
    
def editar_empleado():
    p_id=entry_id.get()
    cursor_empleados.execute("SELECT * FROM empleados")
    empleados=cursor_empleados.fetchall()
    for empleado in empleados:
        if int(p_id)==empleado[0]:
            nom_ape=comprobar(empleado,entry_nom_ape,1)
            anio=comprobar(empleado,entry_anio,2)
            asist=comprobar(empleado,entry_asistencias,3)
            dni=comprobar(empleado,entry_dni,4)
            cursor_empleados.execute("UPDATE empleados SET nombre_apellido = ?, anio_inicio = ?, asistencias = ?, dni = ? WHERE id = ?",(nom_ape,anio,asist,dni,p_id))
            conexion_empleados.commit()
            ver()
            limpiar_entry()

def eliminar_empleado():
    p_id=entry_id.get()
    cursor_empleados.execute("DELETE FROM empleados WHERE id = ?",(p_id,))
    conexion_empleados.commit()
    ver()
    limpiar_entry()

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
ventana.title("Empresa")
ventana.geometry("1080x1240")
ventana.resizable(False,False)
label_id=tk.Label(ventana, text="ID")
label_id.pack()
entry_id=tk.Entry(ventana)
entry_id.pack()
label_nom_ape=tk.Label(ventana, text="Apellido nombre")
label_nom_ape.pack()
entry_nom_ape=tk.Entry(ventana)
entry_nom_ape.pack()
label_anios=tk.Label(ventana, text="Anios trabajados", padx = 10, pady = 10)
label_anios.pack()
entry_anio=tk.Entry(ventana)
entry_anio.pack()
label_asistencias=tk.Label(ventana, text="Asistencias")
label_asistencias.pack()
entry_asistencias=tk.Entry(ventana)
entry_asistencias.pack()
label_dni=tk.Label(ventana, text="DNI")
label_dni.pack()
entry_dni=tk.Entry(ventana)
entry_dni.pack()
label_asistencias_justificadas=tk.Label(ventana, text="Asistencias justificadas o no")
label_asistencias_justificadas.pack()
label_bonificaciones=tk.Label(ventana, text="Bonificaciones o no")
label_bonificaciones.pack()
lista = tk.Listbox(ventana)
lista.pack()
ver()
COLOR_FONDO = "#FBFBFB"
COLOR_TEXTO = "#010300"
#Botones
boton_editar = tk.Button(ventana,text ="EDITAR EMPLEADO",command=editar_empleado)
boton_editar.pack()
# Frames
frame_id = tk.Frame(ventana, bg=COLOR_FONDO)
frame_id.pack(pady=10)
frame_botones = tk.Frame(ventana, bg=COLOR_FONDO)
frame_botones.pack(fill="x", padx=50, pady=20) 
boton_agregar = tk.Button(frame_botones, text="AGREGAR EXPEDIENTE",command = new_empleado ,font=("Arial", 12), bg="green", fg="white")
boton_agregar.pack(side=tk.LEFT)
# Y aca tambien le puse fg="white" para que resalte mas
boton_eliminar = tk.Button(frame_botones, text="ELIMINAR ARCHIVOS", command=eliminar_empleado,font=("Arial", 12), bg="red", fg="white")
boton_eliminar.pack(side=tk.RIGHT)
ventana.mainloop()